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
from discord.ext import commands
from cogs.imaging.base import polaroid, sepia, charcoal, swirl, flip, flop, spectrum, thicc
from cogs.imaging.base import image_edit


def setup(bot: Kirby):
    bot.add_cog(Fx(bot=bot))


class Fx(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def polaroid(self, ctx: commands.Context, member: discord.Member = None):
        member = member or ctx.author

        async with ctx.channel.typing():
            return await ctx.send(
                file=discord.File(
                    filename="polaroid.png",
                    fp=image_edit(await member.avatar_url.read(), polaroid)
                )
            )
    
    @commands.command()
    async def sepia(self, ctx: commands.Context, threshold: float, member: discord.Member = None):
        member = member or ctx.author

        async with ctx.channel.typing():
            return await ctx.send(
                file=discord.File(
                    filename="sepia.png",
                    fp=image_edit(await member.avatar_url.read(), sepia, threshold=threshold)
                )
            )

    @commands.command()
    async def charcoal(self, ctx: commands.Context, radius: float, sigma: float,
                       member: discord.Member = None):
        member = member or ctx.author

        async with ctx.channel.typing():
            return await ctx.send(
                file=discord.File(
                    filename="charcoal.png",
                    fp=image_edit(await member.avatar_url.read(), charcoal,
                                  radius=radius, sigma=sigma)
                )
            )

    @commands.command()
    async def swirl(self, ctx: commands.Context, degree: float, member: discord.Member = None):
        member = member or ctx.author

        async with ctx.channel.typing():
            return await ctx.send(
                file=discord.File(
                    filename="swirl.png",
                    fp=image_edit(await member.avatar_url.read(), swirl, degree=degree)
                )
            )

    @commands.command()
    async def flip(self, ctx: commands.Context, member: discord.Member = None):
        member = member or ctx.author

        async with ctx.channel.typing():
            return await ctx.send(
                file=discord.File(
                    filename="flip.png",
                    fp=image_edit(await member.avatar_url.read(), flip)
                )
            )

    @commands.command()
    async def flop(self, ctx: commands.Context, member: discord.Member = None):
        member = member or ctx.author

        async with ctx.channel.typing():
            return await ctx.send(
                file=discord.File(
                    filename="flop.png",
                    fp=image_edit(await member.avatar_url.read(), flop)
                )
            )

    @commands.command()
    async def spectrum(self, ctx: commands.Context, member: discord.Member = None):
        member = member or ctx.author

        async with ctx.channel.typing():
            return await ctx.send(
                file=discord.File(
                    filename="spectrum.png",
                    fp=image_edit(await member.avatar_url.read(), spectrum)
                )
            )
    
    @commands.command()
    async def thicc(self, ctx: commands.Context, amount: float, member: discord.Member = None):
        member = member or ctx.author

        async with ctx.channel.typing():
            return await ctx.send(
                file=discord.File(
                    filename="thicc.png",
                    fp=image_edit(await member.avatar_url.read(), thicc, amount=amount)
                )
            )    
