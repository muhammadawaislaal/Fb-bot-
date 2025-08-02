import streamlit as st
from account_creator import create_account
from account_storage import load_accounts
from facebook_simulator import simulate_follow

st.title("📣 Facebook Auto Follower Bot (Simulated)")

num_accounts = st.number_input("How many accounts to create?", min_value=1, max_value=50, value=5)
profile_url = st.text_input("Profile URL to follow")

if st.button("Create Accounts"):
    st.write("Creating accounts...")
    for _ in range(num_accounts):
        create_account()
    st.success("Accounts created!")

if st.button("Follow Profile"):
    st.write("Following...")
    accounts = load_accounts()
    results = simulate_follow(profile_url, num_accounts, accounts)
    for r in results:
        st.success(r)