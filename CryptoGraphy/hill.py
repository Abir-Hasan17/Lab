import numpy as np

def char_to_num(c):
    return ord(c.upper()) - ord('A')

def num_to_char(n):
    return chr((n % 26) + ord('A'))

def create_key_matrix(key):
    key = key.upper().replace(" ", "")
    if len(key) != 4:
        raise ValueError("Key must be 4 letters for 2x2 matrix.")
    key_matrix = [[char_to_num(key[0]), char_to_num(key[1])],
                  [char_to_num(key[2]), char_to_num(key[3])]]
    return np.array(key_matrix)

def mod_inverse_matrix(matrix):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = None
    for i in range(1, 26):
        if (det * i) % 26 == 1:
            det_inv = i
            break
    if det_inv is None:
        raise ValueError("Matrix determinant has no modular inverse, key is invalid.")

    adj = np.array([[matrix[1][1], -matrix[0][1]],
                    [-matrix[1][0], matrix[0][0]]])
    
    inv_matrix = (det_inv * adj) % 26
    return inv_matrix

def hill_cypher(text, key_matrix):
    result_text = ""
    for i in range(0, len(text), 2):
        block = text[i:i+2]
        vec = np.array([[char_to_num(block[0])], [char_to_num(block[1])]])
        result = np.dot(key_matrix, vec) % 26
        result_block =  num_to_char(result[0][0]) + num_to_char(result[1][0])
        result_text += result_block
    return result_text


def hill_encrypt(plaintext, key):
    if len(plaintext) % 2 != 0:
        plaintext += 'X' 

    key_matrix = create_key_matrix(key)
    ciphertext = hill_cypher(plaintext, key_matrix)
    return ciphertext

def hill_decrypt(ciphertext, key):
    key_matrix = create_key_matrix(key)
    key_inv_matrix = mod_inverse_matrix(key_matrix)
    plaintext = hill_cypher(ciphertext, key_inv_matrix)
    return plaintext

plaintext = "HELLO"
key = "HILL"

ciphertext = hill_encrypt(plaintext, key)
decrypted = hill_decrypt(ciphertext, key)

print("Plaintext:", plaintext)
print("Key:", key)
print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted)
