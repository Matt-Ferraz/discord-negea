import os
from dotenv import load_dotenv
from utils.eventos import message_handler
from utils.client import client, set_status
from utils.eastereggs import easter_eggs
load_dotenv()

TOKEN = os.getenv('TOKEN')

ENABLED_ZOAS = False

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await easter_eggs(message)

    if message.content and message.content[0] != "?":
        return

    if "ativar-modo-zoas" in message.content:
        ENABLED_ZOAS = True
        return

    if "update-status" in message.content and ENABLED_ZOAS is True:
        status = message.content.replace("?update-status ", '')
        await set_status(status)


    await message_handler(message, client)


client.run(TOKEN)
