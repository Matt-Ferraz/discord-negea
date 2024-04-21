
import discord
import os
from dotenv import load_dotenv
from utils.eventos import message_handler 
load_dotenv()

TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.content and message.content[0] != "#":
        return

    if message.author == client.user:
        return
    
    await message_handler(message, client)


client.run(TOKEN)
