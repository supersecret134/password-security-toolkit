import hashlib
import string
import itertools

def hash_func(password, algo):
    if algo == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    return None


def brute_force(hash_value, algo="md5"):
    # 1. Common passwords (fast)
    common = [
        "admin", "password", "123456", "12345678",
        "admin123", "root", "toor", "test",
        "guest", "user", "1234", "12345",
        "qwerty", "abc123", "letmein"
    ]

    for p in common:
        if hash_func(p, algo) == hash_value:
            return p

    # 2. Numeric (VERY fast)
    for i in range(1000000):  # 000000–999999
        p = f"{i:06d}"
        if hash_func(p, algo) == hash_value:
            return p

    # 3. Short brute force (limit to 3 chars for speed)
    chars = string.ascii_lowercase + string.digits

    for length in range(1, 4):  # ONLY 1–3 (fast)
        for attempt in itertools.product(chars, repeat=length):
            p = "".join(attempt)
            if hash_func(p, algo) == hash_value:
                return p

    return None
