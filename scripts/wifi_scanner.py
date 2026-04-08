#!/usr/bin/env python3

# -----------------------------------------------
# sec-toolkit | wifi_scanner.py
# Scan nearby WiFi networks from terminal
# -----------------------------------------------

import subprocess
import sys
from datetime import datetime

def scan():
    print(f"\n{'='*50}")
    print(f"  SEC-TOOLKIT | WiFi Scanner")
    print(f"  Time : {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'='*50}\n")

    try:
        result = subprocess.run(
            ['nmcli', '-f', 'SSID,BSSID,SIGNAL,SECURITY,CHAN', 'dev', 'wifi', 'list'],
            capture_output=True, text=True
        )
        lines = result.stdout.strip().split('\n')
        print(f"  {'SSID':<30} {'SIGNAL':<10} {'SECURITY':<15} {'CHAN'}")
        print(f"  {'-'*65}")
        for line in lines[1:]:
            parts = line.split()
            if parts:
                signal = int(parts[-3]) if parts[-3].isdigit() else 0
                if signal > 70:
                    color = "\033[92m"
                elif signal > 40:
                    color = "\033[93m"
                else:
                    color = "\033[91m"
                print(f"  {color}{line}\033[0m")

    except Exception as e:
        print(f"  \033[91mError: {e}\033[0m")
        print(f"  Make sure nmcli is installed: sudo apt install network-manager")

    print(f"\n{'='*50}\n")

if __name__ == "__main__":
    scan()
