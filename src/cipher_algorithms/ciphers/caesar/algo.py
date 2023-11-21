from enum import Enum
from cipher_algorithms.helpers.char_conversion_27 import char_from_int, int_from_char


class Operation(Enum):
    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"


def caesar_cipher(input_value, operation, shift):
    if operation not in (Operation.ENCRYPT, Operation.DECRYPT):
        raise Exception(f"This function does not support operation {operation}")

    cipher = ""
    for c in input_value:
        # We can't just use ord, because we need to take the space character into account
        char_int_value = int_from_char(c)

        # This is the "encryption" and "decryption
        new_int_value = (
            (char_int_value + shift) % 27
            if operation == Operation.ENCRYPT
            else (char_int_value - shift) % 27
        )

        cipher += char_from_int(new_int_value)
    return cipher


def break_cipher(cipher, dictionary):
    highest_score = 0
    highest_score_shift = None

    for i in range(27):
        current_score = 0
        potential_message = caesar_cipher(cipher, shift=i, operation=Operation.DECRYPT)
        words_potential_message = potential_message.split(" ")
        for word in words_potential_message:
            if word.lower() in dictionary:
                current_score += 1
        if current_score > highest_score:
            highest_score = current_score
            highest_score_shift = i
    if highest_score == 0:
        raise Exception(f'Could not break cipher of "{cipher}"')

    return {
        "shift": highest_score_shift,
        "message": caesar_cipher(
            cipher, shift=highest_score_shift, operation=Operation.DECRYPT
        ),
    }
