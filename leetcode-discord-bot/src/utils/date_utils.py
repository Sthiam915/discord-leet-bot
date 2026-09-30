from datetime import datetime, timedelta, timezone


def get_utc_date():
    return datetime.now(timezone.utc).date()

def is_day_missed(date, completed_dates):
    return date not in completed_dates

def calculate_average_time(times):
    if not times:
        return 0
    return sum(times) / len(times)

def get_dates_in_month(year, month):
    first_day = datetime(year, month, 1)
    last_day = (first_day + timedelta(days=31)).replace(day=1) - timedelta(days=1)
    return [first_day + timedelta(days=i) for i in range((last_day - first_day).days + 1)]