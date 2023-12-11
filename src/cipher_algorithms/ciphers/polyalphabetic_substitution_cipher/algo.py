class CipherError(Exception):
    """Custom exception for cipher errors."""

    pass


def validate_input(text, keyword):
    if not text or not keyword:
        raise CipherError("Text and keyword must not be empty.")

    if not text.isalpha() or not keyword.isalpha():
        raise CipherError("Text and keyword must only contain alphabetic characters.")


def generate_key(plaintext, keyword):
    return (keyword * (len(plaintext) // len(keyword))) + keyword[
        : len(plaintext) % len(keyword)
    ]


def encrypt(text, keyword):
    validate_input(text, keyword)
    key = generate_key(text, keyword)
    result = ""

    for p, k in zip(text, key):
        shift = ord("A") - (ord(k.upper()) - ord("A"))
        result += chr((ord(p.upper()) + shift) % 26 + ord("A"))

    return result


def decrypt(text, keyword):
    # As the Beaufort Cipher uses the same process for encryption and decryption,
    # the decrypt function is identical to the encrypt function.
    return encrypt(text, keyword)


# Example usage
if __name__ == "__main__":
    try:
        plaintext = "HELLOWORLD"
        keyword = "KEY"
        encrypted_text = encrypt(plaintext, keyword)
        decrypted_text = decrypt(encrypted_text, keyword)

        print(f"Plaintext: {plaintext}")
        print(f"Encrypted: {encrypted_text}")
        print(f"Decrypted: {decrypted_text}")
    except CipherError as e:
        print(f"Error: {e}")
