import discord
from bot import Kirby
from io import BytesIO
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFilter, ImageFont


def setup(bot: Kirby):
    bot.add_cog(GuildEvent(bot=bot))


class GuildEvent(commands.Cog):

    def __init__(self, bot: Kirby):
        self.bot = bot
        self.font_105 = ImageFont.truetype("./assets/on_member_join/fonts/theboldfont.ttf", 105)
        self.size_105 = self.font_105.getsize("Welcome!")[0]
        self.font_56 = ImageFont.truetype("./assets/on_member_join/fonts/futura.ttf", 56)
        self.font_45 = ImageFont.truetype("./assets/on_member_join/fonts/futura.ttf", 40)
        self.size_45 = self.font_45.getsize("#9999")
        self.mask = Image.open("./assets/on_member_join/mask.png")

    @staticmethod
    def _process_name(name: str) -> str:
        valid_name = ''.join([l for l in name if l.isalnum() or " "])
        if len(valid_name) > 17 or len(valid_name) != len(name):
            valid_name = valid_name[:17] + "..."
        return valid_name

    @staticmethod
    def _filter_letters(name: str) -> str:
        return ''.join([l for l in name if l not in "gjpqy"]) + "o"  # Safe guard

    @staticmethod
    def _trans(greeting: str, member: discord.Member):
        translation = {
            "[user]": f"**{str(member)}**",
            "[mention]": member.mention,
            "[guild]": f"**{member.guild.name}**"
        }
        for i in translation.keys():
            greeting = greeting.replace(i, translation[i])
        return greeting

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):

        member_name = self._process_name(member.name)
        filtered_name = self._filter_letters(member_name)
        channel = [c for c in member.guild.channels if isinstance(c, discord.TextChannel)]

        bg = Image.open("./assets/on_member_join/bg.png")
        profile = Image.open(BytesIO(await member.avatar_url.read())).resize((256, 256)).convert("RGBA")

        profile.putalpha(self.mask.resize(profile.size, Image.LANCZOS))

        bg_w, bg_h = bg.size
        profile_w, profile_h = profile.size

        bg.paste(profile, (bg_w // 2 - profile_w // 2, bg_h // 2 - profile_h // 2 - 120), mask=profile)

        txt_layer = Image.new("RGBA", size=bg.size, color=(0, 0, 0, 0))
        txt_draw = ImageDraw.Draw(txt_layer)

        t2 = bg_w // 2 - (self.font_56.getsize(member_name)[0] + self.size_45[0] + 10) // 2
        t3 = bg_w // 2 + self.font_56.getsize(member_name)[0] // 2 - self.size_45[0] // 2 + 10
        t0 = self.font_56.getsize(filtered_name)[1] - self.size_45[1]

        txt_draw.text((t2, 384), member_name, (0, 0, 0, 100), font=self.font_56)
        txt_draw.text((t3, 384 + t0), f"#{member.discriminator}",
                      (0, 0, 0, 100), font=self.font_45)

        txt_layer = txt_layer.filter(ImageFilter.GaussianBlur(2))
        txt_draw = ImageDraw.Draw(txt_layer)

        txt_draw.text((t2, 377), member_name, (255, 255, 255), font=self.font_56)
        txt_draw.text((t3, 377 + t0), f"#{member.discriminator}",
                      (255, 255, 255), font=self.font_45)

        bg.paste(txt_layer, mask=txt_layer)

        image = BytesIO()
        bg.save(image, format="PNG")
        image.seek(0)

        return await channel[0].send(embed=discord.Embed(
            description=self._trans("", member)
        ).set_image(url="attachment://welcome.png"),
            file=discord.File(filename="welcome.png", fp=image))
