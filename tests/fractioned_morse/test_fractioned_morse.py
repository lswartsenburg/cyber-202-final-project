# cipher_algo = FractionedMorseCipher(key="CROWDED")
# result = cipher_algo.encrypt("NOBODY GOES THERE ANY MORE BECAUSE ITS TOO CROWDED ")
# message = cipher_algo.decrypt(result["cipher"])

import pytest

from cipher_algorithms.ciphers.fractioned_morse.algo import (
    FractionedMorseCipher,
)
from cipher_algorithms.helpers.char_conversion_27 import InvalidCharacterException


def test_encrypt_valid_messages():
    fractioned_morse = FractionedMorseCipher(key="CROWDED")
    assert (
        fractioned_morse.encrypt(
            message="NOBODY GOES THERE ANY MORE BECAUSE ITS TOO CROWDED"
        )["cipher"]
        == "IKUOKUBDZIKTCZQOAIFEIHPLKSAZCTHAMECTQXCZVNLUIWVMLGTG"
    )


def test_decrypt_valid_messages():
    fractioned_morse = FractionedMorseCipher(key="CROWDED")
    assert (
        fractioned_morse.decrypt(
            cipher="IKUOKUBDZIKTCZQOAIFEIHPLKSAZCTHAMECTQXCZVNLUIWVMLGTG"
        )["message"]
        == "NOBODY GOES THERE ANY MORE BECAUSE ITS TOO CROWDED"
    )


def test_encrypt_invalid_message():
    with pytest.raises(InvalidCharacterException) as _:
        assert FractionedMorseCipher(key="sdf#23")
