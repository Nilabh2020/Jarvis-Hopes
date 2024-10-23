import os
import subprocess

def automate(command):
    if command.startswith("open"):
        app_name = command.split("open ")[1].strip()  # Get the app name after "open"
        open_application(app_name)

def open_application(app_name):
    # Open the command prompt and type the command to open the application
    command = f'start {app_name}'
    subprocess.run(command, shell=True)
