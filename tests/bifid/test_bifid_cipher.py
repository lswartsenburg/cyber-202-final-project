from cipher_algorithms.ciphers.bifid_cipher.algo import bifid_encrypt, bifid_decrypt


def test_encrypt_valid_messages():
    key = "KEYWORD"
    plaintext = "HELLO"
    expected_cipher = "FHYCZ"
    assert bifid_encrypt(plaintext, key) == expected_cipher


def test_decrypt_valid_messages():
    key = "KEYWORD"
    plaintext = "HELLO"
    expected_cipher = "FHYCZ"
    assert bifid_decrypt(expected_cipher, key) == plaintext
