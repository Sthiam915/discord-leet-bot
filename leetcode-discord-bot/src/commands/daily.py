from datetime import datetime

from discord.ext import commands

from ..models.user_progress import UserProgress, user_progress_data


def parse_time_input(value):
    try:
        hours_str, minutes_str, seconds_str = value.split(":")
        hours = int(hours_str)
        minutes = int(minutes_str)
        seconds = int(seconds_str)

        if minutes < 0 or seconds < 0 or hours < 0:
            raise ValueError

        total_seconds = (hours * 60 * 60) + (minutes * 60) + seconds
        return total_seconds / 60
    except (ValueError, TypeError):
        raise ValueError("Use time in H:M:S format like 1:25:30.")


@commands.command(name="mark_done")
async def mark_done(ctx, time_taken: str):
    user_id = ctx.author.id
    if user_id not in user_progress_data:
        user_progress_data[user_id] = UserProgress(user_id)

    try:
        total_minutes = parse_time_input(time_taken)
    except ValueError as exc:
        await ctx.send(f"{ctx.author.mention}, {exc}")
        return

    user_progress = user_progress_data[user_id]
    user_progress.mark_done(datetime.now().date(), total_minutes)
    await ctx.send(
        f"{ctx.author.mention}, your LeetCode daily challenge has been marked as done in {total_minutes:.2f} minutes."
    )


def get_user_progress(user_id):
    return user_progress_data.get(user_id, None)