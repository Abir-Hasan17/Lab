from math import gcd
import random

def gen_key(p, q):
    n = p*q
    phi = (p-1)*(q-1)

    while True:
        e = random.randint(2, phi-1)
        if gcd(phi, e) != 1:
            continue
        d = pow(e, -1, phi) # Modular inverse
        if e != d: break
    return (e, n), (d, n)

def rsa_encrypt_dycrypt(data, key):
    k, n = key
    return pow(data, k, n) # Encrypt or decrypt using modular exponentiation

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
