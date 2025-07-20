import string


def gen_matrix(key):
    key = key.replace("I", "J")
    key = key.upper()
    matrix = []
    added = set()
    for char in key:
        if char not in added:
            matrix.append(char)
        else:
            added.add(char)
    for char in string.ascii_uppercase:
        if char not in added:
            matrix.append(char)
        else:
            added.add(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_pos(char, matrix):
    for i in range(5):
        for j in range(5):
            print(i,j)
            if char == matrix[i][j]:
                return i,j
            
    return None, None

def encrypt_decrypt_pair(a, b, matrix, ed):
    row_a, col_a = find_pos(a, matrix)
    row_b, col_b = find_pos(b, matrix)

    if row_a == row_b:
        return matrix[row_a][(col_a + ed)%5] + matrix[row_b][(col_b + ed)%5]
    elif col_a == col_b:
        return matrix[(row_a + ed) % 5][col_a] + matrix[(row_b + ed) % 5][col_b]
    else:
        return matrix[row_a][col_b] + matrix[row_b][col_a]
    
def process_txt(text):
    text = text.upper().replace("I", "J")
    text = ''.join(filter(str.isalpha, text))
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            text = text[:i + 1] + 'X' + text[i + 1:]
    if len(text) % 2 != 0:
        text += 'X'
    return text

def playfair_encrypt(text, key):
    matrix = gen_matrix(key)
    text = process_txt(text)
    cyphertext = ''
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        # print(f"Encrypting pair: {a}, {b}")
        cyphertext += encrypt_decrypt_pair(matrix, a, b, 1)
    return cyphertext

def playfair_decrypt(text, key):
    matrix = gen_matrix(key)
    plaintext = ''
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        plaintext += encrypt_decrypt_pair(matrix, a, b, -1)
    return plaintext

key = "PLAYFAIR"
text = "HIDE THE GOLD IN THE TREE STUMP"
print(gen_matrix(key))
print("Original Text:", text)
cyphertext = playfair_encrypt(text, key)
print("Encrypted:", cyphertext)
plaintext = playfair_decrypt(cyphertext, key)
print("Decrypted:", plaintext)