import string
from modules.hash_utils import hash_word

def brute_force(hash_value, algo):
    chars = string.ascii_lowercase + string.digits

    for c1 in chars:
        for c2 in chars:
            attempt = c1 + c2

            if hash_word(attempt, algo) == hash_value:
                print(f"✅ Cracked: {attempt}")
                return attempt

    print("❌ Not found")
