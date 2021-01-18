import discord
from bot import Kirby
from PIL import Image
from io import BytesIO
from discord.ext import commands


def setup(bot: Kirby):
    bot.add_cog(Slappers(bot=bot))


class Slappers(commands.Cog):

    def __init__(self, bot: Kirby):
        self.bot = bot

    @commands.command()
    async def slap(self, ctx: commands.Context, person_to_slap: discord.Member = None):
        bg = Image.open("./assets/slap/slap.bmp")

        slapper = ctx.author
        if person_to_slap is None:
            person_to_slap = ctx.author

        slapper = Image.open(BytesIO(await slapper.avatar_url.read()))
        person_to_slap = Image.open(BytesIO(await person_to_slap.avatar_url.read()))

        bg.paste(person_to_slap.resize((128, 128)), (173, 112))
        bg.paste(slapper.resize((128, 128)), (680, 102))

        image = BytesIO()
        bg.save(image, format="png")
        image.seek(0)

        return await ctx.send(file=discord.File(filename="slapped.png", fp=image))
