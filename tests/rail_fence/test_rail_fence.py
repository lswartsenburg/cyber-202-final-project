from cipher_algorithms.ciphers.rail_fence.algo import encryptRailFence, decryptRailFence


def test_encrypt_valid_messages():
    plaintext = "QUICK BROWN FOX JUMPS"
    key = 2
    expected_cipher = "Q UFIOCXK  JBURMOPWSN"
    assert encryptRailFence(plaintext, key) == expected_cipher


def test_decrypt_valid_messages():
    plaintext = "QUICK BROWN FOX JUMPS"
    expected_cipher = "Q UFIOCXK  JBURMOPWSN"
    key = 2
    assert decryptRailFence(expected_cipher, key) == plaintext
