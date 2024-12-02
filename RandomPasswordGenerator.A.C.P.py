import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols),
    ]

    all_characters = lower + upper + digits + symbols
    while len(password) < length:
        password.append(random.choice(all_characters))

    random.shuffle(password)
    return ''.join(password)

password_length = int(input("Enter the desired password length (minimum 4): "))
password = generate_password(password_length)
print("Generated Password:", password)
