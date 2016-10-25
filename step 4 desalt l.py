with open('l_salt', 'r') as t:
    salt_l = int(t.readline())
    salt_f = int(t.readline())
with open('sk', 'r') as t:
    c = int(t.readline())
    words = t.readline().split()
    p = int(words[0])
    q = int(words[1])
    b = int(words[2])
l = salt_l * 250 % p
m = 132
# f = salt_f * 250 % p
f = salt_f
print("l = ", l)
print("f = ", f)
print("p = ", p)
r = pow(q, f, p)
salt = 564
desalt = 23
print("m salt = ", m*salt % (p-1))
print(m)
print("WHAAAAAAAAAAAAAAAAT", (f*salt_l * desalt + c * r * salt * desalt) % (p-1))
print((f*l + c*r) % (p-1))

print(m*salt % p)
print((f*salt_l + c * r * salt) % (p-1))

print()
print(((f*salt_l + c * r * salt)*desalt) % (p-1))
