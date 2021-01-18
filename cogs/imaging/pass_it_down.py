import discord
from bot import Kirby
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from discord.ext import commands


def setup(bot: Kirby):
    bot.add_cog(PassItDown(bot=bot))


class PassItDown(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.i = [*range(0, 230, 16)] + [*reversed(range(0, 230, 16))]
        self.j = [*range(0, 610, 16)]
        self.arial_font = ImageFont.truetype("./assets/pass_it_down/fonts/arial.ttf", 45)

    @commands.command()
    async def pass_it_down(self, ctx: commands.Context, emote: discord.PartialEmoji, *, text: str):

        base = Image.open("./assets/pass_it_down/pass_it_down.bmp")
        emote_image = Image.open(BytesIO(await emote.url.read())).convert("RGBA")
        emote_image.resize((128, emote_image.size[1] * 128 // emote_image.size[0]), Image.LANCZOS)
        base.paste(emote_image, (346, base.size[1]//2 - emote_image.size[1]//2), mask=emote_image)
        base_draw = ImageDraw.Draw(base)
        base_draw.text((307, 66), text, (255, 255, 255), font=self.arial_font)

        async with ctx.channel.typing():

            pass_it = BytesIO()
            frames = []

            for x, y in zip(self.i, self.j):
                base_clone = base.copy()
                base_clone.paste(emote_image, (x, y), mask=emote_image)
                frames.append(base_clone)
            frame, *frames = frames

            frame.save(pass_it, format="GIF", append_images=frames, save_all=True,
                       duration=40, loop=0)
            pass_it.seek(0)

            return await ctx.send(
                file=discord.File(
                    filename="pass_it_down.gif",
                    fp=pass_it
                )
            )

    @pass_it_down.error
    async def error(self, ctx: commands.Context, error):
        if isinstance(error, commands.errors.PartialEmojiConversionFailure):
            return await ctx.send("Enter a valid custom emote.")
