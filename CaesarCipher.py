def generate_key(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    key = {}

    count = 0
    for c in letters:
        key[c] = letters[(count + n) % len(letters)]
        count += 1

    return key

def get_decryption_key(key):
    dkey = {}

    for c in key:
        dkey[key[c]] = c 

    return dkey

def encrypt(key, message):
    cipher = ""

    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c 

    return cipher 


def run_example():
    key = generate_key(3)
    cipher = encrypt(key, "YOU ARE AWESOME")
    
    decoded_message = encrypt(get_decryption_key(key), cipher)
    print(cipher)
    print(decoded_message)

run_example()

"""
Kerckhoff's Principles of Cryptography

1. The system should be, if not theoretically unbreakable, unbreakable in practice.
2. The design of a system should not require secrecy, and compromise of the system should not inconvenience the correspondents (Kerckhoffs's principle).
3. The key should be memorable without notes and should be easily changeable.
4. The cryptograms should be transmittable by telegraph.
5. The apparatus or documents should be portable and operable by a single person.
6. The system should be easy, neither requiring knowledge of a long list of rules nor involving mental strain.

source(https://en.wikipedia.org/wiki/Auguste_Kerckhoffs)
"""

def attack_encryption():
    key = generate_key(3)
    cipher = encrypt(key, "YOU ARE AWESOME")
    
    for i in range(26):
        message = encrypt(get_decryption_key(generate_key(i)), cipher)
        
        print(message)

        if message == "YOU ARE AWESOME":
            print("Key is generated with value = {n} ".format(n = i))

            return generate_key(i)
    
cracked_key = attack_encryption()

print("Cracked key = {ck}".format(ck = cracked_key))




