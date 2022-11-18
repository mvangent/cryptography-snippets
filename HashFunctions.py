import hashlib

m = "This is the hash value message".encode()

sha256 = hashlib.sha256()
sha256.update(m)
d = sha256.digest()
print(d)

def modify(m):
    l = list(m)
    l[0] = l[0] ^ 1

    return bytes(l)

sha256 = hashlib.sha256()
sha256.update(modify(m))
d = sha256.digest()
print(d)

