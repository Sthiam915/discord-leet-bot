from discord.ext import commands
import os
from src.bot import LeetCodeBot

if __name__ == "__main__":
    bot = LeetCodeBot(command_prefix="!")
    bot.run(os.getenv("DISCORD_TOKEN"))