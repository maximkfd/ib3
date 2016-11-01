import random

with open("p", 'r') as f:
    p = int(f.readline())
q = -1
for i in range(2, p):
    if pow(i, p - 1) % p == 1:
        q = i
        break
if q == -1:
    print("ALERT")
    exit(1)
else:
    q = 7
    print("q = " + str(q))
b = random.randint(1, p - 1)
c = pow(q, b, p)
pk = [p, q, c]
sk = [b]
print("Public key = " + str(pk))
print("Secret key = " + str(sk))

with open("pk", 'w') as f:
    print(p, q, c, end=" ", file=f)
with open("sk", 'w') as f:
    print(b, file=f)
    print(p, q, c, end=" ", file=f)
