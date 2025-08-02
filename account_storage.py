import csv
import os

def save_account(email, password, name, file="accounts.csv"):
    """
    Saves a new fake account to the CSV file.

    Args:
        email (str): Email address.
        password (str): Password.
        name (str): Full name.
        file (str): CSV filename (default is 'accounts.csv').
    """
    file_exists = os.path.exists(file)

    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Email", "Password", "Name"])  # Header row
        writer.writerow([email, password, name])

def load_accounts(file="accounts.csv"):
    """
    Loads all saved accounts from the CSV file.

    Returns:
        list of dict: Each row is a dictionary with keys 'Email', 'Password', and 'Name'.
    """
    accounts = []

    if os.path.exists(file):
        with open(file, newline="") as f:
            reader = csv.DictReader(f)
            accounts = list(reader)

    return accounts
