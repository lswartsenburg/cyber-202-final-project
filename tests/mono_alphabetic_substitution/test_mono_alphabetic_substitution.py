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
    mono_alphabetic_substitution = MonoAlphabeticSubstitution(key=DEFAULT_CHARS[::-1])
    assert (
        mono_alphabetic_substitution.encrypt(
            message="NOBODY GOES THERE ANY MORE BECAUSE ITS TOO CROWDED"
        )
        == "MLYLWB TLVH GSVIV ZMB NLIV YVXZFHV RGH GLL XILDWVW"
    )


def test_decrypt_valid_messages():
    mono_alphabetic_substitution = MonoAlphabeticSubstitution(key=DEFAULT_CHARS[::-1])
    assert (
        mono_alphabetic_substitution.decrypt(
            cipher="IKUOKUBDZIKTCZQOAIFEIHPLKSAZCTHAMECTQXCZVNLUIWVMLGTG"
        )["message"]
        == "NOBODY GOES THERE ANY MORE BECAUSE ITS TOO CROWDED"
    )


def test_encrypt_invalid_message():
    mono_alphabetic_substitution = MonoAlphabeticSubstitution(key=DEFAULT_CHARS[::-1])
    with pytest.raises(InvalidCharacterException) as _:
        assert mono_alphabetic_substitution.encrypt("###")
    with pytest.raises(InvalidCharacterException) as _:
        assert mono_alphabetic_substitution.decrypt("###")
