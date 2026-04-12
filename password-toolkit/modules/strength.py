import math

COMMON_PASSWORDS = ["admin", "admin123", "password", "123456", "qwerty"]

def check_strength(password):
    if password.lower() in COMMON_PASSWORDS:
        return "Weak (Common Password)"

    length = len(password)
    charset = 0

    if any(c.islower() for c in password): charset += 26
    if any(c.isupper() for c in password): charset += 26
    if any(c.isdigit() for c in password): charset += 10
    if any(not c.isalnum() for c in password): charset += 32

    entropy = length * math.log2(charset) if charset else 0

    if entropy < 40:
        return "Weak"
    elif entropy < 60:
        return "Medium"
    else:
        return "Strong"
