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
            reconnect=True, intents=discord.Intents.all(), case_insensitive=True
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
