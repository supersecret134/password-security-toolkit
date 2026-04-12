from modules.dictionary import generate_wordlist
from modules.cracker import dictionary_attack
from modules.brute_force import brute_force
from modules.strength import check_strength
from modules.report import generate_report

results = []

while True:
    print("\n=== Advanced Credential Toolkit ===")
    print("1. Generate Wordlist")
    print("2. Check Password Strength")
    print("3. Dictionary Attack")
    print("4. Brute Force Attack")
    print("5. Generate Report")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        generate_wordlist()

    elif choice == "2":
        pwd = input("Enter password: ")
        strength = check_strength(pwd)
        print("Strength:", strength)
        results.append(f"{pwd} -> {strength}")

    elif choice == "3":
        hash_val = input("Enter hash: ")
        algo = input("Algorithm (md5/sha1/sha256): ")
        cracked = dictionary_attack(hash_val, algo)
        if cracked:
            results.append(f"Cracked: {cracked}")

    elif choice == "4":
        hash_val = input("Enter hash: ")
        algo = input("Algorithm: ")
        brute_force(hash_val, algo)

    elif choice == "5":
        generate_report(results)

    elif choice == "6":
        break
