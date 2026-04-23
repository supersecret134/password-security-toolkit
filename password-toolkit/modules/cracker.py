import os
import time
from modules.hash_utils import hash_word

def dictionary_attack(hash_value, algo):
    attempts = 0
    start = time.time()

    # ✅ FIXED: stable project root path
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    wordlist_path = os.path.join(BASE_DIR, "data", "wordlist.txt")

    hash_value = hash_value.strip().lower()

    print("\n⚡ Starting Dictionary Attack...\n")
    print(f"📂 Wordlist: {wordlist_path}\n")

    if not os.path.exists(wordlist_path):
        print("❌ Wordlist not found.")
        return None

    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:

        for word in f:
            word = word.strip()

            if not word:
                continue

            attempts += 1

            hashed = hash_word(word, algo)

            if not hashed:
                continue

            hashed = hashed.strip().lower()

            if hashed == hash_value:
                print("\n\n=================================")
                print("✅ PASSWORD FOUND")
                print(f"Password : {word}")
                print(f"Attempts : {attempts}")
                print(f"Time     : {round(time.time() - start, 2)} sec")
                print("=================================\n")
                return word

            if attempts % 5000 == 0:
                print(f"Trying [{attempts}] {word[:30]}", end="\r")

    print("\n❌ Not found in dictionary attack")
    return None
