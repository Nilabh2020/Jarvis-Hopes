import psutil

def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    return f"Your CPU is currently at {cpu_percent}% usage."
