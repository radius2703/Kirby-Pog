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
from cogs.imaging.base import despeckle, kuwahara, spread, noise
from cogs.imaging.base import image_edit


def setup(bot: Kirby):
    bot.add_cog(Noise(bot=bot))


class Noise(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def despeckle(self, ctx: commands.Context, member: discord.Member = None):
        member = member or ctx.author

        async with ctx.channel.typing():
            return await ctx.send(
                file=discord.File(
                    filename="despeckle.png",
                    fp=image_edit(await member.avatar_url.read(), despeckle)
                )
            )

    @commands.command()
    @commands.guild_only()
    async def kuwahara(self, ctx: commands.Context, radius: float, sigma: float, member: discord.Member = None):
        member = member or ctx.author

        async with ctx.channel.typing():
            return await ctx.send(
                file=discord.File(
                    filename="kuwahara.png",
                    fp=image_edit(await member.avatar_url.read(), kuwahara, radius=radius, sigma=sigma)
                )
            )

    @commands.command()
    @commands.guild_only()
    async def spread(self, ctx: commands.Context, radius: float, member: discord.Member = None):
        member = member or ctx.author

        async with ctx.channel.typing():
            return await ctx.send(
                file=discord.File(
                    filename="spread.png",
                    fp=image_edit(await member.avatar_url.read(), spread, radius=radius)
                )
            )

    @commands.command()
    @commands.guild_only()
    async def noise(self, ctx: commands.Context, noise_type: str, attenuate: float, member: discord.Member = None):
        member = member or ctx.author

        async with ctx.channel.typing():
            return await ctx.send(
                file=discord.File(
                    filename="noise.png",
                    fp=image_edit(await member.avatar_url.read(), noise, noise_type=noise_type, attenuate=attenuate)
                )
            )
