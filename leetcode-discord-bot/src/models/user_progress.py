from datetime import datetime, timedelta

from ..utils.date_utils import get_utc_date


user_progress_data = {}


class UserProgress:
    def __init__(self, user_id):
        self.user_id = user_id
        self.daily_completions = {}
        self.times_taken = {}
        self.leetcode_completions = []
        self.missed_days = 0

    def mark_done(self, date, time_taken):
        self.daily_completions[date] = True
        self.times_taken[date] = time_taken

    def mark_completion(self, date, time_taken):
        self.mark_done(date, time_taken)

    def mark_problem_done(self, date, problem_number, time_taken):
        self.leetcode_completions.append((date, problem_number, time_taken))

    def mark_read(self, date, problem_number, time_taken):
        self.daily_completions[date] = True
        self.mark_problem_done(date, problem_number, time_taken)

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

    def get_missed_days_in_current_month(self):
        today = get_utc_date()
        year = today.year
        month = today.month
        first_day = datetime(year, month, 1).date()
        last_day = today - timedelta(days=1)

        missed = 0
        current_day = first_day

        while current_day <= last_day:
            if current_day not in self.daily_completions:
                missed += 1
            current_day += timedelta(days=1)

        return missed