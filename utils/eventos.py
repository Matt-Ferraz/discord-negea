async def message_handler(message: str, client):
    print(message)
    if message.author == client.user:
        return

    if message.content.find('macaco') > 0 or message.content.lower() == "macaco":
        await message.channel.send(':monkey: :monkey: :monkey: :monkey:')