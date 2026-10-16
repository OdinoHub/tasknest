from dataclasses import dataclass
from datetime import date, timedelta

@dataclass
class Task:
    title: str
    due: date

def demo_tasks(today: date) -> list[Task]:
    """Return five sample tasks relative to the provided today date."""
    return [
        Task("Buy groceries", today - timedelta(days=1)),
        Task("Pay electricity bill", today),
        Task("Schedule dentist appointment", today),
        Task("Water the plants", today + timedelta(days=1)),
        Task("Read a new book", today + timedelta(days=3)),
    ]
