from math import gcd

with open('l_salt', 'r') as t:
    salt_f = int(t.readline())
    salt_l = int(t.readline())
with open('sk', 'r') as t:
    c = int(t.readline())
    words = t.readline().split()
    p = int(words[0])
    q = int(words[1])
    b = int(words[2])
with open('salt', 'r') as t:
    salt = int(t.readline())
    desalt = int(t.readline())
with open('m_salt', 'r') as t:
    m_salt = int(t.readline())
l = salt_l * desalt % (p)
f = salt_f * desalt % (p)
m = m_salt * desalt % (p)
print("l = ", l)
print("f = ", f)
print("f = ", salt_f)
print("f = ", gcd(f, p-1))

v1 = pow(b, salt_f, p)
v1 = (v1*pow(salt_f, salt_l, p)) % p
v2 = pow(q, m_salt, p)
if v1 == v2:
    print("Ok")
else:
    print("shit")

a = pow(q, f, p)
v1 = pow(b, a, p)
v1 = (v1*pow(a, l, p)) % p
v2 = pow(q, m, p)
if v1 == v2:
    print("Ok")
else:
    print("shit")
# print("l = ", l)
# print("f = ", f)
# print("p = ", p)
# r = pow(q, f, p)
# # print("m salt = ", m*salt % (p-1))
# print((f*l + c*r) % (p-1))
#
# print(((f*salt_l + c * r * salt)*desalt) % (p-1))

# ?(looks like) salt is mod p
# ? salt is mod p-1
