import discord
from discord.ext import commands
from modules.helpers import *
import os
import asyncio
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "MyBot is ready"

async def main():
    client = commands.Bot(
        command_prefix=PREFIX,
        owner_ids=OWNER_IDS,
        intents=discord.Intents.all()
    )

    client.remove_command('help')

    for filename in os.listdir(COG_FOLDER):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

    await client.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
