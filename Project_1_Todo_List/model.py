"""
model.py

This file handles all DATA related work.

It is called the Model because it stores,
loads and modifies our task data.
"""

# Import JSON library
# JSON is used to permanently store data inside tasks.json
import json

# File where tasks are stored
FILE_NAME = "tasks.json"


# -----------------------------
# Function : Load Tasks
# -----------------------------
def load_tasks():
    """
    Reads tasks from tasks.json.

    If the file is empty,
    return an empty list.
    """

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


# -----------------------------
# Function : Save Tasks
# -----------------------------
def save_tasks(tasks):
    """
    Saves the updated task list
    into tasks.json.
    """

    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# -----------------------------
# Function : Add Task
# -----------------------------
def add_task(task_name):
    """
    Adds a new task.

    Each task is a dictionary.

    Example

    {
        "id":1,
        "task":"Learn Python"
    }
    """

    # Load existing tasks
    tasks = load_tasks()

    # New ID
    new_id = len(tasks) + 1

    # Create dictionary
    task = {
        "id": new_id,
        "task": task_name
    }

    # append() adds the dictionary
    # into our list
    tasks.append(task)

    # Save again
    save_tasks(tasks)


# -----------------------------
# Function : Get Tasks
# -----------------------------
def get_tasks():
    """
    Returns all tasks.
    """

    return load_tasks()