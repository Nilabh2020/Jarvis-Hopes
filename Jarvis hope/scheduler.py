import schedule
import time
from plyer import notification
import threading

def task_reminder(task):
    # Send a notification for the scheduled task
    notification.notify(
        title="Task Reminder",
        message=f"It's time to: {task}",
        timeout=10  # Notification duration in seconds
    )

def schedule_task(task, time_str):
    try:
        schedule.every().day.at(time_str).do(task_reminder, task)
        print(f"Task '{task}' scheduled at {time_str}.")

        # Start a thread to run the scheduler
        threading.Thread(target=run_scheduler, daemon=True).start()
    except Exception as e:
        print(f"Error scheduling task - {e}")

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)  # Wait for one second before checking again

