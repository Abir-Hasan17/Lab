#curve: y^2 = x^3 + ax + b mod p.
p = 97
a = 2
b = 3
O = None

def is_on_curve(point):
    if point is None:
        return True
    x, y = point
    return (y * y) % p == (x * x * x + a * x + b) % p

def point_addition(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    
    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and y1 != y2:
        return None
    if P == Q:
        m = (3 * x1 * x1 + a) * pow(2 * y1, -1, p) % p
    else:
        m = (y2 - y1) * pow(x2 - x1, -1, p) % p
    
    m = m % p
    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)

def point_multiplication(P, k):
    result = None
    addend = P
    while k > 0:
        if k % 2 == 1:
            result = point_addition(result, addend)
        addend = point_addition(addend, addend)
        k //= 2
    return result

def point_order(P):
    Q = P
    order = 1
    while True:
        Q = point_addition(Q, P)
        order += 1
        if Q is None:
            break
    return order


# Example usage

G = (17,10)  # Generator point of high order
assert is_on_curve(G), "Generator point G is not on the curve."

P = G
Q = G
R = point_addition(P, Q)
T = point_multiplication(G, 4)

print(f"P = {P}")
print(f"Q = {Q}")
print(f"P + Q = R = {R}")
print(f"Is R on the curve? {is_on_curve(R)}")
print(f"T = 4G = {T}")

# Key exchange example

PRa = 3
PUa = point_multiplication(G, PRa)
print("Alices private key:", PRa)
print("Alices public key:", PUa)

PRb = 5
PUb = point_multiplication(G, PRb)
print("Bobs private key:", PRb)
print("Bobs public key:", PUb)

Alice_shared_secret = point_multiplication(PUb, PRa)
Bob_shared_secret = point_multiplication(PUa, PRb)
print("Alice's shared secret:", Alice_shared_secret)
print("Bob's shared secret:", Bob_shared_secret)