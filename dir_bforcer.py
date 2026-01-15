import requests

COMMON_DIRS = ["admin", "login", "dashboard", "uploads", "test"]

def brute_dirs(url):
    print("\n[+] Directory Bruteforce Started")
    for d in COMMON_DIRS:
        test_url = f"{url}/{d}"
        r = requests.get(test_url)
        if r.status_code == 200:
            print(f"[FOUND] {test_url}")
        else:
            print(f"[NOT FOUND] {test_url}")
