from discord.ext import commands
from datetime import datetime
from models.user_progress import UserProgress

user_progress_data = {}

async def mark_done(ctx, time_taken: float):
    user_id = ctx.author.id
    if user_id not in user_progress_data:
        user_progress_data[user_id] = UserProgress(user_id)

    user_progress = user_progress_data[user_id]
    user_progress.mark_completion(datetime.now(), time_taken)
    await ctx.send(f"{ctx.author.mention}, your LeetCode daily challenge has been marked as done in {time_taken} minutes.")

def get_user_progress(user_id):
    return user_progress_data.get(user_id, None)