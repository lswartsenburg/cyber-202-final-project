def validate_input(text, keyword):
    if not isinstance(text, str) or not isinstance(keyword, str):
        raise ValueError("Both text and keyword should be strings.")

    if not text:
        raise ValueError("Text cannot be empty.")

    if not keyword.isalpha():
        raise ValueError("Keyword must only contain alphabetic characters.")

def generate_key(text, keyword):
    key = keyword.lower() * (len(text) // len(keyword)) + keyword.lower()[:len(text) % len(keyword)]
    return key

def encrypt(plaintext, keyword):
    validate_input(plaintext, keyword)
    key = generate_key(plaintext, keyword)
    encrypted = ""

    for p, k in zip(plaintext, key):
        if p.isalpha():
            shift = ord(k) - ord('a')
            encrypted += chr((ord(p.lower()) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted += p

    return encrypted

def decrypt(ciphertext, keyword):
    validate_input(ciphertext, keyword)
    key = generate_key(ciphertext, keyword)
    decrypted = ""

    for c, k in zip(ciphertext, key):
        if c.isalpha():
            shift = ord(k) - ord('a')
            decrypted += chr((ord(c.lower()) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted += c

    return decrypted

# Example usage
try:
    plaintext = "Hello, World!"
    keyword = "Key"
    encrypted_text = encrypt(plaintext, keyword)
    decrypted_text = decrypt(encrypted_text, keyword)

    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text}")
except ValueError as e:
    print(f"Error: {e}")
