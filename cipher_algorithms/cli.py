import argparse
from cipher_algorithms.ciphers.caesar.cli import Caesar
from cipher_algorithms.ciphers.vigenere.cli import Vigenere


active_ciphers = {"caesar": Caesar, "vigenere": Vigenere}


def main():
    parser = argparse.ArgumentParser(
        prog="Cipher Algorithms",
        description="Implements various cipher algorithms",
        epilog="Thanks for trying our cipher algorithms",
    )

    subparsers = parser.add_subparsers(help="sub-command help", dest="cipher")
    subparsers.required = True

    for sub_parser_name, cipher in active_ciphers.items():
        sub_parser = subparsers.add_parser(
            sub_parser_name,
            help=f"Help text for the {sub_parser_name} cipher",
        )
        cipher.cipher_arg_parser(parser=sub_parser)
        sub_parser.set_defaults(cipher_class=cipher)

    args = parser.parse_args()

    cipher = args.cipher_class
    cipher(args)
