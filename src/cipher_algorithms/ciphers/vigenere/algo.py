from enum import Enum
from cipher_algorithms.helpers.char_conversion_27 import char_from_int, int_from_char
from cipher_algorithms.helpers.common_exceptions import UnsupporterOperationException


class Operation(Enum):
    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"


def vigenere(input, key, operation):
    if operation not in (Operation.ENCRYPT, Operation.DECRYPT):
        raise UnsupporterOperationException(operation=operation, function="vigenere")

    result = ""
    for i, input_char in enumerate(input):
        key_char = key[i % len(key)]
        key_char_int = int_from_char(key_char)
        input_char_int = int_from_char(input_char)

        # print(key_char_int, input_char_int)

        result_char_int = (
            key_char_int + input_char_int
            if operation == Operation.ENCRYPT
            else input_char_int - key_char_int
        )
        result += char_from_int(result_char_int % 27)
    return result
