"""
main.py

This is the starting point of the program.

It handles user input.
"""

# Import functions

from model import add_task
from view import show_tasks


def main():

    while True:

        print("====== TO DO LIST ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice : ")

        if choice == "1":

            task = input("Enter task : ")

            add_task(task)

            print("Task Added Successfully.\n")

        elif choice == "2":

            show_tasks()

        elif choice == "3":

            print("Thank You!")

            break

        else:

            print("Invalid Choice\n")


# Main Guard
# This ensures the program starts
# only when main.py is executed.

if __name__ == "__main__":
    main()