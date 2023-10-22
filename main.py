import string
import random

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length=12):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

if __name__ == '__main__':
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        password_length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers for the number of passwords and password length.")
        exit(1)

    passwords = generate_multiple_passwords(num_passwords, password_length)

    print("Generated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")
