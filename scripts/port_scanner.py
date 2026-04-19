#!/usr/bin/env python3

import socket
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"\033[92m[OPEN]\033[0m Port {port}")
        s.close()
    except:
        pass

def scan(target, start_port, end_port):
    print(f"\n{'='*50}")
    print(f"  SEC-TOOLKIT | FAST Port Scanner")
    print(f"  Target : {target}")
    print(f"  Ports  : {start_port} - {end_port}")
    print(f"  Time   : {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'='*50}\n")

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, target, port)

    print("\nScan complete.\n")
