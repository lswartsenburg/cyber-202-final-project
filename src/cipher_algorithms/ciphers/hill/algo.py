import numpy as np


def prepare_text(text, key_size):
    text = text.replace(" ", "").upper()
    padding = (key_size - len(text) % key_size) % key_size
    padded_text = text + "X" * padding
    return padded_text, padding


def text_to_matrix(text, key_size):
    return np.array([ord(char) - ord("A") for char in text], dtype=int).reshape(
        -1, key_size
    )


def matrix_to_text(matrix):
    return "".join([chr(int(num) % 26 + ord("A")) for num in matrix.flatten()])


def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def generate_key(key_str, key_size):
    key_size_squared = key_size * key_size
    key = np.array([ord(char) - ord("A") for char in key_str], dtype=int)

    if len(key) < key_size_squared:
        raise ValueError(
            "Key length is less than the required size for a square matrix."
        )

    key = key[:key_size_squared].reshape(key_size, key_size)
    return key


def encrypt(plain_text, key_str):
    key_size = int(len(key_str) ** 0.5)
    key = generate_key(key_str, key_size)
    padded_text, _ = prepare_text(plain_text, key_size)
    plain_matrix = text_to_matrix(padded_text, key_size)
    cipher_matrix = (plain_matrix @ key) % 26
    return matrix_to_text(cipher_matrix)


def decrypt(cipher_text, key_str):
    key_size = int(len(key_str) ** 0.5)
    key = generate_key(key_str, key_size)
    key_det = int(round(np.linalg.det(key)))

    if key_det == 0:
        raise ValueError(
            "The determinant of the key matrix is zero. Unable to calculate the modular inverse."
        )

    key_det_inv = mod_inverse(key_det, 26)

    key_adjugate = np.round(np.linalg.inv(key) * np.linalg.det(key)).astype(int)
    key_inv_mod = (key_det_inv * key_adjugate) % 26

    cipher_matrix = text_to_matrix(cipher_text, key_size)
    plain_matrix = (cipher_matrix @ key_inv_mod) % 26
    decoded_text = matrix_to_text(plain_matrix)

    return decoded_text


if __name__ == "__main__":
    key_str = "HELLO"
    plaintext = "TESTINGABC"

    cipher_text = encrypt(plaintext, key_str)
    decoded_text = decrypt(cipher_text, key_str)

    print("Original Text:", plaintext)
    print("Encoded Text:", cipher_text)
    print("Decoded Text:", decoded_text)
