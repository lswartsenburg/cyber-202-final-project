from cipher_algorithms.ciphers.base64.algo import (
    encrypt,
    decrypt,
)


def test_base64_encrypt():
    plaintext = "testingabc"
    cipher = encrypt(plaintext)

    assert cipher == "dGVzdGluZ2FiYw=="


def test_base64_decrypt():
    cipher = "dGVzdGluZ2FiYw=="
    plaintext = decrypt(cipher)

    assert plaintext == "testingabc"
