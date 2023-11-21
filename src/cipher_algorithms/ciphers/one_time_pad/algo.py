from cipher_algorithms.helpers.char_conversion_27 import InvalidCharacterException


def one_time_pad_char(input, key):
    if ord(input) < ord("A") or ord(input) > ord("Z"):
        raise InvalidCharacterException(char=input)
    if ord(key) < ord("A") or ord(key) > ord("Z"):
        raise InvalidCharacterException(char=key)

    i = ord(input) - ord("A")
    offset = (i + ord(key) - ord("A")) % 26
    new_char = chr(ord("Z") - offset)
    return new_char


def print_row(char):
    source_char = ""
    new_char = ""
    for i in range(26):
        new_source_char = chr(i + ord("A"))
        source_char += new_source_char

        nc = one_time_pad_char(new_source_char, char)
        new_char += nc
    return {"source": source_char, "new_char": new_char}


def one_time_pad(input, key_with_spaces):
    key = key_with_spaces.replace(" ", "")
    res = ""
    for i in range(len(input)):
        res += one_time_pad_char(input[i], key[i % len(key)])
    return res
