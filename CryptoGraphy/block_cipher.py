B = 8 #block size

# Simple ECB

def padd(text):
    padd_length  = B - (len(text) % B)
    return text + bytes([padd_length] * padd_length)

def unpadd(text):
    padd_length = text[-1]
    return text[:-padd_length]

def xor_block(block, key):
    return bytes([block[i] ^ key[i % len(key)] for i in range(B)])

def ecb_encrypt(key, plaintext):
    padded = padd(plaintext)
    ciphertext = b""

    for i in range(0, len(padded), B):
        block = padded[i:i+B]
        ciphertext += xor_block(block, key)

    return ciphertext

def ecb_decrypt(key, ciphertext):
    plaintext = b""

    for i in range(0, len(ciphertext), B):
        block = ciphertext[i:i+B]
        plaintext += xor_block(block, key)

    return unpadd(plaintext)

print("\nECB Mode Encryption/Decryption Example")
text = b"Hello, World!"
key = b"secret"

ciphertext = ecb_encrypt(key, text)
print("Ciphertext:", ciphertext)

plaintext = ecb_decrypt(key, ciphertext)
print("Decrypted plaintext:", plaintext)

# Simple CBC

def cbc_encrypt(key, plaintext, iv):
    padded = padd(plaintext)
    ciphertext = b""
    prev = iv

    for i in range(0, len(padded), B):
        block = padded[i:i+B]
        pre_encrypted = xor_block(block, prev)
        encrypted = xor_block(pre_encrypted, key)
        ciphertext += encrypted
        prev = encrypted
    return ciphertext

def cbc_decrypt(key, ciphertext, iv):
    plaintext = b""
    prev = iv

    for i in range(0, len(ciphertext), B):
        block = ciphertext[i:i+B]
        pre_decrypted = xor_block(block, key)
        decrypted = xor_block(pre_decrypted, prev)
        plaintext += decrypted
        prev = block
    return unpadd(plaintext)

print("\nCBC Mode Encryption/Decryption Example")
iv = b"initialvectr"
text = b"Hello, World!"
key = b"secret"

ciphertext = cbc_encrypt(key, text, iv)
print("Ciphertext:", ciphertext)

plaintext = cbc_decrypt(key, ciphertext, iv)
print("Decrypted plaintext:", plaintext)

# Simple CFB same same but different from CBC

def cfb_encrypt(key, plaintext, iv):
    padded = padd(plaintext)
    ciphertext = b""
    prev = iv

    for i in range(0, len(padded), B):
        block = padded[i:i+B]
        pre_encrypted = xor_block(prev, key)
        encrypted = xor_block(block, pre_encrypted)
        ciphertext += encrypted
        prev = encrypted
    return ciphertext

def cfb_decrypt(key, ciphertext, iv):
    plaintext = b""
    prev = iv

    for i in range(0, len(ciphertext), B):
        block = ciphertext[i:i+B]
        pre_decrypted = xor_block(prev, key)
        decrypted = xor_block(block, pre_decrypted)
        plaintext += decrypted
        prev = block
    return unpadd(plaintext)

print("\nCFB Mode Encryption/Decryption Example")
iv = b"initialvectr"
text = b"Hello, World!"
key = b"secret"

ciphertext = cfb_encrypt(key, text, iv)
print("Ciphertext:", ciphertext)

plaintext = cfb_decrypt(key, ciphertext, iv)
print("Decrypted plaintext:", plaintext)

# Simple OFB

def ofb_encrypt(key, plaintext, iv):
    padded = padd(plaintext)
    ciphertext = b""
    prev = iv

    for i in range(0, len(padded), B):
        prev = xor_block(prev, key) # encrypt the IV and feed it back
        block = padded[i:i+B]
        encrypted = xor_block(block, prev)
        ciphertext += encrypted
    return ciphertext

def ofb_decrypt(key, ciphertext, iv):
    plaintext = b""
    prev = iv

    for i in range(0, len(ciphertext), B):
        prev = xor_block(prev, key) # encrypt the IV and feed it back
        block = ciphertext[i:i+B]
        decrypted = xor_block(block, prev)
        plaintext += decrypted
    return unpadd(plaintext)

print("\nOFB Mode Encryption/Decryption Example")
iv = b"initialvectr"
text = b"Hello, World!"
key = b"secret"

ciphertext = ofb_encrypt(key, text, iv)
print("Ciphertext:", ciphertext)

plaintext = ofb_decrypt(key, ciphertext, iv)
print("Decrypted plaintext:", plaintext)
