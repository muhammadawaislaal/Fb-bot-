def simulate_follow(profile_link, num, accounts):
    """
    Simulate fake Facebook accounts following a profile link.

    Args:
        profile_link (str): The URL of the Facebook profile or page.
        num (int): Number of accounts to simulate.
        accounts (list): List of account dictionaries loaded from storage.

    Returns:
        list: Messages showing which account followed the profile.
    """
    results = []

    for i in range(min(num, len(accounts))):
        acc = accounts[i]

        # Try to safely extract email or fallback to string representation
        email = acc.get("Email") or acc.get("email") or str(acc)

        # Simulate following action
        results.append(f"{email} followed {profile_link}")

    return results
