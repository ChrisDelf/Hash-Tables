import time
import hashlib

n = 1000000

key = b"Blue"

for _ in range(10):
    # it prints an objects we can hexdigest to show it
    print(int(hashlib.sha256(key).hexdigest(), 16) % 8)
