# m = f * l + c*r mod p-1


def inverse(k, p):
    for i in range(0, p):
        if k * i % p == 1:
            return i


with open('m_salt', 'r') as t:
    m_salt = int(t.readline())
    f = int(t.readline())
with open('salt', 'r') as t:
    salt = int(t.readline())
with open('sk', 'r') as t:
    c = int(t.readline())
    words = t.readline().split()
    p = int(words[0])
    q = int(words[1])
    b = int(words[2])
r = pow(q, f, p)
fuck = (m_salt-c*r) % (p-1)
while fuck < 0:
    fuck += (p-1)
b = (fuck*inverse(f, p-1)) % (p-1)
print("f =", f)
# for i in range(0, p):
#     if m_salt == (f * i + c * r*salt) % (p-1):
#         l = i
#         break
# print("lambda is " + str(l))
with open('l_salt', 'w') as t:
    t.write(str(r) + '\n' + str(b))
