import os
from datetime import datetime

from discord.ext import tasks

from ..models.user_progress import user_progress_data


class MonthlyMissTracker:
    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(minutes=1)
    async def check(self):
        channel_id = os.getenv("ANNOUNCEMENT_CHANNEL_ID")
        if not channel_id:
            return

        channel = self.bot.get_channel(int(channel_id))
        if channel is None:
            return

        for user_id, progress in list(user_progress_data.items()):
            missed_days = progress.get_missed_days_in_current_month()
            if missed_days > 5:
                await channel.send(
                    f"<@{user_id}> has missed {missed_days} LeetCode days this month. "
                    "Please mark your daily challenge as done soon."
                )

    @check.before_loop
    async def before_check(self):
        await self.bot.wait_until_ready()