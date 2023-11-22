# cipher_algo = FractionedMorseCipher(key="CROWDED")
# result = cipher_algo.encrypt("NOBODY GOES THERE ANY MORE BECAUSE ITS TOO CROWDED ")
# message = cipher_algo.decrypt(result["cipher"])

import pytest

from cipher_algorithms.ciphers.mono_alphabetic_substitution.algo import (
    MonoAlphabeticSubstitution,
    DEFAULT_CHARS,
)
from cipher_algorithms.helpers.char_conversion_27 import InvalidCharacterException


def test_encrypt_valid_messages():
    fractioned_morse = MonoAlphabeticSubstitution(key=DEFAULT_CHARS[::-1])
    assert (
        fractioned_morse.encrypt(
            message="NOBODY GOES THERE ANY MORE BECAUSE ITS TOO CROWDED"
        )
        == "MLYLWB TLVH GSVIV ZMB NLIV YVXZFHV RGH GLL XILDWVW"
    )


# def test_decrypt_valid_messages():
#     fractioned_morse = FractionedMorseCipher(key="CROWDED")
#     assert (
#         fractioned_morse.decrypt(
#             cipher="IKUOKUBDZIKTCZQOAIFEIHPLKSAZCTHAMECTQXCZVNLUIWVMLGTG"
#         )["message"]
#         == "NOBODY GOES THERE ANY MORE BECAUSE ITS TOO CROWDED"
#     )


def test_encrypt_invalid_message():
    fractioned_morse = MonoAlphabeticSubstitution(key=DEFAULT_CHARS[::-1])
    with pytest.raises(InvalidCharacterException) as _:
        assert fractioned_morse.encrypt("###")
    with pytest.raises(InvalidCharacterException) as _:
        assert fractioned_morse.decrypt("###")
