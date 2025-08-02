import streamlit as st
from account_creator import create_account
from account_storage import load_accounts
from facebook_simulator import simulate_follow

st.set_page_config(page_title="Facebook Auto Bot", page_icon="🤖")

st.title("📣 Facebook Auto Follower Bot (Simulated)")

num_accounts = st.number_input("How many accounts to create?", min_value=1, max_value=50, value=5)
profile_url = st.text_input("Enter Facebook Profile URL to follow")

# Automatically create accounts and simulate follow
if num_accounts > 0 and profile_url:
    with st.spinner("Creating accounts..."):
        for _ in range(num_accounts):
            create_account()
        st.success(f"{num_accounts} fake accounts created!")

    with st.spinner("Following the profile..."):
        accounts = load_accounts()
        results = simulate_follow(profile_url, num_accounts, accounts)
        for r in results:
            st.success(r)
