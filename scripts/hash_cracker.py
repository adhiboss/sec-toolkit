#!/usr/bin/env python3

# -----------------------------------------------
# sec-toolkit | hash_cracker.py
# Crack MD5/SHA1/SHA256 hashes using wordlist
# -----------------------------------------------

import hashlib
import sys
import os

def crack(hash_input, hash_type, wordlist):
    if not os.path.exists(wordlist):
        print(f"  Wordlist not found: {wordlist}")
        return

    print(f"\n{'='*50}")
    print(f"  SEC-TOOLKIT | Hash Cracker")
    print(f"  Hash : {hash_input}")
    print(f"  Type : {hash_type}")
    print(f"{'='*50}\n")

    count = 0
    with open(wordlist, 'r', errors='ignore') as f:
        for word in f:
            word = word.strip()
            count += 1

            if hash_type == 'md5':
                hashed = hashlib.md5(word.encode()).hexdigest()
            elif hash_type == 'sha1':
                hashed = hashlib.sha1(word.encode()).hexdigest()
            elif hash_type == 'sha256':
                hashed = hashlib.sha256(word.encode()).hexdigest()
            else:
                print("  Unsupported hash type. Use md5/sha1/sha256")
                return

            if hashed == hash_input:
                print(f"  \033[92m[CRACKED]\033[0m Password: {word}")
                print(f"  Tried {count} words")
                print(f"\n{'='*50}\n")
                return

            if count % 1000 == 0:
                print(f"  Trying... {count} words checked", end='\r')

    print(f"\n  \033[91m[FAILED]\033[0m Hash not cracked after {count} attempts")
    print(f"\n{'='*50}\n")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 hash_cracker.py <hash> <type> <wordlist>")
        print("Example: python3 hash_cracker.py 5f4dcc3b5aa765d61d8327deb882cf99 md5 wordlist.txt")
        sys.exit()
    crack(sys.argv[1], sys.argv[2], sys.argv[3])
