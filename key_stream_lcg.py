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


# This is Alice
key = KeyStream(10)
message = "Hello, World!"
message = message.encode()
cipher = encrypt(key, message)

# This is Bob
key = KeyStream(10)
message = encrypt(key, cipher)
print(message)
