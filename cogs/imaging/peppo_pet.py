import discord
from bot import Kirby
from PIL import Image
from io import BytesIO
from discord.ext import commands


def setup(bot: Kirby):
    bot.add_cog(Pet(bot=bot))


class Pet(commands.Cog):

    def __init__(self, bot: Kirby):
        self.bot = bot
        self.dim = [(176, 176), (184, 152), (189, 121), (189, 131), (176, 156)]

    @commands.command()
    async def pet(self, ctx: commands.Context, emote: discord.PartialEmoji = None):
        blank = Image.new("RGBA", (200, 200), (0, 0, 0, 0))
        if emote is None:
            profile = Image.open(BytesIO(await ctx.author.avatar_url.read())).convert("RGBA")
        else:
            profile = Image.open(BytesIO(await emote.url.read())).convert("RGBA")
        pet = BytesIO()
        frames = []
        for i, dim in zip(range(5), self.dim):
            b = blank.copy().convert("RGBA")
            hand = Image.open(f"./assets/peppo_pet/{i}.png").convert("RGBA")
            image = profile.resize(dim, Image.LANCZOS)
            b.paste(image, (200-dim[0], 200-dim[1]), mask=image)
            b.paste(hand, (0, 0), mask=hand)
            frames.append(b)

        frame, *frames = frames
        frame.save(pet, format="GIF", append_images=frames, save_all=True,
                   duration=60, loop=0, optimize=True, disposal=2)
        pet.seek(0)

        return await ctx.send(
            file=discord.File(
                filename="petpetpetpetpet.gif",
                fp=pet
            )
        )

    @pet.error
    async def error(self, ctx: commands.Context, error):
        if isinstance(error, commands.errors.PartialEmojiConversionFailure):
            return await ctx.send("Enter a valid custom emote.")
