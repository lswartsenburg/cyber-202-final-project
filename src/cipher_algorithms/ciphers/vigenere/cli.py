from cipher_algorithms.ciphers import cipher_abc
from . import algo


class Vigenere(cipher_abc.Cipher):
    def __init__(self, args):
        if args.operation == "encrypt":
            Vigenere.encrypt(message=args.message, key=args.key)
        elif args.operation == "decrypt":
            Vigenere.decrypt(cipher=args.cipher, key=args.key)

    def encrypt(message, key):
        cipher = algo.vigenere(
            message,
            operation=algo.Operation.ENCRYPT,
            key=key,
        )
        print(f"The message {message} encrypted to {cipher}")

    def decrypt(cipher, key):
        message = algo.vigenere(
            cipher,
            operation=algo.Operation.DECRYPT,
            key=key,
        )
        print(f"Cipher {cipher} decrypted to {message}")

    def encrypt_arg_parser(parser):
        parser.add_argument(
            "--message",
            type=str,
            required=True,
            help="The message that needs to be encrypted",
        )
        parser.add_argument(
            "--key",
            type=str,
            required=True,
            help="The key to encrypt the message with",
        )

    def decrypt_arg_parser(parser):
        parser.add_argument(
            "--cipher",
            type=str,
            required=True,
            help="The message that needs to be encrypted",
        )
        parser.add_argument(
            "--key",
            type=str,
            required=True,
            help="The key to decrypt the message with",
        )

    def cipher_arg_parser(parser):
        subparsers = parser.add_subparsers(help="sub-command help", dest="operation")
        subparsers.required = True

        encrypt_parser = subparsers.add_parser(
            "encrypt", help="Encrypt vigenere cipher help"
        )
        encrypt_parser.set_defaults(operation="encrypt")
        Vigenere.encrypt_arg_parser(encrypt_parser)

        decrypt_parser = subparsers.add_parser(
            "decrypt", help="Decrypt vigenere cipher help"
        )
        decrypt_parser.set_defaults(operation="decrypt")
        Vigenere.decrypt_arg_parser(decrypt_parser)

        return parser
