#!/usr/bin/env python3

import subprocess
import socket
import sys
from datetime import datetime

def scan_network(subnet):
    print(f"\n{'='*50}")
    print(f"  SEC-TOOLKIT | Network Scanner")
    print(f"  Subnet : {subnet}")
    print(f"  Time   : {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'='*50}\n")

    alive = []

    for i in range(1, 255):
        ip = f"{subnet}.{i}"
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if result.returncode == 0:
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except:
                hostname = "unknown"
            print(f"  \033[92m[ALIVE]\033[0m {ip:<18} — {hostname}")
            alive.append(ip)

    print(f"\n  Total hosts found: {len(alive)}")
    print(f"{'='*50}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 network_scanner.py <subnet>")
        print("Example: python3 network_scanner.py 192.168.1")
        sys.exit()
    scan_network(sys.argv[1])
