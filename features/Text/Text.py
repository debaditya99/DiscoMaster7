from discord import app_commands
import discord
import asyncio
import json
import aiohttp

OLLAMA_API_URL = "http://localhost:11434/api/generate"
# Faster models: phi, tinyllama, orca-mini
# Balanced: mistral, llama2
# Better quality but slower: llama2:13b, mixtral
MODEL_NAME = "phi"  # Fast and efficient model

async def thinking_animation(message):
    dots = 0
    increasing = True
    while True:
        await message.edit(content=f"Thinking{'.' * dots}")
        await asyncio.sleep(0.5)
        
        if increasing:
            dots += 1
            if dots > 7:  # Max 7 dots
                dots = 7
                increasing = False
        else:
            dots -= 1
            if dots < 0:  # Back to 0 dots
                dots = 0
                increasing = True

async def get_ollama_response_streaming(prompt, message, thinking_task):
    """Get streaming response from Ollama API and update message in real-time"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(OLLAMA_API_URL, json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": True
            }) as response:
                response.raise_for_status()
                
                # Cancel thinking animation when we start receiving data
                if thinking_task and not thinking_task.done():
                    thinking_task.cancel()
                    try:
                        await thinking_task
                    except asyncio.CancelledError:
                        pass
                
                full_response = ""
                last_update = 0
                
                async for line in response.content:
                    if line:
                        try:
                            data = json.loads(line)
                            if "response" in data:
                                full_response += data["response"]
                                
                                # Update message every 20 characters or at the end
                                if len(full_response) - last_update > 20 or data.get("done", False):
                                    if len(full_response) <= 2000:
                                        await message.edit(content=full_response)
                                    last_update = len(full_response)
                            
                            if data.get("done", False):
                                break
                        except json.JSONDecodeError:
                            continue
                
                return full_response
    except aiohttp.ClientError as e:
        raise Exception(f"Failed to communicate with Ollama: {str(e)}")

async def get_ollama_response(prompt):
    """Get complete response from Ollama API (non-streaming)"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(OLLAMA_API_URL, json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            }) as response:
                response.raise_for_status()
                data = await response.json()
                return data["response"]
    except aiohttp.ClientError as e:
        raise Exception(f"Failed to communicate with Ollama: {str(e)}")

async def setup(bot):
    @bot.tree.command(name="text", description="Have a conversation with the AI")
    @app_commands.describe(content="What would you like to discuss?")
    async def text_command(interaction: discord.Interaction, content: str):
        # Send initial response
        await interaction.response.send_message("Thinking...")
        message = await interaction.original_response()
        
        # Start the thinking animation task
        thinking_task = asyncio.create_task(thinking_animation(message))
        
        try:
            # Get response from Ollama
            response = await get_ollama_response(content)
            
            # Cancel the thinking animation
            thinking_task.cancel()
            try:
                await thinking_task
            except asyncio.CancelledError:
                pass
            
            # Update the message with the actual response
            # Split long responses into chunks if needed
            if len(response) > 2000:
                chunks = [response[i:i+1990] for i in range(0, len(response), 1990)]
                await message.edit(content=chunks[0])
                for chunk in chunks[1:]:
                    await interaction.followup.send(chunk)
            else:
                await message.edit(content=response)
            
        except Exception as e:
            # Cancel the thinking animation
            thinking_task.cancel()
            try:
                await thinking_task
            except asyncio.CancelledError:
                pass
            
            error_message = f"Sorry, I encountered an error: {str(e)}"
            await message.edit(content=error_message)
    
    @bot.tree.command(name="textstream", description="Have a conversation with the AI (streaming response)")
    @app_commands.describe(content="What would you like to discuss?")
    async def textstream_command(interaction: discord.Interaction, content: str):
        # Send initial response
        await interaction.response.send_message("Thinking...")
        message = await interaction.original_response()
        
        # Start the thinking animation task
        thinking_task = asyncio.create_task(thinking_animation(message))
        
        try:
            # Get streaming response from Ollama
            response = await get_ollama_response_streaming(content, message, thinking_task)
            
            # Handle long responses
            if len(response) > 2000:
                chunks = [response[i:i+1990] for i in range(0, len(response), 1990)]
                await message.edit(content=chunks[0])
                for chunk in chunks[1:]:
                    await interaction.followup.send(chunk)
            
        except Exception as e:
            # Cancel the thinking animation if still running
            if not thinking_task.done():
                thinking_task.cancel()
                try:
                    await thinking_task
                except asyncio.CancelledError:
                    pass
            
            error_message = f"Sorry, I encountered an error: {str(e)}"
            await message.edit(content=error_message)
