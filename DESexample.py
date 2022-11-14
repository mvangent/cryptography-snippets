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


key1 = bytes([11, 0, 0, 0, 0, 0, 0, 0])
key2 = bytes([56, 0, 0, 0, 0, 0, 0, 0])

doubleDesMessage = "0123456701234567"

k1 = des(key1, ECB, iv, pad=None, padmode=PAD_PKCS5) 
k2 = des(key2, ECB, iv, pad=None, padmode=PAD_PKCS5) 

doubleCipher = k2.encrypt(k1.encrypt(doubleDesMessage))

# Eve's attack on double DES 
lookup = {}

brute_forced_key1 = bytes([])
brute_forced_key2 = bytes([])

for i in range (256):
    key = bytes([i ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)
    lookup[k.encrypt(doubleDesMessage)] = key
   
print(lookup)

for i in range(256):
    key = bytes([i ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)
    
    if k.decrypt(doubleCipher) in lookup:
        brute_forced_key2 = key
        brute_forced_key1 = lookup[k.decrypt(doubleCipher)]
        break
   
print("BK1: ", brute_forced_key1) 
print("BK2: ", brute_forced_key2) 

brute_force_k1 = des(brute_forced_key1, ECB, iv, pad=None, padmode=PAD_PKCS5)
brute_force_k2 = des(brute_forced_key2, ECB, iv, pad=None, padmode=PAD_PKCS5)

brute_force_plain = brute_force_k1.decrypt(brute_force_k2.decrypt(doubleCipher))

print(brute_force_plain)

