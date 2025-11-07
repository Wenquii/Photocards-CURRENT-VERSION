import os

import discord

from commands import get_command_class
from constants import COMMAND_PREFIX, ALLOWED_CHANNELS

token = os.getenv("DISCORD_PHOTOCARD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    elif message.channel.id not in ALLOWED_CHANNELS:
        return
    elif not message.content.startswith(COMMAND_PREFIX):
        return

    await message.channel.send(**get_command_class(message).process())


client.run(token)
