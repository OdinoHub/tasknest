from datetime import date, datetime, time, timezone
from zoneinfo import ZoneInfo

def local_today(tz_name: str, now: datetime | None = None) -> date:
    """Return today's date in the given IANA time zone."""
    if now is None:
        now = datetime.now(timezone.utc)
    zone = ZoneInfo(tz_name)
    return now.astimezone(zone).date()

def is_overdue(due: date, tz_name: str, now: datetime | None = None) -> bool:
    """Determine whether a task due date is overdue."""
    if now is None:
        now = datetime.now(timezone.utc)

    # Normalize dates to UTC to ensure consistent comparison regardless of server location
    zone = ZoneInfo(tz_name)
    due_date_midnight = datetime.combine(due, time.min, tzinfo=zone)
    utc_due_date = due_date_midnight.astimezone(ZoneInfo("UTC")).date()
    today_utc_date = now.astimezone(ZoneInfo("UTC")).date()

    return utc_due_date < today_utc_date
