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
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"
                print(f"  \033[92m[OPEN]\033[0m Port {port:>5} — {service}")
                open_ports.append(port)
            s.close()
        except KeyboardInterrupt:
            print("\n  Scan cancelled.")
            sys.exit()
        except:
            pass

    print(f"\n  Total open ports: {len(open_ports)}")
    print(f"{'='*50}\n")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 port_scanner.py <target> <start_port> <end_port>")
        print("Example: python3 port_scanner.py 127.0.0.1 1 1024")
        sys.exit()

    target = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])
    scan(target, start, end)
