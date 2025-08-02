def simulate_follow(profile_link, num, accounts):
    results = []
    for i in range(min(num, len(accounts))):
        acc = accounts[i]
        results.append(f"{acc['email']} followed {profile_link}")
    return results