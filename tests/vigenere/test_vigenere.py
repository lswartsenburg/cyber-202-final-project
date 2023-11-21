import pytest

from cipher_algorithms.ciphers.vigenere.algo import (
    vigenere,
    Operation,
)
from cipher_algorithms.helpers.char_conversion_27 import InvalidCharacterException


def test_encrypt_valid_messages():
    assert vigenere("A", operation=Operation.ENCRYPT, key="TEST") == "T"
    assert (
        vigenere(
            "THE CAT IS OUT OF THE BAG", operation=Operation.ENCRYPT, key="KOMRADE"
        )
        == "CVQQCDXJWDQOXXJBRQTKIJPMX"
    )


def test_decrypt_valid_messages():
    assert vigenere("A", operation=Operation.DECRYPT, key="TEST") == "I"
    assert (
        vigenere(
            "CVQQCDXJWDQOXXJBRQTKIJPMX", operation=Operation.DECRYPT, key="KOMRADE"
        )
        == "THE CAT IS OUT OF THE BAG"
    )


def test_encrypt_invalid_message():
    with pytest.raises(InvalidCharacterException) as _:
        assert vigenere("a", operation=Operation.ENCRYPT, key="TEST")
