import hashlib
import string
import itertools
import time


def hash_func(password, algo):
    if algo == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    elif algo == "sha1":
        return hashlib.sha1(password.encode()).hexdigest()
    elif algo == "sha256":
        return hashlib.sha256(password.encode()).hexdigest()
    else:
        return None


def brute_force(hash_value, algo="md5"):
    print("\n⚡ Starting Brute Force Attack...\n")
    start_time = time.time()
    attempts = 0

    # =========================
    # 1. COMMON PASSWORDS
    # =========================
    common = [
        "admin", "password", "123456", "12345678",
        "admin123", "root", "toor", "test",
        "guest", "user", "1234", "12345",
        "qwerty", "abc123", "letmein"
    ]

    for p in common:
        attempts += 1
        if hash_func(p, algo) == hash_value:
            print(f"✅ Found in common list: {p}")
            print_stats(attempts, start_time)
            return p

    # =========================
    # 2. SMALL CHARSET (SMART)
    # =========================
    chars = string.ascii_lowercase

    for length in range(1, 4):
        for attempt in itertools.product(chars, repeat=length):
            attempts += 1
            p = "".join(attempt)

            if attempts % 50000 == 0:
                print(f"⏳ Attempts: {attempts}")

            if hash_func(p, algo) == hash_value:
                print(f"✅ Found brute password: {p}")
                print_stats(attempts, start_time)
                return p

    # =========================
    # 3. NUMERIC BRUTE FORCE
    # =========================
    for i in range(1000000):
        attempts += 1
        p = f"{i:06d}"

        if attempts % 100000 == 0:
            print(f"⏳ Attempts: {attempts}")

        if hash_func(p, algo) == hash_value:
            print(f"✅ Found numeric password: {p}")
            print_stats(attempts, start_time)
            return p

    print("❌ Password not found in brute force range")
    print_stats(attempts, start_time)
    return None


def print_stats(attempts, start_time):
    duration = time.time() - start_time
    print("\n📊 Attack Stats:")
    print(f"Total Attempts : {attempts}")
    print(f"Time Taken     : {duration:.2f} seconds")
