from cipher_algorithms.ciphers import cipher_abc
from . import algo


class OneTimePad(cipher_abc.Cipher):
    def __init__(self, args):
        if args.operation == "encrypt":
            OneTimePad.encrypt(message=args.message, key_with_spaces=args.key)
        elif args.operation == "decrypt":
            OneTimePad.decrypt(cipher=args.cipher, key_with_spaces=args.key)

    def encrypt(message, key_with_spaces):
        cipher = algo.one_time_pad(
            message,
            key_with_spaces=key_with_spaces,
        )
        print(f"The message {message} encrypted to {cipher}")

    def decrypt(cipher, key_with_spaces):
        message = algo.one_time_pad(
            cipher,
            key_with_spaces=key_with_spaces,
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
            "encrypt", help="Encrypt One Time Pad cipher help"
        )
        encrypt_parser.set_defaults(operation="encrypt")
        OneTimePad.encrypt_arg_parser(encrypt_parser)

        decrypt_parser = subparsers.add_parser(
            "decrypt", help="Decrypt One Time Pad cipher help"
        )
        decrypt_parser.set_defaults(operation="decrypt")
        OneTimePad.decrypt_arg_parser(decrypt_parser)

        return parser
