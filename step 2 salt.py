import random
import math


def power(k, p):
    for i in range(0, p):
        if k * i % p == 1:
            return i


with open('m', 'r') as f:
    m = int(f.readline())
mold = m
with open('salt', 'r') as f:
    salt = int(f.readline())

with open('p', 'r') as f:
    p = int(f.readline())

with open('salt', 'w') as f:
    f.write(str(salt) + "\n")
    f.write(str(power(salt, p)))
m = (m * salt) % (p - 1)
print("salt m = ", mold, " with salt = ", salt, " result = ", m)
f = random.randint(2, p - 2)
while math.gcd(f, p - 1) != 1:
    f = random.randint(2, p - 2)
print("random f = ", f)
with open('f', 'w') as t:
    t.write(str(f))
with open('m_salt', 'w') as t:
    t.write(str(m))
    t.write("\n")
    t.write(str(f))
    # t.write(str((f*salt) % p))
