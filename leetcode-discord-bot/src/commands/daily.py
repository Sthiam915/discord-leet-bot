from discord.ext import commands

from ..models.user_progress import UserProgress, user_progress_data
from ..utils.date_utils import get_utc_date


def parse_time_input(value):
    try:
        hours_str, minutes_str, seconds_str = value.split(":")
        hours = int(hours_str)
        minutes = int(minutes_str)
        seconds = int(seconds_str)

        if hours < 0 or not 0 <= minutes < 60 or not 0 <= seconds < 60:
            raise ValueError

        total_seconds = (hours * 60 * 60) + (minutes * 60) + seconds
        return total_seconds / 60
    except (ValueError, TypeError):
        raise ValueError("Use time in H:M:S format like 1:25:30.")


@commands.command(name="mark_done")
async def mark_done(ctx, time_taken: str, problem: str):
    try:
        total_minutes = parse_time_input(time_taken)
    except ValueError as exc:
        await ctx.send(f"{ctx.author.mention}, {exc}")
        return

    problem = problem.strip().lower()
    is_daily = problem == "daily"
    if not is_daily and (not problem.isdecimal() or int(problem) <= 0):
        await ctx.send(
            f"{ctx.author.mention}, specify `daily` or a positive LeetCode problem number."
        )
        return

    user_id = ctx.author.id
    if user_id not in user_progress_data:
        user_progress_data[user_id] = UserProgress(user_id)

    user_progress = user_progress_data[user_id]
    today = get_utc_date()
    if is_daily:
        user_progress.mark_done(today, total_minutes)
        await ctx.send(
            f"{ctx.author.mention}, your daily challenge is marked done in {time_taken}."
        )
    else:
        problem_number = int(problem)
        user_progress.mark_problem_done(today, problem_number, total_minutes)
        await ctx.send(
            f"{ctx.author.mention}, LeetCode problem #{problem_number} is marked done in {time_taken}. "
            "Only daily completion times count toward the daily average."
        )


@commands.command(name="mark_read")
async def mark_read(ctx, time_taken: str, problem: str):
    try:
        total_minutes = parse_time_input(time_taken)
    except ValueError as exc:
        await ctx.send(f"{ctx.author.mention}, {exc}")
        return

    if not problem.isdecimal() or int(problem) <= 0:
        await ctx.send(f"{ctx.author.mention}, provide a positive LeetCode problem number.")
        return

    user_id = ctx.author.id
    if user_id not in user_progress_data:
        user_progress_data[user_id] = UserProgress(user_id)

    user_progress_data[user_id].mark_read(
        get_utc_date(), int(problem), total_minutes
    )
    await ctx.send(
        f"{ctx.author.mention}, LeetCode problem #{int(problem)} is marked done in {time_taken}. "
        "This counts as a daily completion but is excluded from your average time."
    )


def get_user_progress(user_id):
    return user_progress_data.get(user_id, None)