from cipher_algorithms.ciphers.columnar_transposition.algo import (
    encryptMessage,
    decryptMessage,
)


def test_encrypt_valid_messages():
    plaintext = "QUICK BROWN FOX JUMPS"
    key = "HELLO"
    expected_cipher = "UROPQBFMIOXSCWJKNU"
    assert encryptMessage(plaintext, key) == expected_cipher


def test_decrypt_valid_messages():
    plaintext = "QUICK BROWN FOX JUMPS"
    expected_cipher = "UROPQBFMIOXSCWJKNU"
    key = "HELLO"
    assert decryptMessage(expected_cipher, key) == plaintext
