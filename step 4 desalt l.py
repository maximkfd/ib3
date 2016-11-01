with open('l_salt', 'r') as t:
    salt_l = int(t.readline())
    salt_f = int(t.readline())
with open('sk', 'r') as t:
    c = int(t.readline())
    words = t.readline().split()
    p = int(words[0])
    q = int(words[1])
    b = int(words[2])
m = 132
salt = 563
# desalt = 912
desalt = 23
l = salt_l * desalt % (p-1)
# f = salt_f * 250 % p
f = salt_f
print("l = ", l)
print("f = ", f)
print("p = ", p)
r = pow(q, f, p)
print("m salt = ", m*salt % (p-1))
print((f*l + c*r) % (p-1))

print(((f*salt_l + c * r * salt)*desalt) % (p-1))

# ?(looks like) salt is mod p
# ? salt is mod p-1
