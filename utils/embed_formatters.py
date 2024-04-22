from discord import Embed

def format_embed_message(str: str) -> Embed:
    embed = Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0xFF5733)
    embed.set_author(name="Author Name", icon_url="https://upload.wikimedia.org/wikipedia/commons/7/70/Example.png")
    embed.set_thumbnail(url="https://example.com/thumbnail.png")
    embed.add_field(name="Field Name", value="Field Value", inline=False)
    embed.set_image(url="https://upload.wikimedia.org/wikipedia/commons/7/70/Example.png")
    embed.set_footer(text="Footer Text", icon_url="https://upload.wikimedia.org/wikipedia/commons/7/70/Example.png")

    return embed
