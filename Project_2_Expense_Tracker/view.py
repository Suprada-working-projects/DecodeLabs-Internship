"""
view.py

Responsible for displaying data.
"""

from model import get_expenses


def show_summary():
    """
    Display all expenses
    and the total amount.
    """

    expenses = get_expenses()

    if len(expenses) == 0:
        print("\nNo expenses recorded.\n")
        return

    print("\n===== EXPENSE LIST =====\n")

    total = 0

    # enumerate() is the professional way
    # to loop through a list.

    for index, expense in enumerate(expenses, start=1):

        print(f"{index}. ID : {expense['id']}")
        print(f"   Amount : ₹{expense['amount']}")

        # Accumulator Pattern
        total += expense["amount"]

    print("\n--------------------")
    print(f"Total Spent : ₹{total}")