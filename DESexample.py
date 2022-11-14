from pyDes import *


message = "0123456701234567"
key = "DESCRYPT"
iv = bytes([0]*8)
# create the cipher here
key = des(key, CBC, iv, None, PAD_PKCS5) 
cipher = key.encrypt(message)

def modify(cipher):
    mod = [0]*len(cipher)
    mod[9] = 1
    
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])

cipher = modify(cipher)

# Alice sending the encrypted message
# encrypt the message to cipher
print("Length of plain text:", len(message))
print("Length of cipher text:", len(cipher))

# Bob decrypting the cipher text
decrypted_message = key.decrypt(cipher)
# decrypt the cipher to message
print("Original:", message)
print("Decrypted: ", decrypted_message)
