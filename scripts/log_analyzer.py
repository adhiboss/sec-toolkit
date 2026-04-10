#!/usr/bin/env python3

# -----------------------------------------------
# sec-toolkit | log_analyzer.py
# Analyze system logs for suspicious activity
# -----------------------------------------------

import sys
import os
from datetime import datetime
from collections import Counter

def analyze(logfile):
    print(f"\n{'='*50}")
    print(f"  SEC-TOOLKIT | Log Analyzer")
    print(f"  File : {logfile}")
    print(f"  Time : {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'='*50}\n")

    if not os.path.exists(logfile):
        print(f"  \033[91mFile not found: {logfile}\033[0m")
        sys.exit()

    failed_logins = []
    successful_logins = []
    suspicious_ips = []
    sudo_attempts = []
    errors = []

    with open(logfile, 'r', errors='ignore') as f:
        for line in f:
            if 'Failed password' in line:
                failed_logins.append(line.strip())
                ip = [x for x in line.split() if x.count('.') == 3]
                if ip:
                    suspicious_ips.append(ip[0])
            elif 'Accepted password' in line or 'Accepted publickey' in line:
                successful_logins.append(line.strip())
            elif 'sudo' in line.lower():
                sudo_attempts.append(line.strip())
            elif 'error' in line.lower() or 'fail' in line.lower():
                errors.append(line.strip())

    print(f"  \033[92m[1] Successful Logins: {len(successful_logins)}\033[0m")
    for l in successful_logins[-5:]:
        print(f"      {l[:80]}")
    print()

    print(f"  \033[91m[2] Failed Logins: {len(failed_logins)}\033[0m")
    for l in failed_logins[-5:]:
        print(f"      {l[:80]}")
    print()

    print(f"  \033[93m[3] Top Suspicious IPs:\033[0m")
    for ip, count in Counter(suspicious_ips).most_common(5):
        print(f"      {ip:<20} — {count} attempts")
    print()

    print(f"  \033[93m[4] Sudo Attempts: {len(sudo_attempts)}\033[0m")
    for l in sudo_attempts[-5:]:
        print(f"      {l[:80]}")
    print()

    print(f"  \033[91m[5] Errors Found: {len(errors)}\033[0m")
    for l in errors[-5:]:
        print(f"      {l[:80]}")

    print(f"\n{'='*50}\n")

if __name__ == "__main__":
    logfile = sys.argv[1] if len(sys.argv) > 1 else "/var/log/auth.log"
    analyze(logfile)
