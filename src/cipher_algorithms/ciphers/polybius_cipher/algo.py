#polybius cipher

def generate_polybius_square():
    # Generate a Polybius Square mapping letters to coordinates
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    square = {}
    count = 1

    for char in alphabet:
        if char == 'J':
            continue  # Skip 'J' in the square
        row = (count - 1) // 5 + 1
        col = (count - 1) % 5 + 1
        square[char] = (row, col)
        count += 1

    return square

def encrypt_polybius(plain_text):
    # Encrypt the plain text using the Polybius Square
    plain_text = plain_text.upper()
    square = generate_polybius_square()
    cipher_text = ""

    for char in plain_text:
        if char == 'J':
            char = 'I'  # Replace 'J' with 'I'
        if char.isalpha():
            row, col = square[char]
            cipher_text += str(row) + str(col) + ' '

    return cipher_text.strip()

def decrypt_polybius(cipher_text):
    cipher_text = cipher_text.replace(' ', '')
    square = generate_polybius_square()
    plain_text = ""

    for i in range(0, len(cipher_text), 2):
        row = int(cipher_text[i])
        col = int(cipher_text[i + 1])
        char = square.get((row, col))
        if char:
            plain_text += char

    return plain_text
