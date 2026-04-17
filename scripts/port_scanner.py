#!/usr/bin/env python3

import socket
import sys
from datetime import datetime

def scan(target, start_port, end_port):
    print(f"\n{'='*50}")
    print(f"  SEC-TOOLKIT | Port Scanner")
    print(f"  Target : {target}")
    print(f"  Ports  : {start_port} - {end_port}")
    print(f"  Time   : {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'='*50}\n")

    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"  \033[92m[OPEN]\033[0m Port {port}")
                open_ports.append(port)
            s.close()
        except KeyboardInterrupt:
            print("\nScan cancelled.")
            sys.exit()
        except:
            pass

    print(f"\nTotal open ports: {len(open_ports)}")
