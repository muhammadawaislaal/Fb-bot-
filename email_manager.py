import requests
import time

def get_temp_email():
    domain = "1secmail.com"
    username = f"user{int(time.time())}"
    return f"{username}@{domain}", username, domain

def check_inbox(username, domain):
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain}"
    response = requests.get(url).json()
    if response:
        mail_id = response[0]['id']
        read_url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain}&id={mail_id}"
        content = requests.get(read_url).json()
        return content.get("body", "")
    return None