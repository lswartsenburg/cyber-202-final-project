from cipher_algorithms.ciphers import cipher_abc
from . import algo

# polybius
# Polybius


class Polybius(cipher_abc.Cipher):
    def __init__(self, args):
        if args.operation == "encrypt":
            Polybius.encrypt(message=args.message)
        elif args.operation == "decrypt":
            Polybius.decrypt(cipher=args.cipher)

    def encrypt(message):
        cipher = algo.encrypt_polybius(
            message,
        )
        print(f"The message {message} encrypted to {cipher}")

    def decrypt(cipher):
        message = algo.decrypt_polybius(
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

    def decrypt_arg_parser(parser):
        parser.add_argument(
            "--cipher",
            type=str,
            required=True,
            help="The message that needs to be encrypted",
        )

    def cipher_arg_parser(parser):
        subparsers = parser.add_subparsers(help="sub-command help", dest="operation")
        subparsers.required = True

        encrypt_parser = subparsers.add_parser(
            "encrypt", help="Encrypt Polybius cipher help"
        )
        encrypt_parser.set_defaults(operation="encrypt")
        Polybius.encrypt_arg_parser(encrypt_parser)

        decrypt_parser = subparsers.add_parser(
            "decrypt", help="Decrypt Polybius cipher help"
        )
        decrypt_parser.set_defaults(operation="decrypt")
        Polybius.decrypt_arg_parser(decrypt_parser)

        return parser
