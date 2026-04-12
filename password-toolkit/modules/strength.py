import math

COMMON_PASSWORDS = ["admin", "admin123", "password", "123456", "qwerty"]

def check_strength(password):
    print(f"\nPassword: {password}")

    if password.lower() in COMMON_PASSWORDS:
        print("Strength: Weak")
        print("Reason: Common password\n")
        return "Weak"

    length = len(password)
    charset = 0
    details = []

    if any(c.islower() for c in password):
        charset += 26
        details.append("lowercase")
    if any(c.isupper() for c in password):
        charset += 26
        details.append("uppercase")
    if any(c.isdigit() for c in password):
        charset += 10
        details.append("digits")
    if any(not c.isalnum() for c in password):
        charset += 32
        details.append("symbols")

    entropy = length * math.log2(charset) if charset else 0

    # Strength classification
    if entropy < 40:
        strength = "Weak"
    elif entropy < 60:
        strength = "Medium"
    else:
        strength = "Strong"

    print(f"Strength: {strength}")
    print(f"Entropy: {entropy:.2f} bits")
    print(f"Length: {length}")
    print(f"Character Set Used: {', '.join(details)}")

    print("\nRecommendations:")
    if length < 12:
        print("- Increase password length (12+ recommended)")
    if "uppercase" not in details:
        print("- Add uppercase letters")
    if "digits" not in details:
        print("- Include numbers")
    if "symbols" not in details:
        print("- Include special characters")

    print()
    return strength
