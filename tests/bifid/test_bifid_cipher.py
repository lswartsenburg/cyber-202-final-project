# WIP

def create_polybius_square(keyword):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # 'J' combined with 'I'
    square = {}
    used_letters = set()
    i = 0

    for char in keyword.upper() + alphabet:
        if char not in used_letters and char in alphabet:
            square[char] = (i // 5, i % 5)
            used_letters.add(char)
            i += 1

    return square

def bifid_encrypt(plaintext, keyword):
    square = create_polybius_square(keyword)
    coords = [square[char] for char in plaintext.upper() if char in square]

    rows, cols = zip(*coords)
    mixed_coords = rows + cols

    encrypted = ''
    for i in range(0, len(mixed_coords), 2):
        encrypted += next((k for k, v in square.items() if v == (mixed_coords[i], mixed_coords[i+1])), '')

    return encrypted

def bifid_decrypt(ciphertext, keyword):
    square = create_polybius_square(keyword)
    coords = [square[char] for char in ciphertext.upper() if char in square]

    rows, cols = zip(*coords)
    mixed_coords = sum(zip(rows, cols), ())

    decrypted = ''
    for i in range(0, len(mixed_coords), 2):
        decrypted += next((k for k, v in square.items() if v == (mixed_coords[i], mixed_coords[i+1])), '')

    return decrypted

# Example usage
keyword = "KEYWORD"
plaintext = "HELLO"
encrypted_text = bifid_encrypt(plaintext, keyword)
decrypted_text = bifid_decrypt(encrypted_text, keyword)

print(f"Plaintext: {plaintext}")
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")
