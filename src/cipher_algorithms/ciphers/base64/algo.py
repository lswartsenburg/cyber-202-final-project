def encrypt(input_string):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    binary_string = "".join(format(ord(char), "08b") for char in input_string)

    while len(binary_string) % 6 != 0:
        binary_string += "0"

    six_bit_chunks = [binary_string[i : i + 6] for i in range(0, len(binary_string), 6)]

    base64_result = "".join(base64_chars[int(chunk, 2)] for chunk in six_bit_chunks)

    padding = len(binary_string) % 24
    if padding:
        base64_result += "=" * (4 - padding // 6)

    return base64_result


def decrypt(encoded_string):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    base64_mapping = {
        char: format(index, "06b") for index, char in enumerate(base64_chars)
    }

    encoded_string = encoded_string.rstrip("=")

    binary_string = "".join(base64_mapping[char] for char in encoded_string)

    eight_bit_chunks = [
        binary_string[i : i + 8] for i in range(0, len(binary_string), 8)
    ]

    decoded_result = "".join(chr(int(chunk, 2)) for chunk in eight_bit_chunks)

    return decoded_result


if __name__ == "__main__":
    print("ENCODE")
    input_string = "testingabc"
    encoded_string = encrypt(input_string)
    print("Original String:", input_string)
    print("Base64 Encoded:", encoded_string)

    print()
    print("DECODE")
    decoded_string = decrypt(encoded_string)
    print("Base64 Encoded:", encoded_string)
    print("Decoded String:", decoded_string)
