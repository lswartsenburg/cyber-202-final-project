from cipher_algorithms.ciphers import cipher_abc
from . import algo


class MonoAlphabeticSubstitutionCLI(cipher_abc.Cipher):
    def __init__(self, args):
        if args.operation == "encrypt":
            MonoAlphabeticSubstitutionCLI.encrypt(message=args.message, key=args.key)
        elif args.operation == "decrypt":
            MonoAlphabeticSubstitutionCLI.decrypt(cipher=args.cipher, key=args.key)

    def encrypt(message, key):
        cipher_obj = algo.MonoAlphabeticSubstitution(key)
        cipher = cipher_obj.encrypt(message)
        print(
            f"The message {message} encrypted to {cipher} using the key {''.join(cipher_obj.key)}"
        )

    def decrypt(cipher, key):
        cipher_obj = algo.MonoAlphabeticSubstitution(key)
        message = cipher_obj.decrypt(cipher)
        print(
            f"Cipher {cipher} decrypted to {message} using the key {''.join(cipher_obj.key)}"
        )

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
            help="The key to encrypt the message with. If no key is set, a random one will be generated",
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
            "encrypt", help="Encrypt MonoAlphabeticSubstitution cipher help"
        )
        encrypt_parser.set_defaults(operation="encrypt")
        MonoAlphabeticSubstitutionCLI.encrypt_arg_parser(encrypt_parser)

        decrypt_parser = subparsers.add_parser(
            "decrypt", help="Decrypt MonoAlphabeticSubstitution cipher help"
        )
        decrypt_parser.set_defaults(operation="decrypt")
        MonoAlphabeticSubstitutionCLI.decrypt_arg_parser(decrypt_parser)

        return parser
