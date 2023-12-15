from cipher_algorithms.ciphers.rail_fence.algo import encryptRailFence, decryptRailFence


def test_encrypt_valid_messages():
    plaintext = "the quick brown fox jumps over the lazy dog"
    key = 3
    expected_cipher = "tqkofjsehadh uc rw o up vrtelz oeibnxmo  yg"
    assert encryptRailFence(plaintext, key) == expected_cipher


def test_decrypt_valid_messages():
    plaintext = "the quick brown fox jumps over the lazy dog"
    key = 3
    expected_cipher = "tqkofjsehadh uc rw o up vrtelz oeibnxmo  yg"
    assert decryptRailFence(expected_cipher, key) == plaintext
