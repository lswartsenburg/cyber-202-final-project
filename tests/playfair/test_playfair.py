from cipher_algorithms.ciphers.playfair.algo import (
    encrypt,
    decrypt,
)


def test_playfair_encrypt():
    plaintext = "TESTINGABC"
    key = "HELLO"
    cipher = encrypt(plaintext, key)

    assert cipher == "ROTUKPPGCD"


def test_playfair_decrypt():
    plaintext = "ROTUKPPGCD"
    key = "HELLO"
    cipher = decrypt(plaintext, key)

    assert cipher == "TESTINGABC"
