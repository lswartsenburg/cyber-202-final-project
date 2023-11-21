import pytest

from cipher_algorithms.ciphers.caesar.algo import caesar_cipher, Operation, break_cipher
from cipher_algorithms.helpers.char_conversion_27 import InvalidCharacterException
from cipher_algorithms.helpers.dictionary import get_dictionary


def test_encrypt_valid_messages():
    assert caesar_cipher("A", operation=Operation.ENCRYPT, shift=3) == "D"
    assert (
        caesar_cipher(
            "MATT IS SHORTER THAN AARON", operation=Operation.ENCRYPT, shift=18
        )
        == "DSKKR JRJZFIKWIRKZSERSSIFE"
    )


def test_decrypt_valid_messages():
    assert caesar_cipher("D", operation=Operation.DECRYPT, shift=3) == "A"
    assert (
        caesar_cipher(
            "DSKKR JRJZFIKWIRKZSERSSIFE", operation=Operation.DECRYPT, shift=18
        )
        == "MATT IS SHORTER THAN AARON"
    )


def test_break_cipher():
    result = break_cipher("DSKKR JRJZFIKWIRKZSERSSIFE", get_dictionary())
    assert result["message"] == "MATT IS SHORTER THAN AARON"
    assert result["shift"] == 18


def test_encrypt_invalid_message():
    with pytest.raises(InvalidCharacterException) as _:
        assert caesar_cipher("a", operation=Operation.ENCRYPT, shift=3)
