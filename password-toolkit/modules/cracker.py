from modules.hash_utils import hash_word
import time

def dictionary_attack(hash_value, algo):
    attempts = 0
    start = time.time()

    try:
        with open("data/wordlist.txt") as f:
            for word in f:
                word = word.strip()
                attempts += 1

                if hash_word(word, algo) == hash_value:
                    end = time.time()

                    print(f"\n✅ Cracked: {word}")
                    print(f"Attempts: {attempts}")
                    print(f"Time: {round(end-start,2)}s")

                    return word

        print("❌ Not found")
        return None

    except:
        print("❌ Generate wordlist first!")
