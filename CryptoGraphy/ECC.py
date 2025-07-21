#curve: y^2 = x^3 + ax + b mod p.
p = 97
a = 2
b = 2
O = None

def is_on_curve(point):
    if point is None:
        return True
    x, y = point
    return (y * y) % p == (x * x * x + a * x + b) % p

def find_affine_points(A = a, B = b, P = p):
    points = []
    for x in range(P):
        rhs = (x ** 3 + A * x + B) % P
        for y in range(P):
            if (y * y) % P == rhs:
                points.append((x, y))
    return points

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

def point_order(P):
    Q = P
    order = 1
    while True:
        Q = point_addition(Q, P)
        order += 1
        if Q is None:
            break
    return order

def point_multiplication(P, k):
    result = None
    addend = P
    while k > 0:
        if k % 2 == 1:
            result = point_addition(result, addend)
        addend = point_addition(addend, addend)
        k //= 2
    return result

def point_neg(point):
    if point is None:
        return None
    x, y = point
    return (x, (-y) % p)

# Example usage

# affine points and their orders
affine_points = find_affine_points()
for point in affine_points:
    order = point_order(point)
    print(f"Point: {point} order: {order}")

G = (0,14)  # Generator point of high order
assert is_on_curve(G), "Generator point G is not on the curve."

P = G
Q = G
R = point_addition(P, Q)
T = point_multiplication(G, 4)
n = point_order(G)

print(f"P = {P}")
print(f"Q = {Q}")
print(f"P + Q = R = {R}")
print(f"Is R on the curve? {is_on_curve(R)}")
print(f"T = 4G = {T}")
print("order of G:", n)

# Key exchange example
print()

PRa = 9 # < n
PUa = point_multiplication(G, PRa)
key_alice = (PRa, PUa)
print("Alices private key:", PRa)
print("Alices public key:", PUa)

PRb = 3 # < n
PUb = point_multiplication(G, PRb)
key_bob = (PRb, PUb)
print("Bobs private key:", PRb)
print("Bobs public key:", PUb)

Alice_shared_secret = point_multiplication(PUb, PRa)
Bob_shared_secret = point_multiplication(PUa, PRb)
print("Alice's shared secret:", Alice_shared_secret)
print("Bob's shared secret:", Bob_shared_secret)

# encryption decryption example
print()

def encrypt(PM, key, shared_key, G):
    PR, PU = key
    C1 = PU
    C2 = point_addition(PM, shared_key)
    return (C1, C2)

def decrypt(CM, key, shared_key, G):
    C1, C2 = CM
    PR, PU = key
    #shared_key = point_multiplication(C1, PR)
    S = shared_key
    PM = point_addition(C2, point_neg(S))
    return PM

PM = (63, 77) # alices message, has to be on the curve
assert is_on_curve(PM), "Plain text PM is not on the curve."
CM = encrypt(PM, key_alice, Alice_shared_secret, G)
print("Plain text", PM,"Cypher text", CM)

decrypted_PM = decrypt(CM, key_bob, Bob_shared_secret, G)
print("Cypher text", CM, "Decrypted plain text", decrypted_PM) 

# Text encryption and decryption probably not important, but here it is
print()
def char_to_point(c):
    c = c.upper()
    x = ord(c) - ord('A') + 1  # Convert character to a number (1-26)
    while x < p:
        rhs = (x ** 3 + a * x + b) % p
        for y in range(p):
            if (y * y) % p == rhs:
                return (x, y)
        x += 1
    raise ValueError(f"Could not encode character '{c}' on the curve")

def point_to_char(point):
    x, _ = point
    return chr(x + ord('A') - 1)  # Convert number back to character (1-26)

def encrypt_text(text, key, shared_key, G):
    cypher = []
    for c in text:
        PM = char_to_point(c)
        CM = encrypt(PM, key, shared_key, G)
        cypher.append(CM)
    return cypher

def decrypt_text(cypher, key, shared_key, G):
    plain_text = ""
    for CM in cypher:
        PM = decrypt(CM, key, shared_key, G)
        plain_text += point_to_char(PM)
    return plain_text

text = "Hello"
cypher_text = encrypt_text(text, key_alice, Alice_shared_secret, G)
print("Text:", text)
print("Cypher text:", cypher_text)

decrypted_text = decrypt_text(cypher_text, key_bob, Bob_shared_secret, G)
print("Decrypted text:", decrypted_text)


