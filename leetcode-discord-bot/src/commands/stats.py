from discord.ext import commands

from ..models.user_progress import UserProgress, user_progress_data
from ..utils.date_utils import get_utc_date


@commands.command(name="track_completions")
async def track_completions(ctx):
    user_id = ctx.author.id
    today = get_utc_date()
    if user_id not in user_progress_data:
        user_progress_data[user_id] = UserProgress(user_id)

    user_progress = user_progress_data[user_id]
    if today not in user_progress.daily_completions:
        user_progress.daily_completions[today] = True

    await ctx.send(f"{ctx.author.mention}, your daily completion was tracked for {today}.")


@commands.command(name="announce_stats")
async def announce_stats(ctx):
    user_id = ctx.author.id
    if user_id not in user_progress_data:
        await ctx.send("No data available for this user.")
        return

    user_progress = user_progress_data[user_id]
    total_days = len(user_progress.daily_completions)
    missed_days = user_progress.get_missed_days_in_current_month()
    average_time = user_progress.get_average_time()

    stats_message = (
        f"User: {ctx.author.mention}\n"
        f"Total Days Completed: {total_days}\n"
        f"Days Missed: {missed_days}\n"
        f"Average Time: {average_time:.2f} minutes\n"
    )
    await ctx.send(stats_message)


@commands.command(name="month_miss_check")
async def month_miss_check(ctx):
    for user_id, progress in user_progress_data.items():
        missed_days = progress.get_missed_days_in_current_month()
        if missed_days > 5:
            await ctx.send(f"<@{user_id}> has missed {missed_days} days this month.")
            return

    await ctx.send("No one in this server is currently above the 5-day missed threshold.")