from utils.client import client

def find_emoji_by_name(emojis, name):
    for emoji in emojis:
        if emoji.name == name:
            return emoji
    return None

async def easter_eggs(message):
    if "lá ele" in message.content.lower():
        return await message.channel.send("https://tenor.com/view/oxi-oxi-la-ele-la-ele-homem-la-ele-sorriso-la-ele-gif-5780490895468984482")

    if "cinema" in message.content.lower():
        return await message.channel.send("https://tenor.com/view/luigi-that-is-cinema-mario-super-mario-bros-commercial-gif-1104736381557132611")

    if ":bill:" in message.content:
        emoji = find_emoji_by_name(client.emojis, "50")
        return await message.channel.send(emoji)

    if "kkkkkkkkkkkkkkkkkkkkkkkk" in message.content.lower():
        emoji = find_emoji_by_name(client.emojis, "50")
        return await message.channel.send("qual é a graça?")

    if "imaginei" in message.content.lower() and "que" in message.content.lower() and "perguntaria" in message.content.lower():
        return await message.channel.send("é que eu pensei numa piada")

    if "não" in message.content.lower() or "nao" in message.content.lower() and "entenderia" in message.content.lower():
        return await message.channel.send("senhoras e senhores")


    if "bora bill" in message.content.lower():
        emoji = find_emoji_by_name(client.emojis, "bill")
        print(emoji, "emoji")
        return await message.channel.send(emoji)
