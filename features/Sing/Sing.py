from discord import app_commands
import discord
import asyncio
import yt_dlp
import os

# YouTube DL configuration
ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',
    'extractaudio': True,
    'audioformat': 'mp3',
}

ffmpeg_options = {
    'options': '-vn',
}

ytdl = yt_dlp.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        
        if 'entries' in data:
            # Take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

class MusicPlayer:
    def __init__(self, bot):
        self.bot = bot
        self.voice_clients = {}  # Store voice clients for each guild

    async def join_channel(self, channel):
        """Join a voice channel"""
        if channel.guild.id in self.voice_clients:
            await self.voice_clients[channel.guild.id].move_to(channel)
        else:
            self.voice_clients[channel.guild.id] = await channel.connect()

    async def leave_channel(self, guild_id):
        """Leave a voice channel"""
        if guild_id in self.voice_clients:
            await self.voice_clients[guild_id].disconnect()
            del self.voice_clients[guild_id]

    async def play_song(self, interaction, url):
        """Play a song from URL or search query"""
        try:
            # Get the voice client for this guild
            voice_client = self.voice_clients.get(interaction.guild_id)
            if not voice_client:
                await interaction.followup.send('Bot is not connected to a voice channel!')
                return
                
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
            
            await interaction.followup.send(f'Now playing: {player.title}')
        except Exception as e:
            await interaction.followup.send(f'An error occurred: {str(e)}')

async def setup(bot):
    # Initialize the music player
    music_player = MusicPlayer(bot)
    
    @bot.tree.command(name='join', description='Join a voice channel')
    async def join(interaction: discord.Interaction):
        if not interaction.user.voice:
            await interaction.response.send_message('You need to be in a voice channel first!')
            return
        
        channel = interaction.user.voice.channel
        await music_player.join_channel(channel)
        await interaction.response.send_message(f'Joined {channel.name}!')

    @bot.tree.command(name='leave', description='Leave the voice channel')
    async def leave(interaction: discord.Interaction):
        await music_player.leave_channel(interaction.guild_id)
        await interaction.response.send_message('Left the voice channel!')

    @bot.tree.command(name='sing', description='Play music from a URL or search query')
    @app_commands.describe(query='URL or search query for the song to play')
    async def sing(interaction: discord.Interaction, query: str):
        if not interaction.guild.voice_client:
            if not interaction.user.voice:
                await interaction.response.send_message('You need to be in a voice channel first!')
                return
            await music_player.join_channel(interaction.user.voice.channel)
        
        await interaction.response.send_message(f'🎵 Looking for: {query}')
        await music_player.play_song(interaction, query)
