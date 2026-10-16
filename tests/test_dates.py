from datetime import date, datetime, timezone
from tasklist.dates import is_overdue, local_today

# FIXED_NOW is 16 Oct 2026 08:00 UTC (10:00 in Malta, 17:00 in Tokyo, 04:00 in New York)
FIXED_NOW = datetime(2026, 10, 16, 8, 0, tzinfo=timezone.utc)

def test_due_yesterday_is_overdue_utc():
    assert is_overdue(date(2026, 10, 15), "UTC", now=FIXED_NOW) is True

def test_due_today_is_not_overdue_utc():
    assert is_overdue(date(2026, 10, 16), "UTC", now=FIXED_NOW) is False

def test_due_tomorrow_is_not_overdue_utc():
    assert is_overdue(date(2026, 10, 17), "UTC", now=FIXED_NOW) is False

def test_due_today_is_not_overdue_new_york():
    assert is_overdue(date(2026, 10, 16), "America/New_York", now=FIXED_NOW) is False

def test_local_today_utc():
    assert local_today("UTC", now=FIXED_NOW) == date(2026, 10, 16)

def test_local_today_tokyo_after_midnight():
    evening_now = datetime(2026, 10, 16, 20, 0, tzinfo=timezone.utc)
    assert local_today("Asia/Tokyo", now=evening_now) == date(2026, 10, 17)
