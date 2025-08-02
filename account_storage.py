import csv
import os

def save_account(email, password, name, file="accounts.csv"):
    exists = os.path.exists(file)
    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow(["Email", "Password", "Name"])
        writer.writerow([email, password, name])

def load_accounts(file="accounts.csv"):
    accounts = []
    if os.path.exists(file):
        with open(file, newline="") as f:
            reader = csv.DictReader(f)
            accounts = list(reader)
    return accounts