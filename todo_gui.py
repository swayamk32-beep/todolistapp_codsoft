import tkinter as tk
from tkinter import messagebox
import json
import os

FILENAME = "tasks.json"

# ------------------- Data Handling -------------------

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

# ------------------- GUI Functions -------------------

def refresh_task_list():
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        display = f"[{'✓' if task['done'] else ' '}] {task['task']}"
        task_listbox.insert(tk.END, display)

def add_task():
    task_text = task_entry.get().strip()
    if task_text:
        tasks.append({"task": task_text, "done": False})
        task_entry.delete(0, tk.END)
        refresh_task_list()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        refresh_task_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def mark_done():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = not tasks[index]["done"]
        refresh_task_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark as complete/incomplete.")

def on_close():
    save_tasks(tasks)
    root.destroy()

# ------------------- Main GUI -------------------

tasks = load_tasks()

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x450")
root.configure(bg="#f0f0f0")

title_label = tk.Label(root, text="📝 To-Do List", font=("Arial", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

task_entry = tk.Entry(root, font=("Arial", 14), width=25)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", font=("Arial", 12), width=20, command=add_task)
add_button.pack(pady=5)

task_listbox = tk.Listbox(root, font=("Arial", 12), width=35, height=10, selectbackground="lightblue")
task_listbox.pack(pady=10)

mark_button = tk.Button(root, text="Mark Complete / Incomplete", font=("Arial", 12), width=25, command=mark_done)
mark_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", font=("Arial", 12), width=20, command=delete_task)
delete_button.pack(pady=5)

refresh_task_list()
root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
