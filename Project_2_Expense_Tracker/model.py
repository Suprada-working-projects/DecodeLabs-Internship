"""
model.py

This file is responsible for all data-related operations.

It loads expenses from a JSON file,
adds new expenses,
and saves them permanently.
"""

# Import JSON module
import json

# File name used for storing expenses
FILE_NAME = "expenses.json"


def load_expenses():
    """
    Load expenses from JSON file.

    If file is missing or empty,
    return an empty list.
    """

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses(expenses):
    """
    Save expense list to JSON file.
    """

    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(amount):
    """
    Add one expense.

    Every expense is stored
    as a dictionary.
    """

    expenses = load_expenses()

    new_expense = {
        "id": len(expenses) + 1,
        "amount": amount
    }

    # append() adds dictionary to list
    expenses.append(new_expense)

    save_expenses(expenses)


def get_expenses():
    """
    Return all stored expenses.
    """

    return load_expenses()