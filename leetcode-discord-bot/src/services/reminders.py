import logging

import discord
from discord.ext import tasks

from ..models.user_progress import user_progress_data
from ..utils.date_utils import get_utc_date


class MonthlyMissTracker:
    def __init__(self, bot):
        self.bot = bot
        self.announced_misses = {}

    @tasks.loop(minutes=1)
    async def check(self):
        month = get_utc_date().strftime("%Y-%m")
        for guild in self.bot.guilds:
            channel = next(
                (
                    text_channel
                    for text_channel in guild.text_channels
                    if text_channel.name == "punishment"
                ),
                None,
            )
            if channel is None:
                continue

            for user_id, progress in list(user_progress_data.items()):
                missed_days = progress.get_missed_days_in_current_month()
                key = (guild.id, user_id)
                previous_month, previous_count = self.announced_misses.get(
                    key, (month, 6)
                )
                if missed_days <= 6 or (
                    previous_month == month and missed_days <= previous_count
                ):
                    continue

                try:
                    await channel.send(
                        f"<@{user_id}> has missed {missed_days} LeetCode days this month."
                    )
                except discord.HTTPException:
                    logging.exception(
                        "Could not announce missed days for user %s in guild %s",
                        user_id,
                        guild.id,
                    )
                    continue
                self.announced_misses[key] = (month, missed_days)

    @check.before_loop
    async def before_check(self):
        await self.bot.wait_until_ready()