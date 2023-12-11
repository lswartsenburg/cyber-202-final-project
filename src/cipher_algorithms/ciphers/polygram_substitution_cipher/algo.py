from cipher_algorithms.ciphers.polygram_substitution_cipher.key_gen import (
    DEFAULT_ENCRYPTION_DICT,
)


class UnsupportedCharacterError(Exception):
    """Custom exception for unsupported characters."""

    pass


def encrypt(text, key=None):
    encryption_dict = key if key is not None else DEFAULT_ENCRYPTION_DICT
    encrypted = ""
    for i in range(0, len(text), 2):
        digram = text[i : i + 2]
        if digram not in encryption_dict and len(digram) == 2:
            raise UnsupportedCharacterError(f"Unsupported characters found: {digram}")
        encrypted += encryption_dict.get(digram, digram)
    return encrypted


def decrypt(text, key=None):
    encryption_dict = key if key is not None else DEFAULT_ENCRYPTION_DICT
    decryption_dict = {v: k for k, v in encryption_dict.items()}
    decrypted = ""
    for i in range(0, len(text), 2):
        digram = text[i : i + 2]
        if digram not in decryption_dict and len(digram) == 2:
            raise UnsupportedCharacterError(f"Unsupported characters found: {digram}")
        decrypted += decryption_dict.get(digram, digram)
    return decrypted


# Example usage
if __name__ == "__main__":
    try:
        plaintext = "HELLO"
        encrypted_text = encrypt(plaintext)
        decrypted_text = decrypt(encrypted_text)

        print(f"Plaintext: {plaintext}")
        print(f"Encrypted: {encrypted_text}")
        print(f"Decrypted: {decrypted_text}")
    except UnsupportedCharacterError as e:
        print(f"Error: {e}")
