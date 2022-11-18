import hashlib

# These are Alice's RSA Keys
n = 170171
e = 5
d = 9677

message = "Bob you are awesome".encode()

#Step 1: Hash the message
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
h = int.from_bytes(h, "big") % n
print("Hash value -> ", h)

signed = (h**d) % n

print("Alice -> Bob", "Message: ", message, "Signature: ", signed)

# Eve's evil interception
def modify(m):
    l = list(m)
    l[0] = l[0] ^ 1 
    return bytes(l)

message = modify(message)

# Bob verifying it is really Alice
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
h = int.from_bytes(h, "big") % n

print("Bob's hash ", h, "signature verification ", (signed**e) % n)
print("Its alice -> ", ((signed**e) % n) == h)


