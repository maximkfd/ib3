# m = f * l + c*r mod p-1
with open('m_salt', 'r') as t:
    m_salt = int(t.readline())
    f = int(t.readline())
with open('sk', 'r') as t:
    c = int(t.readline())
    words = t.readline().split()
    p = int(words[0])
    q = int(words[1])
    b = int(words[2])
r = pow(q, f, p)
for i in range(0, p):
    if m_salt == (f * i + c * r*563) % (p-1):
        l = i
        break
print("lambda is " + str(l))
with open('l_salt', 'w') as t:
    t.write(str(l) + '\n' + str(f))
