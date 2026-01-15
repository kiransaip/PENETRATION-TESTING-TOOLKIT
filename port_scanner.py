from utils import is_port_open

COMMON_PORTS = [11, 21, 22, 23, 25, 53, 80, 110, 443, 3306]

def scan_ports(target):
    print(f"\n[+] Port Scanning Started Against {target}")
    for port in COMMON_PORTS:
        if is_port_open(target, port):
            print(f"[OPEN] Port {port}")
        else:
            print(f"[CLOSED] Port {port}")
