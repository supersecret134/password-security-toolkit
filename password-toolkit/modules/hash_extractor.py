def extract_hashes():
    print("\n=== Hash Extraction Module ===")
    print("⚠️ For educational/demo use only\n")

    file_path = input("Enter path to hash file: ").strip()

    try:
        with open(file_path, "r") as f:
            lines = f.readlines()

        print("\n📂 Extracted Hashes:\n")

        for line in lines:
            line = line.strip()

            if ":" in line:
                parts = line.split(":")

                username = parts[0]
                hash_value = parts[1]

                # Basic hash detection
                if hash_value.startswith("$6$"):
                    algo = "SHA-512 (Linux)"
                elif hash_value.startswith("$5$"):
                    algo = "SHA-256 (Linux)"
                elif len(hash_value) == 32:
                    algo = "MD5 / NTLM (Windows)"
                else:
                    algo = "Unknown"

                print(f"User : {username}")
                print(f"Hash : {hash_value}")
                print(f"Type : {algo}\n")

            else:
                print(f"Raw Hash: {line}")

        print("✅ Hash extraction completed!\n")

    except FileNotFoundError:
        print("❌ File not found. Please check the path.\n")
