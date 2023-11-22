import random
from cipher_algorithms.helpers.char_conversion_27 import InvalidCharacterException

DEFAULT_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class WrongSizeKeyException(Exception):
    def __init__(self, key, chars):
        message = f"""
The length of the key needs to match the number of characters the substitution cipher supports. Compare the key lenght with the characters supporter:
{key}
{chars}
        """
        super().__init__(message)


class DuplicateCharactersException(Exception):
    def __init__(self, char):
        message = f"""
The key needs to consist out of unique characters. We found a duplicate character {char}
        """
        super().__init__(message)


class MonoAlphabeticSubstitution:
    def __init__(self, key=None):
        self.supported_chars = DEFAULT_CHARS
        self._unique_key = set([])

        if key is not None:
            if len(key) != len(self.supported_chars):
                raise WrongSizeKeyException(key, self.supported_chars)
            for c in key:
                if c in self._unique_key:
                    raise DuplicateCharactersException(c)
                else:
                    self._unique_key.add(c)
            self.key = [*key]

        else:
            self.key = self.generate_key()

        self.encrypt_map = {}
        self.decrypt_map = {}
        for i in range(len(self.key)):
            self.decrypt_map[self.key[i]] = self.supported_chars[i]
            self.encrypt_map[self.supported_chars[i]] = self.key[i]

    def generate_key(self):
        char_list = [*self.supported_chars]
        random.shuffle(char_list)
        return char_list

    def encrypt(self, message):
        result = ""
        for c in message:
            if c == " ":
                result += " "
            elif c not in self.encrypt_map:
                raise InvalidCharacterException(char=c)
            else:
                result += self.encrypt_map[c]
        return result

    def decrypt(self, cipher):
        result = ""
        for c in cipher:
            if c == " ":
                result += " "
            elif c not in self.decrypt_map:
                raise InvalidCharacterException(char=c)
            else:
                result += self.decrypt_map[c]
        return result
