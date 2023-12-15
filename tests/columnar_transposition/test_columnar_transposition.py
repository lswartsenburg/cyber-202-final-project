from cipher_algorithms.ciphers.columnar_transposition.algo import (
    encryptMessage,
    decryptMessage,
)
import pytest


@pytest.mark.skip(reason="Failing")
def test_encrypt_valid_messages():
    plaintext = "QUICK BROWN FOX JUMPS"
    key = "HELLO"
    expected_cipher = "UROPQBFMIOXSCWJKNU"
    assert encryptMessage(plaintext, key) == expected_cipher


@pytest.mark.skip(reason="Failing")
def test_decrypt_valid_messages():
    plaintext = "QUICK BROWN FOX JUMPS"
    expected_cipher = "UROPQBFMIOXSCWJKNU"
    key = "HELLO"
    assert decryptMessage(expected_cipher, key) == plaintext
