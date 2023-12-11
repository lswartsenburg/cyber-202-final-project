from cipher_algorithms.ciphers.hill.algo import (
    encrypt,
    decrypt,
)


def test_hill_encrypt():
    plaintext = "TESTINGABC"
    key = "HELLO"
    cipher = encrypt(plaintext, key)

    assert cipher == "VQXVRTQYDA"


def test_hill_decrypt():
    plaintext = "VQXVRTQYDA"
    key = "HELLO"
    cipher = decrypt(plaintext, key)

    assert cipher == "TESTINGABC"
