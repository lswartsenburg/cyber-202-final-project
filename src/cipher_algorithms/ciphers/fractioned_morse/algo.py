from enum import Enum
from cipher_algorithms.helpers.char_conversion_27 import InvalidCharacterException


class Operation(Enum):
    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"


MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    " ": "|",
}

# We can do this more efficiently, but Im lazy
MORSE_TABLE = """
.........---------xxxxxxxx
...---xxx...---xxx...---xx
.-x.-x.-x.-x.-x.-x.-x.-x.-
"""


class FractionedMorseCipher:
    def __init__(self, key):
        for c in key:
            if ord(c) < ord("A") or ord(c) > ord("Z"):
                raise InvalidCharacterException(char=c)
        self.keyed_alphabet = self._get_keyed_alphabet(key)
        self.morse_to_char = self._get_morse_to_char_map(self.keyed_alphabet)
        self.reverse_morse_to_char = {v: k for k, v in self.morse_to_char.items()}

    def _get_morse_to_char_map(self, keyed_alphabet):
        morse_dict = {}
        morse_lines = MORSE_TABLE.strip().splitlines()
        for i, c in enumerate(keyed_alphabet):
            morse_tri = ""
            for line in morse_lines:
                morse_tri += line[i]
            morse_dict[morse_tri] = c
        return morse_dict

    def _get_keyed_alphabet(self, key):
        abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        key_chars = [*(key + abc)]
        found_chars = set([])
        keyed_alphabet = ""
        for c in key_chars:
            if c not in found_chars:
                keyed_alphabet += c
                found_chars.add(c)
        return keyed_alphabet

    def _word_to_morse(self, word):
        chars = [*word]
        chars_in_morse = []
        for c in chars:
            chars_in_morse.append(MORSE_CODE_DICT[c])
        return "x".join(chars_in_morse)

    def _to_morse(self, sentence):
        words = sentence.split(" ")
        words_in_morse = []
        for word in words:
            words_in_morse.append(self._word_to_morse(word))
        return "xx".join(words_in_morse)

    def _pad_morse(self, intermediate_morse):
        add_xs = len(intermediate_morse) % 3
        result = "" + intermediate_morse
        if add_xs == 0:
            return intermediate_morse
        else:
            for _ in range(3 - add_xs):
                result += "x"
        return result

    def _intermediate_morse_to_cipher(self, intermediate_morse):
        if len(intermediate_morse) == 0:
            return ""
        padded_morse = self._pad_morse(intermediate_morse)
        result = ""
        for i in range(int(len(padded_morse) / 3)):
            start_index = i * 3
            morse_code = padded_morse[start_index : start_index + 3]
            result += self.morse_to_char[morse_code]
        return result

    def encrypt(self, message):
        intermediate_morse = self._to_morse(message.strip())
        cipher = self._intermediate_morse_to_cipher(intermediate_morse)
        return {"cipher": cipher, "intermediate_morse": f"{intermediate_morse}"}

    def _cipher_to_intermediate_morse(self, cipher):
        intermediate_morse = ""
        for c in cipher:
            if ord(c) < ord("A") or ord(c) > ord("Z"):
                raise InvalidCharacterException(char=c)
            else:
                intermediate_morse += self.reverse_morse_to_char[c]
        return intermediate_morse

    def decrypt(self, cipher):
        intermediate_morse_with_padding = self._cipher_to_intermediate_morse(cipher)
        intermediate_morse = intermediate_morse_with_padding.rstrip("x")
        morse_words = intermediate_morse.split("xx")
        reverse_morse_code_dict = {v: k for k, v in MORSE_CODE_DICT.items()}

        result = ""
        for morse_word in morse_words:
            morse_chars = morse_word.split("x")
            for morse_char in morse_chars:
                result += reverse_morse_code_dict[morse_char]
            result += " "

        return {
            "message": result.strip(),
            "intermediate_morse": f"{intermediate_morse}",
        }


if __name__ == "__main__":
    morse = FractionedMorseCipher("KEYWORD")
    cipher = morse.encrypt("HELLO")
    print(cipher)

    message = morse.decrypt(cipher["cipher"])
    print(message)
