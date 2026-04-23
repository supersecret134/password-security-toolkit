import os
import time
from colorama import Fore, Style, init

from modules.dictionary import generate_wordlist
from modules.cracker import dictionary_attack
from modules.brute_force import brute_force
from modules.strength import check_strength
from modules.report import generate_report
from modules.hash_extractor import extract_hashes

init(autoreset=True)

results = []

# -------------------- UI --------------------

def banner():
    print(Fore.CYAN + "=" * 60)
    print(Fore.YELLOW + "   🔐 ADVANCED CYBERSECURITY TOOLKIT 🔐")
    print(Fore.CYAN + "   Password Security | VAPT Simulation | Learning Lab")
    print(Fore.CYAN + "=" * 60 + "\n")


def menu():
    print(Fore.GREEN + "📌 SELECT AN OPTION:\n")
    print("[1] Generate Wordlist")
    print("[2] Check Password Strength")
    print("[3] Dictionary Attack")
    print("[4] Brute Force Attack")
    print("[5] Hash Extraction (Linux/Windows)")
    print("[6] Generate Security Report")
    print("[7] Exit\n")


def pause():
    input(Fore.MAGENTA + "\nPress Enter to continue...")


# -------------------- START --------------------

os.system("cls" if os.name == "nt" else "clear")
banner()

while True:

    menu()
    choice = input(Fore.WHITE + "Enter choice: ").strip()

    # ---------------- WORDLIST ----------------
    if choice == "1":
        print(Fore.BLUE + "\n📂 Generating Wordlist...\n")
        generate_wordlist()
        results.append("Wordlist generated successfully")
        print(Fore.GREEN + "✅ Done")

    # ---------------- PASSWORD STRENGTH ----------------
    elif choice == "2":
        pwd = input("Enter password: ").strip()
        strength = check_strength(pwd)
        results.append(f"Password Check: {strength}")
        print(Fore.YELLOW + f"\n🔎 Result: {strength}")

    # ---------------- DICTIONARY ATTACK ----------------
    elif choice == "3":
        hash_val = input("Enter hash: ").strip()
        algo = input("Algorithm (md5/sha1/sha256): ").lower().strip()

        print(Fore.BLUE + "\n⚡ Running Dictionary Attack...\n")

        cracked = dictionary_attack(hash_val, algo)

        if cracked:
            print(Fore.GREEN + f"\n✅ Password found: {cracked}")
            results.append(f"Dictionary Attack SUCCESS → {cracked}")
        else:
            print(Fore.RED + "\n❌ Password not found")
            results.append("Dictionary Attack FAILED")

    # ---------------- BRUTE FORCE ----------------
    elif choice == "4":
        hash_val = input("Enter hash: ").strip()
        algo = input("Algorithm (md5/sha1/sha256): ").lower().strip()

        print(Fore.BLUE + "\n⚡ Running Brute Force Attack...\n")

        cracked = brute_force(hash_val, algo)

        if cracked:
            print(Fore.GREEN + f"\n✅ Password found: {cracked}")
            results.append(f"Brute Force SUCCESS → {cracked}")
        else:
            print(Fore.RED + "\n❌ Password not found")
            results.append("Brute Force FAILED")

    # ---------------- HASH EXTRACTION ----------------
    elif choice == "5":
        print(Fore.BLUE + "\n🔍 Extracting hashes...\n")
        extract_hashes()
        results.append("Hash Extraction Completed")
        print(Fore.GREEN + "✅ Done")

    # ---------------- REPORT ----------------
    elif choice == "6":
        if not results:
            print(Fore.YELLOW + "⚠️ No data available.")
        else:
            print(Fore.BLUE + "\n📄 Generating Report...\n")
            generate_report(results)

            print(Fore.CYAN + "\n" + "=" * 50)
            print(Fore.YELLOW + "📄 SECURITY REPORT")
            print(Fore.CYAN + "=" * 50)

            for r in results:
                print(Fore.WHITE + "• " + r)

            print(Fore.CYAN + "=" * 50)
            print(Fore.GREEN + "\n✅ Report ready!")

    # ---------------- EXIT ----------------
    elif choice == "7":
        print(Fore.YELLOW + "\nExiting... Stay ethical 🔐")
        break

    else:
        print(Fore.RED + "❌ Invalid choice")

    pause()
    print("\n")
