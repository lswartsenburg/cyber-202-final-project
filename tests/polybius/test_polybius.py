from cipher_algorithms.ciphers.polybius_cipher.algo import (
    encrypt_polybius,
    decrypt_polybius,
)


def test_playfair_encrypt():
    plaintext = "the quick brown fox jumps over the lazy dog"
    cipher = encrypt_polybius(plaintext)

    assert (
        cipher
        == "44 23 15 41 45 24 13 25 12 42 34 52 33 21 34 53 24 45 32 35 43 34 51 15 42 44 23 15 31 11 55 54 14 34 22"
    )


def test_playfair_decrypt():
    cipher = "44 23 15 41 45 24 13 25 12 42 34 52 33 21 34 53 24 45 32 35 43 34 51 15 42 44 23 15 31 11 55 54 14 34 22"
    plaintext = decrypt_polybius(cipher)

    assert plaintext == "thequickbrownfoxiumpsoverthelazydog"
