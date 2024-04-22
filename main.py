import os
from dotenv import load_dotenv
from utils.eventos import message_handler
from utils.client import client
load_dotenv()

TOKEN = os.getenv('TOKEN')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):

    if message.content and message.content[0] != "?":
        return

    if message.author == client.user:
        return

    # await get_user_profile_pic(message.author.id)


    await message_handler(message, client)


client.run(TOKEN)
