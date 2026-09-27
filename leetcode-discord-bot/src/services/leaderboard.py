def generate_leaderboard(user_progress_list):
    leaderboard = sorted(user_progress_list, key=lambda x: x['completions'], reverse=True)
    return leaderboard