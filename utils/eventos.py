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
        if len(message.content.split()) < 2:
            return await message.channel.send("Invalid command, missing champion name. \nUsage: #champ [name]")

        champ_name = message.content.split()[1]   

        if "list" in message.content.lower():
            return await message.channel.send("In development")

     
        champ_text = await get_champ_by_name(champ_name.capitalize())
        
        if "Access Denied" in champ_text:
            return await message.channel.send("Champion {} not found. Get the full list by #champs list".format(champ_name.capitalize()))

        champ_data = parse_response(champ_text)['data'][champ_name.capitalize()]
        title = champ_data['title']
        await message.channel.send(title)