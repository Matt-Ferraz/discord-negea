from discord import Client, Intents, Game, Status


intents = Intents.default()
intents.message_content = True

client = Client(intents=intents)

async def set_status(custom_status):
    game = Game(custom_status)
    await client.change_presence(status=Status.idle, activity=game)
