from port_scanner import scan_ports
from dir_bforcer import brute_dirs
from login_bforce import brute_login

def main():
    print("=== Penetration Testing Toolkit ===")
    print("1. Port Scanner")
    print("2. Directory Bruteforcer")
    print("3. Login Bruteforce Simulator")

    choice = input("Choose module: ")

    if choice == "1":
        target = input("Enter target IP or domain: ")
        scan_ports(target)

    elif choice == "2":
        url = input("Enter target URL (http://example.com): ")
        brute_dirs(url)

    elif choice == "3":
        login_url = input("Enter login URL : ")
        brute_login(login_url)

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
