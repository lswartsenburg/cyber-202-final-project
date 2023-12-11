from cipher_algorithms.ciphers import cipher_abc
from . import algo
import json


class PolygramSubstitution(cipher_abc.Cipher):
    def __init__(self, args):
        key = json.loads(args.key)

        if args.operation == "encrypt":
            PolygramSubstitution.encrypt(message=args.message, keyword=key)
        elif args.operation == "decrypt":
            PolygramSubstitution.decrypt(cipher=args.cipher, keyword=key)

    def encrypt(message, keyword):
        cipher = algo.encrypt(
            message,
            key=keyword,
        )
        print(f"The message {message} encrypted to {cipher}")

    def decrypt(cipher, keyword):
        message = algo.decrypt(
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
            required=False,
            help="The key to encrypt the message with as a json string",
        )

    def decrypt_arg_parser(parser):
        parser.add_argument(
            "--cipher",
            type=str,
            required=True,
            help="The message that needs to be encrypted as a json string",
        )
        parser.add_argument(
            "--key",
            type=str,
            required=False,
            help="The key to decrypt the message with",
        )

    def cipher_arg_parser(parser):
        subparsers = parser.add_subparsers(help="sub-command help", dest="operation")
        subparsers.required = True

        encrypt_parser = subparsers.add_parser(
            "encrypt", help="Encrypt Polygram Substitution cipher help"
        )
        encrypt_parser.set_defaults(operation="encrypt")
        PolygramSubstitution.encrypt_arg_parser(encrypt_parser)

        decrypt_parser = subparsers.add_parser(
            "decrypt", help="Decrypt Polygram Substitution cipher help"
        )
        decrypt_parser.set_defaults(operation="decrypt")
        PolygramSubstitution.decrypt_arg_parser(decrypt_parser)

        return parser
