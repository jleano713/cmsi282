import math

def egcd(a, b):
    prevx, x = 1, 0; prevy, y = 0, 1
    while b:
        q = a/b
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
        a, b = b, a % b
    return a, prevx, prevy

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

n = 729880581317
e = 7
p = math.floor(math.sqrt(n))
boolean = False
while (not boolean):
    p = p - 1
    if (math.fmod(n, p) == 0):
        print(str(p))
        boolean = True
q = n / p
print("n: " + str(n) + " / p: " + str(p) + " / q: " + str(q))

d = (1 /e) % ((p - 1) * (q - 1))
print(d)
print(str(1 % 352))