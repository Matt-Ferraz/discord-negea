from discord import Embed
# embed = Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0xFF5733)
# embed.set_author(name="Author Name", icon_url="https://upload.wikimedia.org/wikipedia/commons/7/70/Example.png")
# embed.set_thumbnail(url="https://example.com/thumbnail.png")
# embed.add_field(name="Field Name", value="Field Value", inline=False)
# embed.set_image(url="https://upload.wikimedia.org/wikipedia/commons/7/70/Example.png")
# embed.set_footer(text="Footer Text", icon_url="https://upload.wikimedia.org/wikipedia/commons/7/70/Example.png")
#

def format_embed_champion(champ, usuario) -> Embed:
    author_name = usuario.nick if usuario.nick is not None else usuario.name
    embed = Embed(title=champ['name'], description=champ['title'], color=0xeeeeee)
    embed.set_author(name=author_name, icon_url=usuario.avatar)
    embed.set_thumbnail(url="https://ddragon.leagueoflegends.com/cdn/12.4.1/img/champion/" + champ['image_url'])

    embed.add_field(name=champ['passive_name'], value=champ['passive_desc'], inline=False)

    return embed
