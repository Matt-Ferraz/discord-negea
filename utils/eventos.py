import discord
from utils.riot import test_url, get_champ_by_name
from utils.embed_formatters import format_embed_champion
from utils.champ import format_champ_data
import json

def parse_response(str: str):
    return json.loads(str)

async def message_handler(message, client):
    if "champ" in message.content.lower():
        if len(message.content.split()) < 2:
            return await message.channel.send("Invalid command, too few arguments. \nUsage: #champ [name]")

        champ_name = message.content.split()[1].capitalize()
        champ_text = await get_champ_by_name(champ_name)

        if "Access Denied" in champ_text:
            return await message.channel.send("Champion {} not found. Get the full list by #champs list".format(champ_name))

        champ_parsed = parse_response(champ_text)['data'][champ_name]
        champ_data = format_champ_data(champ_parsed, champ_name)


        embed_champ = format_embed_champion(champ_data, message.author)
        view = discord.ui.View()
        for spell in champ_data['spells']:
            button = discord.ui.Button(label=spell.upper())
            view.add_item(button)

        await message.channel.send(embed=embed_champ, view=view)
