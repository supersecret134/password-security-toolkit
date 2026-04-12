def generate_wordlist():
    base_words = [
        "admin", "password", "test", "user", "root",
        "login", "welcome", "qwerty", "abc123",
        "letmein", "iloveyou", "guest", "manager",
        "hello", "superuser", "pass", "security",
        "access", "master", "dragon", "monkey",
        "football", "sunshine", "princess",
        "shadow", "killer", "hacker", "matrix",
        "python", "linux" , "admin123"
    ]

    variations = set()

    for word in base_words:
        variations.add(word)
        variations.add(word + "123")
        variations.add(word + "1")
        variations.add(word + "2024")
        variations.add(word + "@123")
        variations.add(word + "!")

        variations.add(word.capitalize())
        variations.add(word.upper())

    with open("data/wordlist.txt", "w") as f:
        for w in variations:
            f.write(w + "\n")

    print(f"✅ Wordlist generated with {len(variations)} entries!")
