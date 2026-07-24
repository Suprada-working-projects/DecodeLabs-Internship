"""
model.py

This file contains all the logic for
generating and storing passwords.
"""

import json
import string
import secrets

FILE_NAME = "passwords.json"


def load_passwords():
    """
    Load passwords from JSON file.
    """

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_passwords(passwords):
    """
    Save passwords into JSON file.
    """

    with open(FILE_NAME, "w") as file:
        json.dump(passwords, file, indent=4)


def generate_password(length):
    """
    Generate a secure random password.
    """

    # Character pool
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    # Create list of random characters
    password_list = []

    for _ in range(length):
        password_list.append(secrets.choice(characters))

    # Professional way
    # Convert list into string using join()
    password = "".join(password_list)

    # Store password
    passwords = load_passwords()

    passwords.append({
        "id": len(passwords) + 1,
        "password": password
    })

    save_passwords(passwords)

    return password