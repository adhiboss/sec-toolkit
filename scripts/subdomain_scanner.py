#!/usr/bin/env python3

# -----------------------------------------------
# sec-toolkit | subdomain_scanner.py
# Discover subdomains of a target domain
# -----------------------------------------------

import socket
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

def scan(subdomain, domain):
    host = f"{subdomain}.{domain}"
    try:
        ip = socket.gethostbyname(host)
        print(f"  \033[92m[FOUND]\033[0m {host:<40} → {ip}")
        return host
    except:
        return None

def main(domain, wordlist):
    print(f"\n{'='*50}")
    print(f"  SEC-TOOLKIT | Subdomain Scanner")
    print(f"  Target : {domain}")
    print(f"  Time   : {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'='*50}\n")

    try:
        with open(wordlist, 'r', errors='ignore') as f:
            subdomains = f.read().splitlines()
    except:
        print(f"  Wordlist not found: {wordlist}")
        sys.exit()

    found = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(lambda s: scan(s, domain), subdomains)
        found = [r for r in results if r]

    print(f"\n  Total found: {len(found)}")
    print(f"  Total scanned: {len(subdomains)}")
    print(f"\n{'='*50}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 subdomain_scanner.py <domain> <wordlist>")
        print("Example: python3 subdomain_scanner.py google.com wordlist.txt")
        sys.exit()
    main(sys.argv[1], sys.argv[2])
