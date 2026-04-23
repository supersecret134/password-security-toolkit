import os

def detect_hash_type(hash_value):
    if hash_value.startswith("$y$"):
        return "Yescrypt (modern Linux)"
    elif hash_value.startswith("$6$"):
        return "SHA-512 (Linux)"
    elif hash_value.startswith("$5$"):
        return "SHA-256 (Linux)"
    elif hash_value.startswith("$2y$") or hash_value.startswith("$2b$"):
        return "bcrypt"
    elif hash_value.startswith("$1$"):
        return "MD5 crypt"
    elif hash_value in ["*", "!", "!!", ""]:
        return "Disabled / Locked account"

    # 🔥 NEW: length-based detection
    elif len(hash_value) == 32:
        return "MD5 / NTLM"
    elif len(hash_value) == 40:
        return "SHA1"
    elif len(hash_value) == 64:
        return "SHA256"
    else:
        return "Unknown"


def extract_hashes():
    print("\n=== Hash Extraction Module ===")
    print("⚠️ Educational / demo use only")
    print("🔍 Auto-detecting hash file...\n")

    # 🔥 Added Windows simulation paths
    possible_paths = [
        "/etc/shadow",                  # Linux
        "/etc/passwd",
        "data/hashes.txt",              # Custom file
        "hashes.txt",
        "data/windows_hashes.txt"       # Simulated Windows hashes
    ]

    file_path = None

    for path in possible_paths:
        if os.path.exists(path):
            file_path = path
            break

    if not file_path:
        print("❌ No hash file found.")
        print("👉 Place file in 'data/hashes.txt' or 'data/windows_hashes.txt'")
        print("👉 Linux shadow requires sudo\n")
        return []

    print(f"📂 Using file: {file_path}\n")

    extracted = []

    try:
        with open(file_path, "r") as f:
            lines = f.readlines()

        print("📂 Extracted Hashes:\n")

        for line in lines:
            line = line.strip()

            if ":" not in line:
                continue

            parts = line.split(":")

            username = parts[0]
            hash_value = parts[1] if len(parts) > 1 else ""

            algo = detect_hash_type(hash_value)

            extracted.append({
                "user": username,
                "hash": hash_value,
                "type": algo
            })

            print(f"👤 User : {username}")
            print(f"🔑 Hash : {hash_value}")
            print(f"🧠 Type : {algo}\n")

        print("✅ Hash extraction completed!\n")
        return extracted

    except PermissionError:
        print("❌ Permission denied for /etc/shadow (run as sudo)\n")
        return []

    except Exception as e:
        print(f"❌ Error: {e}\n")
        return []
