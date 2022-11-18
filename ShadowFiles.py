import hashlib
import base64

iterations = 454454
salt = base64.b64encode("VERY_SALTY_SALT=".encode())

password = "A Very SECURE PASSWORD".encode()

hashed_pw = hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128)
hashed_pw = base64.b64encode(hashed_pw)

print(hashed_pw)
