import os

def generate_wordlist():
    print("\n=== Smart Wordlist Generator ===")

    wordlist = set()

    print("1. Custom Smart Wordlist (target-based)")
    print("2. Use rockyou.txt (stream mode)")

    choice = input("Select option: ").strip()

    output_file = "data/wordlist.txt"

    # =========================
    # OPTION 1: SMART WORDLIST
    # =========================
    if choice == "1":

        name = input("Enter name (optional): ").strip().lower()
        year = input("Enter year (optional): ").strip()
        custom = input("Enter custom word (optional): ").strip().lower()

        base_words = [
            "admin", "password", "user", "root",
            "login", "welcome", "qwerty",
            "abc123", "letmein", "iloveyou",
            "guest", "manager", "hello",
            "dragon", "monkey", "football"
        ]

        if name:
            base_words.append(name)
        if custom:
            base_words.append(custom)

        suffixes = ["123", "1234", "@123", "!", "@", "#"]
        years = [year] if year else ["2023", "2024", "2025"]

        for word in base_words:
            wordlist.add(word)
            wordlist.add(word.capitalize())
            wordlist.add(word.upper())
            wordlist.add(word[::-1])

            for suf in suffixes:
                wordlist.add(word + suf)

            for y in years:
                wordlist.add(word + y)

            for suf in suffixes:
                for y in years:
                    wordlist.add(word + suf + y)
                    wordlist.add(word + y + suf)

            if name:
                wordlist.add(name + word)
                wordlist.add(word + name)

            if name and year:
                wordlist.add(name + year)
                wordlist.add(name + "@" + year)

    # =========================
    # OPTION 2: ROCKYOU (FIXED STREAM MODE)
    # =========================
    elif choice == "2":

        rockyou_path = "/usr/share/wordlists/rockyou.txt"

        if not os.path.exists(rockyou_path):
            print("❌ rockyou.txt not found!")
            return

        print(f"\n📂 Using rockyou.txt (STREAM MODE)")
        print("⚠️ No full memory load (optimized)\n")

        with open(rockyou_path, "r", errors="ignore") as f, open(output_file, "w") as out:

            count = 0

            for line in f:
                word = line.strip()

                if not word:
                    continue

                out.write(word + "\n")
                count += 1

        print(f"\n✅ Wordlist generated from rockyou (stream mode)")
        print(f"📁 Saved to: {output_file}")

        return

    else:
        print("❌ Invalid option")
        return

    # =========================
    # SAVE SMART WORDLIST
    # =========================
    with open(output_file, "w") as f:
        for word in sorted(wordlist):
            f.write(word + "\n")

    print(f"\n✅ Smart wordlist generated with {len(wordlist)} entries!")
    print(f"📁 Saved to: {output_file}\n")
