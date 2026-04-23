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

    # ensure folder exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    print("1. Custom Wordlist")
    print("2. rockyou.txt")

    choice = input("Select option: ").strip()

    # =========================
    # ✅ CUSTOM WORDLIST
    # =========================
    if choice == "1":

        name = input("Enter name: ").strip()
        dob = input("Enter birth year: ").strip()
        keyword = input("Enter keyword: ").strip()

        # 🔥 NEW: limit control
        limit_input = input("How many entries to generate? (default 1000): ").strip()
        try:
            limit = int(limit_input)
        except:
            limit = 1000

        base_words = [name, keyword]
        numbers = ["", "123", "1234", dob]
        symbols = ["", "!", "@", "#"]

        count = 0

        for word in base_words:
            if not is_clean(word):
                continue

            variations = [
                word.lower(),
                word.upper(),
                word.capitalize()
            ]

            for v in variations:
                if count >= limit:
                    break
                wordlist.add(v)
                count += 1

            for num in numbers:
                for sym in symbols:
                    if count >= limit:
                        break

                    w1 = f"{word}{num}{sym}"
                    w2 = f"{sym}{word}{num}"

                    if is_clean(w1):
                        wordlist.add(w1)
                        count += 1

                    if count >= limit:
                        break

                    if is_clean(w2):
                        wordlist.add(w2)
                        count += 1

                if count >= limit:
                    break

            if count >= limit:
                break

        # 🔥 combinations (controlled)
        for combo in itertools.permutations(base_words, 2):
            if count >= limit:
                break

            combined = "".join(combo)

            if is_clean(combined):
                wordlist.add(combined)
                count += 1

            if count >= limit:
                break

            combo2 = combined + "123"
            if is_clean(combo2):
                wordlist.add(combo2)
                count += 1

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
    print(f"📊 Generated: {len(wordlist)} entries")
