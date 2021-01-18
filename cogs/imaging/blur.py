import discord
from bot import Kirby
from discord.ext import commands
from cogs.imaging.base import blur, gaussian_blur, motion_blur, rotational_blur
from cogs.imaging.base import image_edit


def setup(bot: Kirby):
    bot.add_cog(Blur(bot=bot))


class Blur(commands.Cog):

    def __init__(self, bot: Kirby):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def blur(self, ctx: commands.Context, radius: float, sigma: float, member: discord.Member = None):
        member = member or ctx.author
        content = str()
        if radius < sigma:
            content = (f"**TIP**: It is recommended that the `radius` is greater than the `sigma`.",
                       f"**EG**:  {ctx.prefix}blur 4.0 2.0")

        async with ctx.channel.typing():
            return await ctx.send(
                content='\n'.join(content),
                file=discord.File(
                    filename="blur.png",
                    fp=image_edit(await member.avatar_url.read(), blur, radius=radius, sigma=sigma)
                )
            )

    @commands.command()
    @commands.guild_only()
    async def gaussian_blur(self, ctx: commands.Context, sigma: float, member: discord.Member = None):
        member = member or ctx.author

        async with ctx.channel.typing():
            return await ctx.send(
                content=f"**TIP**: Did you know the **{ctx.prefix}blur** command allows to change "
                        f"the radius and the sigma?\n"
                        f"**EG**:  {ctx.prefix}blur 4.0 2.0",
                file=discord.File(
                    filename="gaussian_blur.png",
                    fp=image_edit(await member.avatar_url.read(), gaussian_blur,
                                  sigma=sigma)
                )
            )

    @commands.command()
    @commands.guild_only()
    async def motion_blur(self, ctx: commands.Context, radius: float, sigma: float, angle: float,
                          member: discord.Member = None):
        member = member or ctx.author

        if radius < sigma:
            return await ctx.send("`radius` argument should always be greater than `sigma`.")

        async with ctx.channel.typing():
            return await ctx.send(
                file=discord.File(
                    filename="motion_blur.png",
                    fp=image_edit(await member.avatar_url.read(), motion_blur,
                                  radius=radius, sigma=sigma, angle=angle)
                )
            )

    @commands.command()
    @commands.guild_only()
    async def rotational_blur(self, ctx: commands.Context, angle: float, member: discord.Member = None):
        member = member or ctx.author

        async with ctx.channel.typing():
            return await ctx.send(
                file=discord.File(
                    filename="rotational_blur.png",
                    fp=image_edit(await member.avatar_url.read(), rotational_blur,
                                  angle=angle)
                )
            )
