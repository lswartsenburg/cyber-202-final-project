# Mostly WIP :)
# test_polygram_substitution_cipher.py
import pytest
from cipher_algorithms.ciphers.polyalphabetic_substitution_cipher.algo import encrypt, decrypt, CipherError

def test_encrypt_decrypt_basic():
    # Test basic encryption and decryption
    plaintext = "HELLOWORLD"
    keyword = "KEY"
    encrypted = encrypt(plaintext, keyword)
    decrypted = decrypt(encrypted, keyword)

    assert decrypted == plaintext

def test_empty_input():
    # Test with empty string for text and keyword
    with pytest.raises(CipherError):
        encrypt("", "KEY")
    with pytest.raises(CipherError):
        decrypt("", "KEY")

def test_non_alpha_input():
    # Test with non-alphabetical characters in text and keyword
    with pytest.raises(CipherError):
        encrypt("HELLO123", "KEY")
    with pytest.raises(CipherError):
        decrypt("HELLO123", "KEY")

    with pytest.raises(CipherError):
        encrypt("HELLO", "KEY1")
    with pytest.raises(CipherError):
        decrypt("HELLO", "KEY1")

def test_same_encryption_decryption():
    # Test that encrypted text is not the same as plaintext
    plaintext = "HELLOWORLD"
    keyword = "KEY"
    encrypted = encrypt(plaintext, keyword)

    assert encrypted != plaintext

# Add more tests as needed

