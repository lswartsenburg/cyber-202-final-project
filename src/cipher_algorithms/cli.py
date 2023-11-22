import argparse
from cipher_algorithms.ciphers.caesar.cli import Caesar
from cipher_algorithms.ciphers.vigenere.cli import Vigenere
from cipher_algorithms.ciphers.one_time_pad.cli import OneTimePad
from cipher_algorithms.ciphers.fractioned_morse.cli import FractionalMorseCLI
from cipher_algorithms.ciphers.mono_alphabetic_substitution.cli import (
    MonoAlphabeticSubstitutionCLI,
)
from cipher_algorithms.ciphers.homophonic_substitution.cli import (
    HomophonicSubstitutionCLI,
)


active_ciphers = {
    "caesar": Caesar,
    "vigenere": Vigenere,
    "one_time_pad": OneTimePad,
    "fractioned_morse": FractionalMorseCLI,
    "mono_alphabetic_substitution": MonoAlphabeticSubstitutionCLI,
    "homophonic_substitution": HomophonicSubstitutionCLI,
}


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
