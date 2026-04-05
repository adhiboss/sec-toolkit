#!/usr/bin/env python3

# -----------------------------------------------
# sec-toolkit | banner_grabber.py
# Grab service banners from open ports
# Reveals software versions running on a server
# -----------------------------------------------

import socket
import sys
from datetime import datetime

PROBES = {
    21:  b"",
    22:  b"",
    25:  b"EHLO test\r\n",
    80:  b"GET / HTTP/1.0\r\n\r\n",
    443: b"GET / HTTP/1.0\r\n\r\n",
    3306: b"",
    5432: b"",
    6379: b"PING\r\n",
    8080: b"GET / HTTP/1.0\r\n\r\n",
}

def grab(host, port):
    try:
        s = socket.socket()
        s.settimeout(3)
        s.connect((host, port))
        probe = PROBES.get(port, b"")
        if probe:
            s.send(probe)
        banner = s.recv(1024).decode(errors='ignore').strip()
        s.close()
        return banner
    except:
        return None

def main(host, ports):
    print(f"\n{'='*50}")
    print(f"  SEC-TOOLKIT | Banner Grabber")
    print(f"  Target : {host}")
    print(f"  Time   : {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'='*50}\n")

    for port in ports:
        banner = grab(host, port)
        if banner:
            print(f"  \033[92m[PORT {port}]\033[0m")
            for line in banner.splitlines()[:3]:
                print(f"  {line}")
            print()
        else:
            print(f"  \033[90m[PORT {port}]\033[0m No banner\n")

    print(f"{'='*50}\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 banner_grabber.py <host> [ports]")
        print("Example: python3 banner_grabber.py scanme.nmap.org 22 80 443")
        sys.exit()

    host = sys.argv[1]
    ports = [int(p) for p in sys.argv[2:]] if len(sys.argv) > 2 else [21,22,25,80,443,3306,8080]
    main(host, ports)
