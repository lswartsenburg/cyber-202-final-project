import pytest

from cipher_algorithms.ciphers.one_time_pad.algo import one_time_pad
from cipher_algorithms.helpers.char_conversion_27 import InvalidCharacterException


def test_encrypt_valid_messages():
    assert one_time_pad("PEACE", key_with_spaces="LFNNY") == "ZQMKX"


def test_decrypt_valid_messages():
    assert one_time_pad("ZQMKX", key_with_spaces="LFNNY") == "PEACE"


def test_encrypt_invalid_message():
    with pytest.raises(InvalidCharacterException) as _:
        assert one_time_pad("a", key_with_spaces="TEST")

    with pytest.raises(InvalidCharacterException) as _:
        assert one_time_pad("A", key_with_spaces="test")
