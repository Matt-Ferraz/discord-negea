from utils.riot import test_url, get_champ_by_name
import json

def parse_response(str: str) -> json:
    return json.loads(str)

async def message_handler(message: str, client):
    if "riot" in message.content.lower():
        champs = await test_url()
        await message.channel.send("``` \n" + champs +"\n ```")


    if "bibi" in message.content.lower():
        await message.channel.send(':blue_car: :blue_car: :blue_car: :blue_car:')
    
    if "champ" in message.content.lower():
        if len(message.content.split()) > 1 and message.content.split()[1] is not None:
            champ_text = await get_champ_by_name(message.content.split()[1].capitalize())
            champ_data = parse_response(champ_text)['data'][message.content.split()[1].capitalize()]
            title = champ_data['title']
            await message.channel.send(title)