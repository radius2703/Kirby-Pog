"""
MIT License

Copyright (c) 2021 radius

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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
