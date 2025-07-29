# DiscoMaster7 Discord Bot

A modular Discord bot that can be configured with various features.

## Setup

1. Create a `.env` file in the root directory and add your Discord bot token:
   ```
   DISCORD_TOKEN=your_bot_token_here
   ```

2. Install the required packages:
   ```
   pip install discord.py python-dotenv
   ```

3. Run the bot:
   ```
   python bot.py
   ```

## Features

The bot is designed with a modular structure where features can be added independently. Current features:

- Base command: `/dm7` - Checks if the bot is working
- Feature1: `/feature1` - Example command from Feature1
- Feature2: `/feature2` - Example command from Feature2

## Adding New Features

1. Create a new directory in the `features` folder
2. Create a Python file with the same name as the directory
3. Implement your feature using the Discord.py commands
4. The bot will automatically load your feature on startup

## Permissions

The bot is designed to work with any level of permissions. It will only use the permissions it has been granted in Discord.
