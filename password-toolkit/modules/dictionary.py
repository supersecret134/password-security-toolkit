import os
import re
import itertools

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

    # ✅ ensure folder exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    print("1. Custom Wordlist")
    print("2. rockyou.txt")

    choice = input("Select option: ").strip()

    # =========================
    # ✅ CUSTOM WORDLIST FIXED
    # =========================
    if choice == "1":

        name = input("Enter name: ").strip()
        dob = input("Enter birth year: ").strip()
        keyword = input("Enter keyword: ").strip()

        base_words = [name, keyword]

        numbers = ["", "123", "1234", dob]
        symbols = ["", "!", "@", "#"]

        for word in base_words:
            if not is_clean(word):
                continue

            # basic forms
            wordlist.add(word.lower())
            wordlist.add(word.upper())
            wordlist.add(word.capitalize())

            # combinations
            for num in numbers:
                for sym in symbols:
                    wordlist.add(f"{word}{num}{sym}")
                    wordlist.add(f"{sym}{word}{num}")

        # optional combos
        for combo in itertools.permutations(base_words, 2):
            combined = "".join(combo)
            if is_clean(combined):
                wordlist.add(combined)
                wordlist.add(combined + "123")

    # =========================
    # ROCKYOU
    # =========================
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

    else:
        print("❌ Invalid option")
        return

    # =========================
    # SAVE FILE
    # =========================
    with open(output_file, "w") as f:
        for w in sorted(wordlist):
            f.write(w + "\n")

    print(f"✅ Saved: {output_file}")
    print(f"📊 Total words: {len(wordlist)}")
