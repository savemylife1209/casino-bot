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
    print(f'Logged in as {client.user}')

for filename in os.listdir(COG_FOLDER):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
