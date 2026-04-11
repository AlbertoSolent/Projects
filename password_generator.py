import random

def generate_password():
    password_lenght = int(input("password lenght: "))
    password = ""

    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
    
    for char in range(password_lenght):
        random_char = random.choice(characters)
        password+=random_char
    
    print(password)


generate_password()