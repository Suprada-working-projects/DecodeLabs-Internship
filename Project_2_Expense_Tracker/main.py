"""
main.py

Starting point of the program.

Implements the IPO model.

Input
↓

Process

↓

Output
"""

from model import add_expense
from view import show_summary


def main():

    # State variable
    # Must be outside loop
    total = 0

    print("===== Expense Tracker =====")

    print("Type 'quit' anytime to finish.\n")

    while True:

        expense = input("Enter expense amount : ")

        # Sentinel Value
        if expense.lower() == "quit":

            print("\nFinal Expense Report\n")

            show_summary()

            print("\nThank You!")

            break

        try:

            # Convert string into integer
            amount = int(expense)

            # Accumulator Pattern
            total += amount

            add_expense(amount)

            print(f"Current Total = ₹{total}\n")

        except ValueError:

            print("Invalid input!")
            print("Please enter numbers only.\n")


# Main Guard
if __name__ == "__main__":
    main()