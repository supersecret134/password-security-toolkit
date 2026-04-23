import os
import re

def is_clean(word):
    if not word:
        return False

    word = word.strip()

    if len(word) < 3 or len(word) > 25:
        return False

    if re.search(r"[^\x20-\x7E]", word):
        return False

    return True


def generate_wordlist():
    print("\n=== Smart Wordlist Generator ===\n")

    wordlist = set()

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    output_file = os.path.join(BASE_DIR, "data", "wordlist.txt")

    print("1. Custom Wordlist")
    print("2. rockyou.txt")

    choice = input("Select option: ").strip()

    if choice == "1":

        base_words = ["admin", "password", "user", "root"]

        for word in base_words:
            if is_clean(word):
                wordlist.add(word)

    elif choice == "2":

        rockyou_path = "/usr/share/wordlists/rockyou.txt"

        if not os.path.exists(rockyou_path):
            print("❌ rockyou not found")
            return

        with open(rockyou_path, "r", errors="ignore") as f, open(output_file, "w") as out:

            for line in f:
                word = line.strip()

                if is_clean(word):
                    out.write(word + "\n")

        print("✅ Wordlist created:", output_file)
        return

    with open(output_file, "w") as f:
        for w in sorted(wordlist):
            f.write(w + "\n")

    print("✅ Saved:", output_file)
