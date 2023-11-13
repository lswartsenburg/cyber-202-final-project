from enum import Enum


class Operation(Enum):
    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"


class InvalidCharacterException(Exception):
    def __init__(self, char=None, int=None):
        message = f"""
The message must consist of all uppercase characters [A-Z] since the exercise
requires the use of mod 27 and the example is uses uppercase characters. Invalid input: {char or int}
        """
        super().__init__(message)


def int_from_char(c):
    if ord(c) >= ord("A") and ord(c) <= ord("Z"):
        return ord(c) - ord("A")
    elif c == " ":
        return 26
    else:
        raise InvalidCharacterException(char=c)


def char_from_int(i):
    if i == 26:
        return " "
    elif i >= 0 and i <= 25:
        return chr(i + ord("A"))
    else:
        raise InvalidCharacterException(int=i)


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
