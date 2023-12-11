def generate_key_matrix(key):
    key = key.replace("J", "I")
    key = key.upper()
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_matrix = [["" for _ in range(5)] for _ in range(5)]
    key_set = set()

    i, j = 0, 0
    for letter in key + alphabet:
        if letter not in key_set:
            key_matrix[i][j] = letter
            key_set.add(letter)
            j += 1
            if j == 5:
                j = 0
                i += 1

    return key_matrix


def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j


def encrypt(plain_text, key):
    key_matrix = generate_key_matrix(key)
    cipher_text = ""
    plain_text = plain_text.upper().replace("J", "I")
    plain_text = plain_text.replace(" ", "")

    if len(plain_text) % 2 != 0:
        plain_text += "X"

    for i in range(0, len(plain_text), 2):
        char1, char2 = plain_text[i], plain_text[i + 1]

        row1, col1 = find_position(key_matrix, char1)
        row2, col2 = find_position(key_matrix, char2)

        if row1 == row2:
            cipher_text += (
                key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
            )
        elif col1 == col2:
            cipher_text += (
                key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
            )
        else:
            cipher_text += key_matrix[row1][col2] + key_matrix[row2][col1]

    return cipher_text


def decrypt(cipher_text, key):
    key_matrix = generate_key_matrix(key)
    cipher_text = cipher_text.upper().replace(" ", "")
    plain_text = ""

    for i in range(0, len(cipher_text), 2):
        char1, char2 = cipher_text[i], cipher_text[i + 1]

        row1, col1 = find_position(key_matrix, char1)
        row2, col2 = find_position(key_matrix, char2)

        if row1 == row2:
            plain_text += (
                key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
            )
        elif col1 == col2:
            plain_text += (
                key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
            )
        else:
            plain_text += key_matrix[row1][col2] + key_matrix[row2][col1]

    return plain_text


if __name__ == "__main__":
    key = "HELLO"
    text = "TESTINGABC"
    cipher_text = encrypt(text, key)
    plain_text = decrypt(cipher_text, key)

    print("Original Text:", text)
    print("Encoded Text:", cipher_text)
    print("Decoded Text:", plain_text)
