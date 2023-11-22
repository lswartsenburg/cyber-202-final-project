# Chris Black - this is still WIP; will add more comments and tests.

# Define the substitution scheme
encryption_dict = {
    'AB': 'XY',
    'CD': 'ZQ',
    # Add more substitutions here
}

# Create a decryption dictionary from the encryption dictionary
decryption_dict = {v: k for k, v in encryption_dict.items()}

def encrypt(text):
    encrypted = ""
    for i in range(0, len(text), 2):
        digram = text[i:i+2]
        encrypted += encryption_dict.get(digram, digram)  # Default to original if not found
    return encrypted

def decrypt(text):
    decrypted = ""
    for i in range(0, len(text), 2):
        digram = text[i:i+2]
        decrypted += decryption_dict.get(digram, digram)  # Default to original if not found
    return decrypted

# Example usage
plaintext = "ABCD"
encrypted_text = encrypt(plaintext)
decrypted_text = decrypt(encrypted_text)

print(f"Plaintext: {plaintext}")
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")
