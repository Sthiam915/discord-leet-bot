from discord.ext import commands
from commands.daily import mark_done
from commands.stats import track_completions, announce_stats

class LeetCodeBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user.name} - {self.user.id}')
        print('------')

    def setup_commands(self):
        self.add_command(mark_done)
        self.add_command(track_completions)
        self.add_command(announce_stats)

def main():
    import os
    from dotenv import load_dotenv
    load_dotenv()

    command_prefix = os.getenv('COMMAND_PREFIX', '!')
    intents = commands.Intents.default()
    bot = LeetCodeBot(command_prefix, intents)
    bot.setup_commands()

    bot.run(os.getenv('DISCORD_TOKEN'))

if __name__ == "__main__":
    main()