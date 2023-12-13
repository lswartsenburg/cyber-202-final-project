from cipher_algorithms.ciphers import cipher_abc
from .algo import FractionedMorseCipher
from cipher_algorithms.helpers import dictionary


class FractionalMorseCLI(cipher_abc.Cipher):
    def __init__(self, args):
        if args.operation == "encrypt":
            FractionalMorseCLI.encrypt(message=args.message, key=args.key)
        elif args.operation == "decrypt":
            FractionalMorseCLI.decrypt(cipher=args.cipher, key=args.key)

    def encrypt(message, key):
        fractional_morse = FractionedMorseCipher(key=key)
        cipher = fractional_morse.encrypt(
            message,
        )
        print(f"The message {message} encrypted to {cipher}")

    def decrypt(cipher, key):
        fractional_morse = FractionedMorseCipher(key=key)
        message = fractional_morse.decrypt(
            cipher,
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
            help="The key to decrypt the message with",
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
            "encrypt", help="Encrypt caesar cipher help"
        )
        encrypt_parser.set_defaults(operation="encrypt")
        FractionalMorseCLI.encrypt_arg_parser(encrypt_parser)

        decrypt_parser = subparsers.add_parser(
            "decrypt", help="Decrypt caesar cipher help"
        )
        decrypt_parser.set_defaults(operation="decrypt")
        FractionalMorseCLI.decrypt_arg_parser(decrypt_parser)

        return parser
