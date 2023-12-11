# Mostly WIP :)
# test_polygram_substitution_cipher.py
import pytest
from cipher_algorithms.ciphers.polygram_substitution_cipher.algo import (
    encrypt,
    decrypt,
    UnsupportedCharacterError,
)


def test_encrypt_decrypt():
    # Test case for successful encryption and decryption
    plaintext = "ABCD"
    expected_encrypted = "CPWB"  # Expected result based on your encryption scheme
    encrypted = encrypt(plaintext)
    decrypted = decrypt(encrypted)

    assert encrypted == expected_encrypted
    assert decrypted == plaintext


def test_unsupported_characters_encryption():
    # Test case for encryption with unsupported characters
    plaintext = "xye"  # Assuming WXYZ is not supported by your scheme
    with pytest.raises(UnsupportedCharacterError):
        encrypt(plaintext)


def test_unsupported_characters_decryption():
    # Test case for decryption with unsupported characters
    encrypted_text = "xye"  # Assuming WXYZ is not supported by your scheme
    with pytest.raises(UnsupportedCharacterError):
        decrypt(encrypted_text)


# TODO - Add more tests as needed
