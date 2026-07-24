"""
main.py

Starting point of the application.

Implements

Input

↓

Process

↓

Output

↓

Storage
"""

from model import generate_password
from view import show_passwords


def main():

    while True:

        print("\n===== PASSWORD GENERATOR =====")

        print("1. Generate Password")
        print("2. View Generated Passwords")
        print("3. Exit")

        choice = input("Enter your choice : ")

        if choice == "1":

            try:

                # Input
                length = int(input("Enter password length : "))

                # Validation
                if length < 8:

                    print("Password should be at least 8 characters.")

                    continue

                elif length > 64:

                    print("Maximum allowed length is 64.")

                    continue

                # Process
                password = generate_password(length)

                # Output
                print("\nGenerated Password")

                print(password)

            except ValueError:

                print("Please enter a valid number.")

        elif choice == "2":

            show_passwords()

        elif choice == "3":

            print("Thank You!")

            break

        else:

            print("Invalid Choice.")


# Main Guard
if __name__ == "__main__":
    main()