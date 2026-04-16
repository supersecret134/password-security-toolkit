from modules.dictionary import generate_wordlist
from modules.cracker import dictionary_attack
from modules.brute_force import brute_force
from modules.strength import check_strength
from modules.report import generate_report
from modules.hash_extractor import extract_hashes

results = []

while True:
    print("\n=== Advanced Credential Toolkit ===")
    print("1. Generate Wordlist")
    print("2. Check Password Strength")
    print("3. Dictionary Attack")
    print("4. Brute Force Attack")
    print("5. Hash Extraction (Linux/Windows)")
    print("6. Generate Report")
    print("7. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        generate_wordlist()

    elif choice == "2":
        pwd = input("Enter password: ").strip()
        strength = check_strength(pwd)
        results.append(f"Password Check: {pwd} -> {strength}")

    elif choice == "3":
        hash_val = input("Enter hash: ").strip()
        algo = input("Algorithm (md5/sha1/sha256): ").lower().strip()

        cracked = dictionary_attack(hash_val, algo)

        if cracked:
            print(f"✅ Password found: {cracked}")
            results.append(f"Dictionary Attack: SUCCESS (Password: {cracked})")
        else:
            print("❌ Password not found")
            results.append("Dictionary Attack: FAILED")

    elif choice == "4":
        hash_val = input("Enter hash: ").strip()
        algo = input("Algorithm (md5/sha1/sha256): ").lower().strip()

        cracked = brute_force(hash_val, algo)

        if cracked:
            print(f"✅ Password found: {cracked}")
            results.append(f"Brute Force: SUCCESS (Password: {cracked})")
        else:
            print("❌ Password not found")
            results.append("Brute Force: FAILED")

    elif choice == "5":
        extract_hashes()
        results.append("Hash Extraction: Completed")

    elif choice == "6":
        if not results:
            print("⚠️ No data to generate report.")
        else:
            generate_report(results)
            print("📄 Report generated successfully!")

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
