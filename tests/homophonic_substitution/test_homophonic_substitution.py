# cipher_algo = FractionedMorseCipher(key="CROWDED")
# result = cipher_algo.encrypt("NOBODY GOES THERE ANY MORE BECAUSE ITS TOO CROWDED ")
# message = cipher_algo.decrypt(result["cipher"])

import pytest

from cipher_algorithms.ciphers.homophonic_substitution.algo import (
    HomophonicSubstitution,
    EncryptionMethod,
    UnknowCharacterException,
    IncorrectCipherLengthException,
)
from cipher_algorithms.helpers.char_conversion_27 import InvalidCharacterException


def test_encrypt_valid_messages():
    homophonic_substitution = HomophonicSubstitution()
    assert (
        homophonic_substitution.encrypt(
            message="TEST THIS MESSAGE", method=EncryptionMethod.ROTATE
        )
        == "06221055 96140299 09374530211736"
    )


def test_decrypt_valid_messages():
    homophonic_substitution = HomophonicSubstitution()
    assert (
        homophonic_substitution.decrypt(cipher="06363055 55144130 43364510271722")
        == "TEST THIS MESSAGE"
    )


def test_encrypt_invalid_message():
    homophonic_substitution = HomophonicSubstitution()
    with pytest.raises(UnknowCharacterException) as _:
        assert homophonic_substitution.encrypt("###")
    with pytest.raises(IncorrectCipherLengthException) as _:
        assert homophonic_substitution.decrypt("###")
