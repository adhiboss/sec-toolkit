#!/usr/bin/env python3

import re
import sys

def check_password(password):
    print(f"\n{'='*50}")
    print(f"  SEC-TOOLKIT | Password Strength Checker")
    print(f"{'='*50}\n")

    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("  ✗ At least 8 characters required")

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("  ✗ 12+ characters recommended")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("  ✗ Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("  ✗ Add lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("  ✗ Add numbers")

    if re.search(r"[!@#$%^&*()_+]", password):
        score += 1
    else:
        feedback.append("  ✗ Add special characters (!@#$%^&*)")

    levels = {
        0: ("\033[91mVery Weak\033[0m",   "▓░░░░░"),
        1: ("\033[91mWeak\033[0m",         "▓▓░░░░"),
        2: ("\033[93mFair\033[0m",         "▓▓▓░░░"),
        3: ("\033[93mModerate\033[0m",     "▓▓▓▓░░"),
        4: ("\033[92mStrong\033[0m",       "▓▓▓▓▓░"),
        5: ("\033[92mVery Strong\033[0m",  "▓▓▓▓▓▓"),
        6: ("\033[92mExcellent\033[0m",    "▓▓▓▓▓▓"),
    }

    label, bar = levels[score]
    print(f"  Strength : {label}")
    print(f"  Score    : {bar} {score}/6\n")

    if feedback:
        print("  Suggestions:")
        for f in feedback:
            print(f)

    print(f"\n{'='*50}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 password_checker.py <password>")
        sys.exit()
    check_password(sys.argv[1])
