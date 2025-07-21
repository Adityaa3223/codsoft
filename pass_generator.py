import secrets
import string

def generate_password(length: int) -> str:
    """Generate a secure password of given length."""
    if length < 1:
        raise ValueError("Password length must be at least 1")

    # Define character set
    alphabet = string.ascii_letters + string.digits + string.punctuation

    # Generate password using cryptographically secure randomness
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def main():
    try:
        length_input = input("Enter desired password length (e.g. 12): ")
        length = int(length_input)
        if length < 1:
            raise ValueError
    except ValueError:
        print("Invalid input–please enter a positive integer for length.")
        return

    pwd = generate_password(length)
    print(f"🔐  Generated password ({length} chars): {pwd}")

# Corrected line:
if __name__ == "__main__":
    main()
