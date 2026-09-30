import os
import time

import discord
from discord.ext import commands
from dotenv import load_dotenv

from .commands.daily import mark_done, mark_read
from .commands.stats import announce_stats, track_completions

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


class LeetCodeBot(commands.Bot):
    def __init__(self, command_prefix="!", intents=None):
        if intents is None:
            intents = discord.Intents.default()
        super().__init__(command_prefix=command_prefix, intents=intents)

    async def on_ready(self):
        print(f"Logged in as {self.user.name} - {self.user.id}")
        print("------")

    def setup_commands(self):
        self.add_command(mark_done)
        self.add_command(mark_read)
        self.add_command(track_completions)
        self.add_command(announce_stats)


def main():
    if not TOKEN:
        raise RuntimeError("DISCORD_TOKEN is missing. Add it to your .env file.")

    retry_delay = 5
    while True:
        intents = discord.Intents.default()
        intents.message_content = True
        bot = LeetCodeBot(command_prefix=os.getenv("COMMAND_PREFIX", "!"), intents=intents)
        bot.setup_commands()

        try:
            bot.run(TOKEN)
            break
        except discord.DiscordServerError as exc:
            print(f"Discord returned a server error ({exc.status}); retrying in {retry_delay} seconds.")
            time.sleep(retry_delay)
            retry_delay = min(retry_delay * 2, 60)


if __name__ == "__main__":
    main()