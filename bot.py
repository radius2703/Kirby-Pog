import sys
import json
import time
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import ExtensionNotFound, NoEntryPointError, ExtensionAlreadyLoaded, ExtensionFailed


class Kirby(commands.AutoShardedBot):

    def __init__(self):
        super().__init__(
            command_prefix=self.get_prefix, owner_id=420244167726333953,
            activity=discord.Streaming(name="kirby!", url="https://twitch.tv/kirby_your_mom/"),
            reconnect=True, intents=discord.Intents.all()
        )
        self.started_at = time.time()

    async def start(self, *args, **kwargs) -> None:
        self.load_cogs(root_dir="cogs")
        await super().start(*args, **kwargs)

    def load_cogs(self, root_dir: str = '') -> None:
        exts_loaded_without_errors = []
        for ext in self.config.get("exts"):
            ext = ext if not root_dir else f"{root_dir}.{ext}"
            try:
                self.load_extension(ext)
            except ExtensionNotFound:
                print(f"Extension '{ext}' was not found.")
                exts_loaded_without_errors.append(False)
            except NoEntryPointError:
                print(f"Extension '{ext}' does not have an entry point.")
                exts_loaded_without_errors.append(False)
            except ExtensionAlreadyLoaded:
                print(f"Extension '{ext}' is already loaded.")
                exts_loaded_without_errors.append(False)
            except ExtensionFailed as e:
                print(f"Extension '{ext}' errored while loading:\n    {e}")
                exts_loaded_without_errors.append(False)
            else:
                print(f"Extension '{ext}' loaded successfully.")
                exts_loaded_without_errors.append(True)
        print(f"Cogs loaded with{'' if not all(exts_loaded_without_errors) else 'out'}"
              f" errors.")

    @property
    def config(self) -> dict:
        with open("./config.json", 'r') as config:
            return json.load(config)

    async def get_prefix(self, message: discord.Message) -> list:
        return commands.when_mentioned_or(self.config.get("prefix"))(self, message)

    async def close(self) -> None:
        await super().close()


if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    bot = Kirby()
    bot.run(bot.config.get("token"))
