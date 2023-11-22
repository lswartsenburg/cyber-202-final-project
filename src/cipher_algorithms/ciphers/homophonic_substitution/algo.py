import random

DEFAULT_KEY = {
    "A": ["21", "27", "31", "40"],
    "B": ["15"],
    "C": ["01", "33"],
    "D": ["20", "34"],
    "E": ["22", "28", "32", "36", "37"],
    "F": ["05"],
    "G": ["17"],
    "H": ["14"],
    "I": ["02", "29", "38", "41"],
    "J": ["19"],
    "K": ["03"],
    "L": ["07", "39", "42"],
    "M": ["09", "43"],
    "N": ["12", "48", "97"],
    "O": ["18", "60", "85"],
    "P": ["26", "44"],
    "Q": ["25"],
    "R": ["24", "49"],
    "S": ["10", "30", "45", "99"],
    "T": ["06", "96", "55"],
    "U": ["16", "94"],
    "V": ["23"],
    "W": ["13"],
    "X": ["11"],
    "Y": ["08"],
    "Z": ["04"],
}

from enum import Enum
from cipher_algorithms.helpers.char_conversion_27 import char_from_int, int_from_char


class EncryptionMethod(Enum):
    ROTATE = "rotate"
    RANDOM = "random"


class DuplicateValuesInKeyException(Exception):
    def __init__(self, value, first_char, second_char):
        message = f"""
There is a duplicate value in the key. Value {value} maps both to {first_char} and {second_char}
        """
        super().__init__(message)


class IncorrectLengthValueException(Exception):
    def __init__(self, value):
        message = f"""
The values for each key need to be exactly 2 characters long. We found a value {value} that did not meet that requirement.
        """
        super().__init__(message)


class IncorrectCharLength(Exception):
    def __init__(self, value):
        message = f"""
The character in the key need to be lenght 1. This character {value} did not meet that requirement.
        """
        super().__init__(message)


class IncorrectCipherLengthException(Exception):
    def __init__(self, word):
        message = f"""
The words in the Cipher needs to have an even number of characters. The given word {word} in the cipher has {len(word)} characters.
        """
        super().__init__(message)


class UnknowCharacterException(Exception):
    def __init__(self, message, char):
        message = f"""
The {message} contains a char {char} that is not in the key
        """
        super().__init__(message)


class UnknowValueException(Exception):
    def __init__(self, chipher, value):
        message = f"""
The {chipher} contains a char {value} that is not in the key
        """
        super().__init__(message)


class HomophonicSubstitution:
    def __init__(self, key=None):
        self.key = key or DEFAULT_KEY
        self.reverse_key = {}
        for char, values in self.key.items():
            for value in values:
                if value in self.reverse_key:
                    raise DuplicateValuesInKeyException(
                        value, self.reverse_key[value], char
                    )
                elif len(value) != 2:
                    raise IncorrectLengthValueException(value)
                elif len(char) != 1:
                    raise IncorrectCharLength(char)
                else:
                    self.reverse_key[value] = char

    def _rotate_key(self, c):
        self.key[c] = self.key[c][-1:] + self.key[c][:-1]

    def encrypt(self, message, method=EncryptionMethod.RANDOM):
        result = ""
        for c in message:
            if c == " ":
                result += " "
            elif c not in self.key:
                raise UnknowCharacterException(message, c)
            else:
                value_list = self.key[c]
                if method == EncryptionMethod.RANDOM:
                    rand_idx = random.randrange(len(value_list))
                    value = value_list[rand_idx]
                    result += value
                elif method == EncryptionMethod.ROTATE:
                    value = value_list[0]
                    self._rotate_key(c)
                    result += value
                else:
                    raise Exception("Invalid encryption method give")
        return result

    def decrypt(self, cipher):
        cipher_words = cipher.split(" ")
        words = []
        for cipher_word in cipher_words:
            word = ""
            if len(cipher_word) % 2 != 0:
                raise IncorrectCipherLengthException(cipher_word)

            for i in range(int(len(cipher_word) / 2)):
                value = cipher_word[i * 2] + cipher_word[i * 2 + 1]
                if value not in self.reverse_key:
                    raise UnknowValueException(cipher, value)
                else:
                    word += self.reverse_key[value]
            words.append(word)

        return " ".join(words)


# c = HomophonicSubstitution()
# print(c.encrypt("TEST THIS MESSAGE", EncryptionMethod.ROTATE))

# print(c.decrypt("06281055 55140245 09374530311732"))
