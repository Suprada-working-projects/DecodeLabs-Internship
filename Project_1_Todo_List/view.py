"""
view.py

This file handles the DISPLAY part.

It prints information for the user.
"""

# Import function from model
from model import get_tasks


def show_tasks():
    """
    Displays all tasks.
    """

    tasks = get_tasks()

    # If list is empty
    if len(tasks) == 0:
        print("\nNo tasks available.\n")
        return

    print("\n===== TO DO LIST =====\n")

    # enumerate() is the professional way
    # of looping through a list.

    for index, task in enumerate(tasks, start=1):

        print(f"{index}. ID : {task['id']}")
        print(f"   Task : {task['task']}")
        print()