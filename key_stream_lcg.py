class KeyStream:
    def __init__(self, key=1):
        self.next = key

    def rand(self):
        # LCG: https://en.wikipedia.org/wiki/Linear_congruential_generator
        a = 1103515245
        b = 12345
        m = 2**31
        
        self.next = (a * self.next + b) % m
        
        return self.next

    def get_key_byte(self):
        return self.rand() % 256
        


def encrypt(key, message):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])

# In the transmit function flip the 6th least significant bit of the 4th byte.
def transmit(cipher):
    b = []
    
    for i in range(len(cipher)):
        c = cipher[i]
        if i == 3:
            c = c ^ 2**5
        
        b.append(c)
    
    return bytes(b)

def tamper(cipher):
    modified = [0] * len(cipher)

    modified[10] = ord(' ') ^ ord('1')
    modified[11] = ord(' ') ^ ord('0')
    modified[12] = ord('1') ^ ord('0')
    
    return bytes([modified[i] ^ cipher[i] for i in range(len(cipher))])

# This is Alice
key = KeyStream(10)
message = "Send Bob:   10 dollar"
message = message.encode()
cipher = encrypt(key, message)
print(message)
print(cipher)
# This is the poor transmission
# cipher = transmit(cipher)

# This is Bob tampering
cipher = tamper(cipher)

# This is the bank
key = KeyStream(10)
message = encrypt(key, cipher)
print(cipher)
print(message)

