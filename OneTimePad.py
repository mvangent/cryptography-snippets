import random

def generate_key_stream(n):
    return bytes([random.randrange(0, 255) for _ in range(n)])

def xor_bytes(key_stream, message):
    length = min(len(key_stream), len(message))

    return bytes([key_stream[i] ^ message[i] for i in range(length)])

message = "This is Major Tom to ground control. I've left foreever more. And I'm floating in the most peculiar way, and the Stars look very different today"
message = message.encode()
key_stream = generate_key_stream(len(message))
cipher = xor_bytes(key_stream, message)

print(key_stream)
print(cipher)
print(xor_bytes(key_stream, cipher))

# why it's so strong?

# this is done by your enemy
message = "DO ATTACK"
message = message.encode()
key_stream = generate_key_stream(len(message))
cipher = xor_bytes(key_stream, message)


# this is us trying to break it
message = "NO ATTACK"
message = message.encode()
guess_key_stream = xor_bytes(message, cipher)
print(xor_bytes(guess_key_stream, cipher)) # Prints: "NO ATTACK"
