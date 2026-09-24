import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    print("===== PASSWORD GENERATOR =====")

    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Password length must be greater than 0.")
            return

        password = generate_password(length)

        print(f"Generated Password: {password}")

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
