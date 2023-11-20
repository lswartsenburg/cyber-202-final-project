import pytest

from cipher_algorithms.ciphers.vigenere.algo import (
    vigenere,
    Operation,
)
from cipher_algorithms.helpers.char_conversion_27 import InvalidCharacterException


def test_encrypt_valid_messages():
    assert vigenere("A", operation=Operation.ENCRYPT, key="TEST") == "T"


def test_decrypt_valid_messages():
    assert vigenere("A", operation=Operation.DECRYPT, key="TEST") == "I"


def test_encrypt_invalid_message():
    with pytest.raises(InvalidCharacterException) as _:
        assert vigenere("a", operation=Operation.ENCRYPT, key="TEST")
