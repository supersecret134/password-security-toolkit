import hashlib
import string
import itertools


def hash_func(password, algo):
    password = password.encode()

    if algo == "md5":
        return hashlib.md5(password).hexdigest()
    elif algo == "sha1":
        return hashlib.sha1(password).hexdigest()
    elif algo == "sha256":
        return hashlib.sha256(password).hexdigest()
    return None


def brute_force(hash_value, algo="md5"):
    print("\n⚡ Starting Brute Force Attack...\n")

    hash_value = hash_value.strip().lower()

    # =========================
    # USER INPUT
    # =========================
    try:
        max_length = int(input("Enter max password length (e.g. 4): "))
    except:
        max_length = 4

    # 🔥 FULL CHARSET (FIXED)
    chars = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    # =========================
    # TIME ESTIMATION
    # =========================
    charset_size = len(chars)
    total_combinations = sum(charset_size ** i for i in range(1, max_length + 1))

    attempts_per_sec = 1_000_000  # simulated
    estimated_time = total_combinations / attempts_per_sec

    print(f"🧠 Total combinations: {total_combinations}")
    print(f"⏱ Estimated time: {round(estimated_time, 2)} seconds\n")

    # =========================
    # COMMON PASSWORDS
    # =========================
    common = [
        "admin", "password", "123456", "12345678",
        "admin123", "root", "toor", "test",
        "guest", "user", "1234", "12345",
        "qwerty", "abc123", "letmein"
    ]

    for p in common:
        if hash_func(p, algo) == hash_value:
            print(f"✅ Found in common list: {p}")
            return p

    # =========================
    # NUMERIC BRUTE FORCE
    # =========================
    for i in range(1000000):
        p = f"{i:06d}"
        if hash_func(p, algo) == hash_value:
            print(f"✅ Found numeric password: {p}")
            return p

    # =========================
    # INCREMENTAL BRUTE FORCE
    # =========================
    for length in range(1, max_length + 1):
        print(f"🔍 Trying length: {length}")

        for attempt in itertools.product(chars, repeat=length):
            p = "".join(attempt)

            if hash_func(p, algo) == hash_value:
                print(f"✅ Found brute force password: {p}")
                return p

    print("❌ Password not found in brute force range")
    return None
