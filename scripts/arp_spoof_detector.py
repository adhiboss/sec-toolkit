#!/usr/bin/env python3

# -----------------------------------------------
# sec-toolkit | arp_spoof_detector.py
# Detect ARP spoofing attacks on your network
# -----------------------------------------------

import subprocess
import sys
import time
from datetime import datetime

def get_arp_table():
    result = subprocess.run(['arp', '-n'], capture_output=True, text=True)
    table = {}
    for line in result.stdout.strip().split('\n')[1:]:
        parts = line.split()
        if len(parts) >= 3 and parts[2] != '<incomplete>':
            ip = parts[0]
            mac = parts[2]
            if mac in table:
                table[mac].append(ip)
            else:
                table[mac] = [ip]
    return table

def detect():
    print(f"\n{'='*50}")
    print(f"  SEC-TOOLKIT | ARP Spoof Detector")
    print(f"  Time : {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'='*50}\n")

    print(f"  Monitoring ARP table — Ctrl+C to stop\n")

    try:
        while True:
            table = get_arp_table()
            spoofed = False

            for mac, ips in table.items():
                if len(ips) > 1:
                    spoofed = True
                    print(f"  \033[91m[ALERT] ARP SPOOFING DETECTED!\033[0m")
                    print(f"  MAC {mac} has multiple IPs:")
                    for ip in ips:
                        print(f"    → {ip}")
                    print()

            if not spoofed:
                print(f"  \033[92m[SAFE]\033[0m No ARP spoofing detected — {datetime.now().strftime('%H:%M:%S')}", end='\r')

            time.sleep(5)

    except KeyboardInterrupt:
        print(f"\n\n  Monitoring stopped.\n{'='*50}\n")

if __name__ == "__main__":
    detect()
