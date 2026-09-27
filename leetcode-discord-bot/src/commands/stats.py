from models.user_progress import UserProgress
from datetime import datetime, timedelta

user_progress_data = {}

def track_completions(user_id):
    today = datetime.now().date()
    if user_id not in user_progress_data:
        user_progress_data[user_id] = UserProgress(user_id)
    
    user_progress_data[user_id].daily_completions[today] = user_progress_data[user_id].daily_completions.get(today, 0) + 1

def announce_stats(user_id):
    if user_id not in user_progress_data:
        return "No data available for this user."
    
    user_progress = user_progress_data[user_id]
    total_days = len(user_progress.daily_completions)
    missed_days = 30 - total_days
    average_time = sum(user_progress.times_taken) / len(user_progress.times_taken) if user_progress.times_taken else 0

    stats_message = (
        f"User: {user_id}\n"
        f"Total Days Completed: {total_days}\n"
        f"Days Missed: {missed_days}\n"
        f"Average Time: {average_time:.2f} minutes\n"
    )
    
    return stats_message