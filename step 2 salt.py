import random
import math

with open('m', 'r') as f:
    m = int(f.readline())
salt = 563
# salt -1 = 250
with open('p', 'r') as f:
    p = int(f.readline())
m = (m*salt) % (p-1)
f = random.randint(2, p-2)
while math.gcd(f, p-1) != 1:
    f = random.randint(2, p-2)
with open('f', 'w') as t:
    t.write(str(f))
with open('m_salt', 'w') as t:
    t.write(str(m))
    t.write("\n")
    t.write(str(f))
    # t.write(str((f*salt) % p))
