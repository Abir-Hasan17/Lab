import numpy as np

def char_to_num(c):
    return ord(c.upper()) - ord('A')

def num_to_char(n):
    return chr((n % 26) + ord('A'))

def process_text(text, dim):
    text = ''.join([c for c in text if c.isalpha()])
    if len(text) % dim != 0:
        padding = dim - (len(text) % dim)
        text += 'X' * padding
    return text.upper()

def create_key_matrix(key):
    key = key.upper().replace(" ", "")
    key_len = len(key)
    dim = int(np.sqrt(key_len))
    if dim * dim != key_len:
        raise ValueError("Key length must be a perfect square.")
    
    key_matrix = np.array([char_to_num(c) for c in key]).reshape(dim, dim)
    return key_matrix

def mod_inverse_matrix(matrix):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = None
    for i in range(1, 26):
        if (det * i) % 26 == 1:
            det_inv = i
            break
    if det_inv is None:
        raise ValueError("Matrix determinant has no modular inverse, key is invalid.")

    adjugate_matrix = np.round(np.linalg.det(matrix) * np.linalg.inv(matrix)).astype(int)
    
    inv_matrix = (det_inv * adjugate_matrix) % 26
    return inv_matrix

def hill_cypher(text, key_matrix):
    dim = key_matrix.shape[0]
    result_text = ""

    for i in range(0, len(text), dim):
        block = text[i:i+dim]
        vec = np.array([char_to_num(c) for c in block])
        result = np.dot(key_matrix, vec) % 26
        result_block = "".join([num_to_char(n) for n in result.flatten()])
        result_text += result_block
    return result_text


def hill_encrypt(plaintext, key):
    key_matrix = create_key_matrix(key)
    dim = key_matrix.shape[0]

    plaintext = process_text(plaintext, dim)
    print("Processed Text:", plaintext)
    ciphertext = hill_cypher(plaintext, key_matrix)
    return ciphertext

def hill_decrypt(ciphertext, key):
    key_matrix = create_key_matrix(key)
    key_inv_matrix = mod_inverse_matrix(key_matrix)
    plaintext = hill_cypher(ciphertext, key_inv_matrix)
    return plaintext

plaintext = "Hello, World"
key = "hell"

ciphertext = hill_encrypt(plaintext, key)
print("Plaintext:", plaintext)
print("Key:", key)
print("Ciphertext:", ciphertext)

decrypted = hill_decrypt(ciphertext, key)
print("Decrypted:", decrypted)
