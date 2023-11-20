import pytest

from cipher_algorithms.ciphers.caesar.algo import (
    caesar_cipher,
    Operation,
    InvalidCharacterException,
)


def test_encrypt_valid_messages():
    assert caesar_cipher("A", operation=Operation.ENCRYPT, shift=3) == "D"


def test_encrypt_invalid_message():
    with pytest.raises(InvalidCharacterException) as _:
        assert caesar_cipher("a", operation=Operation.ENCRYPT, shift=3)
