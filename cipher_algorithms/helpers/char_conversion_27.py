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
