import random
import string

def generate_password(length):
    if length < 1:
        return "Error: Password length must be at least 1."

    # Define character sets for the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            print("Error: Password length must be at least 1.")
            return
        
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError:
        print("Error: Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
