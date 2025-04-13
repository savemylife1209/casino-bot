import discord
from discord.ext import commands
from modules.helpers import *
import os
import asyncio

client = commands.Bot(
    command_prefix=PREFIX,
    owner_ids=OWNER_IDS,
    intents=discord.Intents.all()
)

client.remove_command('help')

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

    # Load extensions inside on_ready or a dedicated function
    for filename in os.listdir(COG_FOLDER):
        if filename.endswith('.py'):
            try:
                await client.load_extension(f'cogs.{filename[:-3]}')
                print(f'Loaded {filename[:-3]}')
            except Exception as e:
                print(f'Failed to load {filename[:-3]}: {e}')
                continue

# Run the bot
if __name__ == '__main__':
    client.run(TOKEN)