import random
import string

def password_generator(length, use_numbers, use_special):
    characters = string.ascii_letters  # a-zA-Z
    
    if use_numbers:
        characters += string.digits  # 0-9
        
    if use_special:
        characters += string.punctuation  # special characters

    password = ""   # initialize password
    
    while len(password) < length:
        password += random.choice(characters)
    
    return password


# --- User Input Section ---
while True:
    user_input = input("Type 'generate' to create a password: ")
    
    if user_input.lower() == "generate":
        length = int(input("Enter password length: "))
        use_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
        use_special = input("Include special characters? (yes/no): ").lower() == "yes"
        
        print("Generated Password:", password_generator(length, use_numbers, use_special))
        break
    else:
        print("Invalid input. Please type 'generate'.")