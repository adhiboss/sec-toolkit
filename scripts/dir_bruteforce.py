#!/usr/bin/env python3

# -----------------------------------------------
# sec-toolkit | dir_bruteforce.py
# Brute force directories on a web server
# -----------------------------------------------

import requests
import sys
from datetime import datetime

def bruteforce(url, wordlist):
    print(f"\n{'='*50}")
    print(f"  SEC-TOOLKIT | Directory Bruteforcer")
    print(f"  Target : {url}")
    print(f"  Time   : {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'='*50}\n")

    found = []
    count = 0

    try:
        with open(wordlist, 'r', errors='ignore') as f:
            dirs = f.read().splitlines()
    except:
        print(f"  Wordlist not found: {wordlist}")
        sys.exit()

    for d in dirs:
        target = f"{url.rstrip('/')}/{d.strip()}"
        count += 1
        try:
            res = requests.get(target, timeout=3)
            if res.status_code == 200:
                print(f"  \033[92m[FOUND 200]\033[0m {target}")
                found.append(target)
            elif res.status_code == 301 or res.status_code == 302:
                print(f"  \033[93m[REDIRECT {res.status_code}]\033[0m {target}")
                found.append(target)
            elif res.status_code == 403:
                print(f"  \033[91m[FORBIDDEN 403]\033[0m {target}")
        except:
            pass

        if count % 50 == 0:
            print(f"  Scanning... {count} paths checked", end='\r')

    print(f"\n\n  Total found: {len(found)}")
    print(f"  Total scanned: {count}")
    print(f"\n{'='*50}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 dir_bruteforce.py <url> <wordlist>")
        print("Example: python3 dir_bruteforce.py http://localhost wordlist.txt")
        sys.exit()
    bruteforce(sys.argv[1], sys.argv[2])
