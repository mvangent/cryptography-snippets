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

def get_decryption_key(key):
    dkey = {}

    for c in key:
        dkey[key[c]] = c 

    return dkey

def decrypt(key, cipher):
    decryption_key = get_decryption_key(key)
    
    decoded_message = ''
    for c in cipher:
        if c in key:
            decoded_message += decryption_key[c]
        else:
            decoded_message += c
    
    return decoded_message

key = generate_key()
message = "YOU ARE AWESOME"
cipher = encrypt(key, message)
print(cipher)

print(decrypt(key, cipher))


