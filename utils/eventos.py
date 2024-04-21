from utils.riot import test_url

async def message_handler(message: str, client):
    if message.content and message.content[0] != "#":
        return

    if message.author == client.user:
        return

    if message.content.lower().find('riot') or message.content.lower() == "riot":
        test_url()


    if message.content.lower().find('bibi') > 0 or message.content.lower() == "bibi":
        await message.channel.send(':blue_car: :blue_car: :blue_car: :blue_car:')