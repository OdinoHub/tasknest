from flask import Flask, render_template, request
from tasklist.dates import is_overdue, local_today
from tasklist.demo_data import demo_tasks

app = Flask(__name__)

VALID_TIMEZONES = ["UTC", "Europe/Malta", "Asia/Tokyo", "America/New_York"]

@app.route("/")
def index():
    tz_name = request.args.get("tz", "UTC")
    if tz_name not in VALID_TIMEZONES:
        tz_name = "UTC"

    today = local_today(tz_name)
    tasks = demo_tasks(today)

    task_list = []
    for task in tasks:
        if is_overdue(task.due, tz_name):
            status = "Overdue"
        elif task.due == today:
            status = "Due today"
        else:
            status = "Upcoming"

        task_list.append({
            "title": task.title,
            "due_formatted": task.due.strftime("%a %d %b %Y"),
            "status": status,
            "status_class": status.lower().replace(" ", "-"),
        })

    formatted_today = today.strftime("%a %d %b %Y")

    return render_template(
        "index.html",
        tasks=task_list,
        today_str=formatted_today,
        current_tz=tz_name,
        timezones=VALID_TIMEZONES,
    )
