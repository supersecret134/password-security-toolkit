from modules.hash_utils import hash_word
import time
import os

def dictionary_attack(hash_value, algo):
    attempts = 0
    start = time.time()

    wordlist_path = "data/wordlist.txt"

    # =========================
    # FILE CHECK (IMPORTANT FIX)
    # =========================
    if not os.path.exists(wordlist_path):
        print("❌ Wordlist not found. Generate it first.")
        return None

    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:

            for word in f:
                word = word.strip()
                if not word:
                    continue

                attempts += 1

                # =========================
                # HASH CHECK
                # =========================
                if hash_word(word, algo) == hash_value:

                    end = time.time()

                    print(f"\n✅ Cracked: {word}")
                    print(f"Attempts: {attempts}")
                    print(f"Time: {round(end - start, 2)}s")

                    return word

        # =========================
        # NOT FOUND
        # =========================
        print("❌ Not found in dictionary attack")
        return None

    except Exception as e:
        print(f"❌ Error: {e}")
        return None
