import hashlib

def hash_word(word, algo):
    word = word.strip()

    if algo == "md5":
        return hashlib.md5(word.encode()).hexdigest()

    elif algo == "sha1":
        return hashlib.sha1(word.encode()).hexdigest()

    elif algo == "sha256":
        return hashlib.sha256(word.encode()).hexdigest()

    else:
        return ""
