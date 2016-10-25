import random

with open("p", 'r') as f:
    n = int(f.readline())
q = -1
for i in range(2, n):
    if pow(i, n - 1) % n == 1:
        q = i
        break
if q == -1:
    print("ALERT")
    exit(1)
else:
    print("q = " + str(q))
b = random.randint(1, n - 1)
c = pow(q, b) % n
pk = [n, q, c]
sk = [b]
print("Public key = " + str(pk))
print("Secret key = " + str(sk))

with open("pk", 'w') as f:
    print(n, q, c, end=" ", file=f)
with open("sk", 'w') as f:
    print(b, file=f)
    print(n, q, c, end=" ", file=f)
