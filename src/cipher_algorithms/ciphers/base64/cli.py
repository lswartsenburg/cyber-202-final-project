from cipher_algorithms.ciphers import cipher_abc
from . import algo


class Base64(cipher_abc.Cipher):
    def __init__(self, args):
        if args.operation == "encrypt":
            Base64.encrypt(message=args.message)
        elif args.operation == "decrypt":
            Base64.decrypt(cipher=args.cipher)

    def encrypt(message):
        cipher = algo.encrypt(message)
        print(f"The message {message} encrypted to {cipher}")

    def decrypt(cipher):
        message = algo.decrypt(cipher)
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
            "encrypt", help="Encrypt Base64 cipher help"
        )
        encrypt_parser.set_defaults(operation="encrypt")
        Base64.encrypt_arg_parser(encrypt_parser)

        decrypt_parser = subparsers.add_parser(
            "decrypt", help="Decrypt Base64 cipher help"
        )
        decrypt_parser.set_defaults(operation="decrypt")
        Base64.decrypt_arg_parser(decrypt_parser)

        return parser
