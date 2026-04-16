import math

COMMON_PASSWORDS = ["admin", "admin123", "password", "123456", "qwerty"]

COMMON_PATTERNS = [
    "123", "1234", "12345",
    "admin", "password", "passwd",
    "qwerty", "abc", "111", "000"
]

def has_common_pattern(password):
    password_lower = password.lower()

    for pattern in COMMON_PATTERNS:
        if pattern in password_lower:
            return True

    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            return True

    return False


def check_strength(password):
    print(f"\nPassword: {password}")

    if password.lower() in COMMON_PASSWORDS:
        print("Strength: Weak")
        print("Reason: Common password\n")
        return "Weak"

    length = len(password)

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    charset = 0
    details = []

    if has_lower:
        charset += 26
        details.append("lowercase")
    if has_upper:
        charset += 26
        details.append("uppercase")
    if has_digit:
        charset += 10
        details.append("digits")
    if has_symbol:
        charset += 32
        details.append("symbols")

    entropy = length * math.log2(charset) if charset else 0

    pattern_flag = has_common_pattern(password)

    # 🔥 FINAL REALISTIC CLASSIFICATION (FIXED INDENTATION)
    if pattern_flag and length < 12:
        strength = "Weak"

    elif pattern_flag:
        strength = "Medium"

    elif length < 8:
        strength = "Weak"

    elif length < 12:
        strength = "Medium"

    elif not (has_lower and has_upper and has_digit and has_symbol):
        strength = "Medium"

    elif entropy < 70:
        strength = "Medium"

    else:
        strength = "Strong"

    # Output
    print(f"Strength: {strength}")
    print(f"Entropy: {entropy:.2f} bits")
    print(f"Length: {length}")
    print(f"Character Set Used: {', '.join(details)}")

    print("\nRecommendations:")

    if length < 12:
        print("- Increase password length (12+ recommended)")
    if not has_lower:
        print("- Add lowercase letters")
    if not has_upper:
        print("- Add uppercase letters")
    if not has_digit:
        print("- Include numbers")
    if not has_symbol:
        print("- Include special characters")
    if pattern_flag:
        print("- Avoid common patterns like 'admin', '12345', 'password'")

    print()
    return strength
