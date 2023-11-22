from cipher_algorithms.ciphers import cipher_abc
from . import algo
import json


class HomophonicSubstitutionCLI(cipher_abc.Cipher):
    def __init__(self, args):
        key_dict = None
        if args.key is not None:
            key_dict = json.loads(args.key)

        if args.operation == "encrypt":
            HomophonicSubstitutionCLI.encrypt(message=args.message, key=key_dict)
        elif args.operation == "decrypt":
            HomophonicSubstitutionCLI.decrypt(cipher=args.cipher, key=key_dict)

    def encrypt(message, key):
        """
        python -m cipher_algorithms homophonic_substitution encrypt --message "TEST THIS MESSAGE" --key "{\"A\":[\"21\",\"27\",\"31\",\"40\"],\"B\":[\"15\"],\"C\":[\"01\",\"33\"],\"D\":[\"20\",\"34\"],\"E\":[\"22\",\"28\",\"32\",\"36\",\"37\"],\"F\":[\"05\"],\"G\":[\"17\"],\"H\":[\"14\"],\"I\":[\"02\",\"29\",\"38\",\"41\"],\"J\":[\"19\"],\"K\":[\"03\"],\"L\":[\"07\",\"39\",\"42\"],\"M\":[\"09\",\"43\"],\"N\":[\"12\",\"48\",\"97\"],\"O\":[\"18\",\"60\",\"85\"],\"P\":[\"26\",\"44\"],\"Q\":[\"25\"],\"R\":[\"24\",\"49\"],\"S\":[\"10\",\"30\",\"45\",\"99\"],\"T\":[\"06\",\"96\",\"55\"],\"U\":[\"16\",\"94\"],\"V\":[\"23\"],\"W\":[\"13\"],\"X\":[\"11\"],\"Y\":[\"08\"],\"Z\":[\"04\"]}"
        """
        cipher_obj = algo.HomophonicSubstitution(key)
        cipher = cipher_obj.encrypt(message)
        print(f"The message {message} encrypted to {cipher}")

    def decrypt(cipher, key):
        """
        python -m cipher_algorithms homophonic_substitution decrypt --cipher "06363055 55144130 43364510271722" --key "{\"A\":[\"21\",\"27\",\"31\",\"40\"],\"B\":[\"15\"],\"C\":[\"01\",\"33\"],\"D\":[\"20\",\"34\"],\"E\":[\"22\",\"28\",\"32\",\"36\",\"37\"],\"F\":[\"05\"],\"G\":[\"17\"],\"H\":[\"14\"],\"I\":[\"02\",\"29\",\"38\",\"41\"],\"J\":[\"19\"],\"K\":[\"03\"],\"L\":[\"07\",\"39\",\"42\"],\"M\":[\"09\",\"43\"],\"N\":[\"12\",\"48\",\"97\"],\"O\":[\"18\",\"60\",\"85\"],\"P\":[\"26\",\"44\"],\"Q\":[\"25\"],\"R\":[\"24\",\"49\"],\"S\":[\"10\",\"30\",\"45\",\"99\"],\"T\":[\"06\",\"96\",\"55\"],\"U\":[\"16\",\"94\"],\"V\":[\"23\"],\"W\":[\"13\"],\"X\":[\"11\"],\"Y\":[\"08\"],\"Z\":[\"04\"]}"
        """
        cipher_obj = algo.HomophonicSubstitution(key)
        message = cipher_obj.decrypt(cipher)
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
            help="The key in JSON format to decrypt the message with",
        )

    def cipher_arg_parser(parser):
        subparsers = parser.add_subparsers(help="sub-command help", dest="operation")
        subparsers.required = True

        encrypt_parser = subparsers.add_parser(
            "encrypt", help="Encrypt Homophonic Substitution cipher help"
        )
        encrypt_parser.set_defaults(operation="encrypt")
        HomophonicSubstitutionCLI.encrypt_arg_parser(encrypt_parser)

        decrypt_parser = subparsers.add_parser(
            "decrypt", help="Decrypt Homophonic Substitution cipher help"
        )
        decrypt_parser.set_defaults(operation="decrypt")
        HomophonicSubstitutionCLI.decrypt_arg_parser(decrypt_parser)

        return parser
