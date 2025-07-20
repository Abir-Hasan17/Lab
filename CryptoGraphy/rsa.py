from math import gcd
import random


def modular_inverse(a, m):
    m0, x0, x1 = m, 0, 1

    while a>1:
        q = a//m
        a, m = m, a%m
        x0, x1 = x1 - q*x0, x0
    
    return x1%m0

def power(base, exp, mod):
    res = 1
    base = base % mod
    while exp>0:
        if exp%2 ==1:
            res = (res*base) % mod
        base = (base*base) % mod
        exp = exp//2
    return res

def gen_key(p, q):
    n = p*q
    phi = (p-1)*(q-1)

    while True:
        e = random.randint(2, phi-1)
        if gcd(phi, e) != 1:
            continue
        d = modular_inverse(e, phi)
        if e != d: break
    return (e, n), (d, n)

def rsa_encrypt_dycrypt(data, key):
    k, n = key
    return power(data, k, n)

def rsa_text_encrypt(text, key):
    encrypted_data = []
    for char in text:
        encrypted_data.append(str(rsa_encrypt_dycrypt(ord(char), key)))
    return " ".join(encrypted_data)

def rsa_text_dycrypt(text, key):
    plain_text = ''
    encrypted_data = text.split(' ')
    for data in encrypted_data:
        plain_text += chr(rsa_encrypt_dycrypt(int(data), key))
    return plain_text

public_key, private_key = gen_key(53777, 10369)
print("Public Key:", public_key)
print("Private Key:", private_key)

data = 30
encrypted_data = rsa_encrypt_dycrypt(data, public_key)
print("Encrypted Data:", encrypted_data)
decrypted_data = rsa_encrypt_dycrypt(encrypted_data, private_key)
print("Decrypted Data:", decrypted_data)

text = "hello world"
cypher_text = rsa_text_encrypt(text, public_key)
print("Encrypted Text:", cypher_text)
plain_text = rsa_text_dycrypt(cypher_text, private_key)
print("Decrypted Text:", plain_text)
