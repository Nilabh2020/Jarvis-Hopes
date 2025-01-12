import tkinter as tk
from tkinter import ttk, messagebox
import firebase_admin
from firebase_admin import credentials, firestore
import json
import os

# Firebase setup
cred = credentials.Certificate('C:\\Users\\prach\\PycharmProjects\\pythonProject\\manage\\op.json')  # Replace with your Firebase credentials file path
firebase_admin.initialize_app(cred)
db = firestore.client()

# Reference to the tasks collection in Firestore
tasks_ref = db.collection('tasks')

# Function to load tasks from Firebase
def load_tasks():
    tasks = []
    docs = tasks_ref.stream()
    for doc in docs:
        task = doc.to_dict()
        task['id'] = doc.id
        tasks.append(task)
    return tasks

# Function to save tasks to Firebase
def save_tasks(tasks):
    for task in tasks:
        tasks_ref.add(task)

# Function to update the listbox
def update_listbox():
    listbox.delete(*listbox.get_children())
    tasks = load_tasks()
    for idx, task in enumerate(tasks, start=1):
        status = "✔ Completed" if task['completed'] else "✖ Pending"
        listbox.insert("", "end", values=(idx, task['task'], status))

# Function to add a task
def add_task():
    task_name = task_entry.get().strip()
    if task_name:
        tasks = load_tasks()
        tasks.append({"task": task_name, "completed": False})
        save_tasks(tasks)
        task_entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to mark a task as completed
def complete_task():
    try:
        selected_item = listbox.selection()[0]
        index = int(listbox.item(selected_item)['values'][0]) - 1  # Get the task index
        tasks = load_tasks()

        # Mark the task as completed (update the task in Firestore)
        task_id = tasks[index]['id']
        tasks_ref.document(task_id).update({"completed": True})

        update_listbox()  # Refresh the task list
    except IndexError:
        messagebox.showerror("Error", "No task selected!")


# Function to delete a task
def delete_task():
    try:
        selected_item = listbox.selection()[0]
        index = int(listbox.item(selected_item)['values'][0]) - 1  # Get the task index
        tasks = load_tasks()

        # Get the task's id and delete it from Firestore
        task_id = tasks[index]['id']
        tasks_ref.document(task_id).delete()

        update_listbox()  # Refresh the task list
        messagebox.showinfo("Info", f"Task deleted successfully!")
    except IndexError:
        messagebox.showerror("Error", "No task selected!")


# Function to draw a gradient on the canvas
def draw_gradient(canvas, width, height, start_color, end_color):
    r1, g1, b1 = canvas.winfo_rgb(start_color)
    r2, g2, b2 = canvas.winfo_rgb(end_color)

    r_ratio = (r2 - r1) / height
    g_ratio = (g2 - g1) / height
    b_ratio = (b2 - b1) / height

    for i in range(height):
        r = int(r1 + (r_ratio * i))
        g = int(g1 + (g_ratio * i))
        b = int(b1 + (b_ratio * i))
        color = f"#{r:04x}{g:04x}{b:04x}"
        canvas.create_line(0, i, width, i, fill=color)

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("500x500")
root.resizable(False, False)

# Create a Canvas for the gradient background
canvas = tk.Canvas(root, width=500, height=500, highlightthickness=0)
canvas.pack(fill="both", expand=True)
draw_gradient(canvas, 500, 500, "#1f1b37", "#6a67ce")  # Gradient from dark purple to lighter purple

# Title Label
title_label = tk.Label(canvas, text="To-Do List", font=("Helvetica", 18, "bold"), bg="#6a67ce", fg="white")
title_label_window = canvas.create_window(250, 30, window=title_label)

# Input Frame
input_frame = tk.Frame(canvas, bg="#6a67ce")
input_frame_window = canvas.create_window(250, 80, window=input_frame)

task_entry = ttk.Entry(input_frame, width=30)
task_entry.grid(row=0, column=0, padx=5, pady=5)

add_button = tk.Button(input_frame, text="Add Task", bg="#4e44a8", fg="white", command=add_task, relief="flat")
add_button.grid(row=0, column=1, padx=5, pady=5)

# Task List (Treeview)
listbox_frame = tk.Frame(canvas, bg="#6a67ce")
listbox_frame_window = canvas.create_window(250, 250, window=listbox_frame)

listbox = ttk.Treeview(listbox_frame, columns=("Index", "Task", "Status"), show="headings", height=10)
listbox.heading("Index", text="ID")
listbox.heading("Task", text="Task")
listbox.heading("Status", text="Status")
listbox.column("Index", width=50, anchor="center")
listbox.column("Task", width=280)
listbox.column("Status", width=120, anchor="center")
listbox.pack()

# Buttons Frame
button_frame = tk.Frame(canvas, bg="#6a67ce")
button_frame_window = canvas.create_window(250, 480, window=button_frame, anchor="s")

complete_button = tk.Button(button_frame, text="Mark as Completed", bg="#4e44a8", fg="white", command=complete_task, relief="flat")
complete_button.grid(row=0, column=0, padx=10, pady=5)

delete_button = tk.Button(button_frame, text="Delete Task", bg="#4e44a8", fg="white", command=delete_task, relief="flat")
delete_button.grid(row=0, column=1, padx=10, pady=5)

# Adjust the placement of the button frame to make it half visible
canvas.coords(button_frame_window, 250, 460)

# Initialize the listbox with tasks
update_listbox()

# Run the GUI event loop
root.mainloop()