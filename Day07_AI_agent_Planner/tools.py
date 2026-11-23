from datetime import datetime

def get_current_time():
    """Return the current date and time."""

    return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

def days_until_new_year():
    """Return how many days are left until next 1st January."""

    today = datetime.now().date()
    new_year = today.replace(year=today.year + 1, month=1, day=1)
    days_left = (new_year - today).days

    return f"{days_left} days left until New Year {new_year.year} (today is {today.strftime('%d-%m-%Y')})"

import random

def roll_dice():
    """Return a random number between 1 and 6."""

    return random.randint(1, 6)

import secrets
import string

def generate_password(length=12):
    """Generate a secure random password."""

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ""

    for _ in range(length):
        password += secrets.choice(characters)

    return password

def read_text_file(filename):

    try:

        with open(filename, "r") as file:

            return file.read()

    except FileNotFoundError:

        return "Error: File not found."

