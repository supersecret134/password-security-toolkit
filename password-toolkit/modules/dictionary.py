def generate_wordlist():
    words = ["admin", "password", "test", "user", "admin123"]

    with open("data/wordlist.txt", "w") as f:
        for w in words:
            f.write(w + "\n")

    print("✅ Wordlist generated!")
