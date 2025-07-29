import os
import discord
import os
import discord
from discord import app_commands
from dotenv import load_dotenv
import importlib
import pkgutil

# Load environment variables
load_dotenv()

# Initialize Discord client with all intents
class DiscoMaster7Bot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.tree = app_commands.CommandTree(self)
        
    async def setup_hook(self):
        # This will be called when the bot starts
        print("Bot is setting up...")
        # Clear all existing commands
        print("Clearing existing commands...")
        self.tree.clear_commands(guild=None)
        await self.load_features()
        # Force sync with Discord
        print("Syncing commands with Discord...")
        await self.tree.sync()
        print("Commands synced successfully!")

    async def load_features(self):
        print("Loading features...")
        features_path = "features"
        print(f"Looking for features in: {os.path.abspath(features_path)}")
        
        # List all directories in features path
        for item in os.listdir(features_path):
            if os.path.isdir(os.path.join(features_path, item)) and not item.startswith('__'):
                try:
                    print(f"Attempting to load feature: {item}")
                    module_name = f"{features_path}.{item}.{item}"
                    feature_module = importlib.import_module(module_name)
                    
                    if hasattr(feature_module, 'setup'):
                        print(f"Setting up feature: {item}")
                        await feature_module.setup(self)
                        print(f"Successfully loaded and set up feature: {item}")
                    else:
                        print(f"Warning: Feature {item} has no setup function")
                except Exception as e:
                    print(f"Failed to load feature {item}: {str(e)}")
                    import traceback
                    print(traceback.format_exc())

client = DiscoMaster7Bot()

@client.tree.command(name="dm7", description="Basic command to check if the bot is working")
async def dm7(interaction: discord.Interaction):
    await interaction.response.send_message("Hello! I'm DiscoMaster7, ready to help!")

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

# Run the bot
if __name__ == "__main__":
    TOKEN = os.getenv('DISCORD_TOKEN')
    if not TOKEN:
        raise ValueError("No token found! Make sure to set DISCORD_TOKEN in your .env file")
    client.run(TOKEN)
