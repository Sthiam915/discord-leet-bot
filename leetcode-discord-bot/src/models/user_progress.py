class UserProgress:
    def __init__(self, user_id):
        self.user_id = user_id
        self.daily_completions = {}
        self.times_taken = {}
        self.missed_days = 0

    def mark_done(self, date, time_taken):
        self.daily_completions[date] = True
        self.times_taken[date] = time_taken

    def track_completion(self, date):
        if date not in self.daily_completions:
            self.missed_days += 1

    def get_average_time(self):
        if not self.times_taken:
            return 0
        return sum(self.times_taken.values()) / len(self.times_taken)

    def get_missed_days(self):
        return self.missed_days

    def get_completion_count(self):
        return len(self.daily_completions)