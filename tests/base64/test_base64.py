from cipher_algorithms.ciphers.base64.algo import (
    encrypt,
    decrypt,
)


def test_base64_encrypt():
    plaintext = "testingabc"
    cipher = encrypt(plaintext)

    assert cipher == "dGVzdGluZ2FiYw=="


def test_base64_encrypt_long():
    plaintext_long = "this is an important message"
    cipher_long = encrypt(plaintext_long)
    assert cipher_long == "dGhpcyBpcyBhbiBpbXBvcnRhbnQgbWVzc2FnZQ=="


def test_base64_decrypt():
    cipher = "dGVzdGluZ2FiYw=="
    plaintext = decrypt(cipher)

    assert plaintext == "testingabc"


def test_base64_decrypt_long():
    cipher_long = "dGhpcyBpcyBhbiBpbXBvcnRhbnQgbWVzc2FnZQ=="
    plaintext_long = decrypt(cipher_long)
    assert plaintext_long == "this is an important message"
