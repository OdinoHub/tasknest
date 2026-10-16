# Tasklist

A tiny Flask to-do web app that displays a list of tasks with due dates, categorized by status ("Overdue", "Due today", or "Upcoming") across different time zones.

## Running the App

1. In VS Code, open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and select **Python: Create Environment** to set up your virtual environment `.venv`.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Go to the Run and Debug panel in VS Code and run **Run Tasklist**.
4. Open your browser at http://127.0.0.1:5050. You can switch time zones using the dropdown menu.

## Running Tests

You can run tests using the Testing panel in VS Code or directly from your terminal:

```bash
pytest -v
```

## Note

Demo tasks are dynamically generated relative to today's date in the selected time zone.
