from faker import Faker
from email_manager import get_temp_email
from account_storage import save_account

fake = Faker()

def create_account():
    email, username, domain = get_temp_email()
    full_name = fake.name()
    password = fake.password()
    
    # Simulate delay or page interaction here
    print(f"[+] Created: {email} | {password}")
    
    save_account(email, password, full_name)
    return {"email": email, "password": password, "name": full_name}