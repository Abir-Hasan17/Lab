def ceaser_cypher(text, key):
    cypher_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            cypher_text += chr((ord(char) - base + key)%26 + base) 
        else: cypher_text += char
    return cypher_text

def ceaser_decypher(text, key):
    return ceaser_cypher(text, -key)

def caesar_brute_force(cipher_text):
    for key in range(1, 26):
        decrypted = ceaser_decypher(cipher_text, key)
        print(f"Key {key}: {decrypted}")



text = "Hello, World!"
key = 3

cypher_text = ceaser_cypher(text, key)
plain_text = ceaser_decypher(cypher_text, key)

print("Original Text:", text)
print("Cypher Text:", cypher_text)
print("Plain Text:", plain_text)

caesar_brute_force(cypher_text)
