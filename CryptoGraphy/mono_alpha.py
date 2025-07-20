import random
import string

def generate_key():
    letters = list(string.ascii_uppercase)
    shuffled = letters[:]
    random.shuffle(shuffled)
    key = dict(zip(letters, shuffled))
    return key

def monoalphabetic_cypher(text, key):
    cypher_text = ""
    for char in text.upper():
        if char in key:
            cypher_text += key[char]
        else:
            cypher_text += char
    return cypher_text

def monoalphabetic_decypher(cypher_text, key):
    reverse_key = {v: k for k, v in key.items()}
    return monoalphabetic_cypher(cypher_text, reverse_key)
    
key = generate_key()
text = "HELLO WORLD"
print("Key:\n", key)

cypher_text = monoalphabetic_cypher(text, key)
print(cypher_text)

plain_text = monoalphabetic_decypher(cypher_text, key)
print(plain_text)
