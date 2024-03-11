import string
import random

def get_password_length():
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length < 8:
                print("The length of the password must be at least 8 characters.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_password_characters():
    while True:
        choice = input("Include lowercase letters? (y/n): ").lower()
        if choice not in ['y', 'n']:
            print("Invalid input. Please enter 'y' or 'n'.")
        else:
            include_lowercase = choice == 'y'
            break
    while True:
        choice = input("Include uppercase letters? (y/n): ").lower()
        if choice not in ['y', 'n']:
            print("Invalid input. Please enter 'y' or 'n'.")
        else:
            include_uppercase = choice == 'y'
            break
    while True:
        choice = input("Include digits? (y/n): ").lower()
        if choice not in ['y', 'n']:
            print("Invalid input. Please enter 'y' or 'n'.")
        else:
            include_digits = choice == 'y'
            break
    while True:
        choice = input("Include special characters? (y/n): ").lower()
        if choice not in ['y', 'n']:
            print("Invalid input. Please enter 'y' or 'n'.")
        else:
            include_special_chars = choice == 'y'
            break
    characters = string.ascii_letters if include_lowercase else ""
    characters += string.ascii_uppercase if include_uppercase else ""
    characters += string.digits if include_digits else ""
    characters += string.punctuation if include_special_chars else ""
    if not characters:
        print("You must include at least one character type.")
        return get_password_characters()
    return characters

def generate_password(length, characters):
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    password_length = get_password_length()
    password_characters = get_password_characters()
    password = generate_password(password_length, password_characters)
    print("Your generated password is: %s" % password)

if __name__ == "__main__":
    main()
