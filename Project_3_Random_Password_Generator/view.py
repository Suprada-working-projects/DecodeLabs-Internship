"""
view.py

Responsible for displaying passwords.
"""

import json

FILE_NAME = "passwords.json"


def show_passwords():

    try:

        with open(FILE_NAME, "r") as file:

            passwords = json.load(file)

    except:

        passwords = []

    if len(passwords) == 0:

        print("\nNo passwords generated yet.\n")

        return

    print("\n===== GENERATED PASSWORDS =====\n")

    # Professional looping
    for index, item in enumerate(passwords, start=1):

        print(f"{index}. ID : {item['id']}")
        print(f"   Password : {item['password']}")