p = 23
g = 5

def power(base, exp, mod):
    res = 1
    base = base % mod
    while exp>0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp = exp // 2
    return res

alice_private_key = 6
alice_public_key = power(g, alice_private_key, p)

bob_private_key = 15
bob_public_key = power(g, bob_private_key, p)

alice_shared_secret = power(bob_public_key, alice_private_key, p)
bob_shared_secret = power(alice_public_key, bob_private_key, p)

print("Alice's Private Key:", alice_private_key)
print("Alice's Public Key:", alice_public_key)

print("Bob's Private Key:", bob_private_key)
print("Bob's Public Key:", bob_public_key)

print("Alice's Shared Secret:", alice_shared_secret)
print("Bob's Shared Secret:", bob_shared_secret)