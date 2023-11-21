from cipher_algorithms.ciphers import cipher_abc
from . import algo
from cipher_algorithms.helpers import dictionary


class Caesar(cipher_abc.Cipher):
    def __init__(self, args):
        if args.operation == "break":
            Caesar.break_cipher(cipher=args.cipher)
        elif args.operation == "encrypt":
            Caesar.encrypt(message=args.message, shift=args.shift)
        elif args.operation == "decrypt":
            Caesar.decrypt(cipher=args.cipher, shift=args.shift)

    def encrypt(message, shift):
        cipher = algo.caesar_cipher(
            message,
            operation=algo.Operation.ENCRYPT,
            shift=shift,
        )
        print(f"The message {message} encrypted to {cipher}")

    def decrypt(cipher, shift):
        message = algo.caesar_cipher(
            cipher,
            operation=algo.Operation.DECRYPT,
            shift=shift,
        )
        print(f"Cipher {cipher} decrypted to {message}")

    def break_cipher(cipher):
        words = dictionary.get_dictionary()
        result = algo.break_cipher(cipher, words)
        print(result)

    def break_arg_parser(parser):
        parser.add_argument(
            "--cipher",
            type=str,
            required=True,
            help="The message that needs to be encrypted",
        )

    def encrypt_arg_parser(parser):
        parser.add_argument(
            "--message",
            type=str,
            required=True,
            help="The message that needs to be encrypted",
        )
        parser.add_argument(
            "--shift",
            type=int,
            required=True,
            help="The number of positions the characters need to be shifted by",
        )

    def decrypt_arg_parser(parser):
        parser.add_argument(
            "--cipher",
            type=str,
            required=True,
            help="The message that needs to be encrypted",
        )
        parser.add_argument(
            "--shift",
            type=int,
            required=True,
            help="The number of positions the characters need to be shifted by",
        )

    def cipher_arg_parser(parser):
        subparsers = parser.add_subparsers(help="sub-command help", dest="operation")
        subparsers.required = True

        break_parser = subparsers.add_parser("break", help="Break Caesar cipher help")
        break_parser.set_defaults(operation="break")
        Caesar.break_arg_parser(break_parser)

        encrypt_parser = subparsers.add_parser(
            "encrypt", help="Encrypt caesar cipher help"
        )
        encrypt_parser.set_defaults(operation="encrypt")
        Caesar.encrypt_arg_parser(encrypt_parser)

        decrypt_parser = subparsers.add_parser(
            "decrypt", help="Decrypt caesar cipher help"
        )
        decrypt_parser.set_defaults(operation="decrypt")
        Caesar.decrypt_arg_parser(decrypt_parser)

        return parser
