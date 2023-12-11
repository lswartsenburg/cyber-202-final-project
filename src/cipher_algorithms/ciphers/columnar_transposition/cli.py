from cipher_algorithms.ciphers import cipher_abc
from . import algo


class ColumnarTransposition(cipher_abc.Cipher):
    def __init__(self, args):
        if args.operation == "encrypt":
            ColumnarTransposition.encrypt(message=args.message, keyword=args.key)
        elif args.operation == "decrypt":
            ColumnarTransposition.decrypt(cipher=args.cipher, keyword=args.key)

    def encrypt(message, keyword):
        cipher = algo.encryptMessage(
            message,
            key=keyword,
        )
        print(f"The message {message} encrypted to {cipher}")

    def decrypt(cipher, keyword):
        message = algo.decryptMessage(
            cipher,
            key=keyword,
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
            "encrypt", help="Encrypt Columnar Transposition cipher help"
        )
        encrypt_parser.set_defaults(operation="encrypt")
        ColumnarTransposition.encrypt_arg_parser(encrypt_parser)

        decrypt_parser = subparsers.add_parser(
            "decrypt", help="Decrypt Columnar Transposition cipher help"
        )
        decrypt_parser.set_defaults(operation="decrypt")
        ColumnarTransposition.decrypt_arg_parser(decrypt_parser)

        return parser
