import random 


def generate_key():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    values = list(letters)
    key = {}
    
    for c in letters:
        key[c] = values.pop(random.randint(0, len(values) - 1))
    
    return key


def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher


key = generate_key()
message = "YOU ARE AWESOME"
cipher = encrypt(key, message)
print(cipher)
