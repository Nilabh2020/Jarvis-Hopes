from plyer import notification
import time

# Send a test notification
notification.notify(
    title="Test Notification",
    message="This is a test notification!",
    timeout=10  # Notification duration in seconds
)

# Wait a few seconds to allow the notification to appear
time.sleep(10)
