import argparse

from cipher_algorithms.ciphers.base64.cli import Base64
from cipher_algorithms.ciphers.bifid_cipher.cli import Bifid
from cipher_algorithms.ciphers.caesar.cli import Caesar
from cipher_algorithms.ciphers.columnar_transposition.cli import ColumnarTransposition
from cipher_algorithms.ciphers.fractioned_morse.cli import FractionalMorseCLI
from cipher_algorithms.ciphers.hill.cli import Hill
from cipher_algorithms.ciphers.homophonic_substitution.cli import (
    HomophonicSubstitutionCLI,
)
from cipher_algorithms.ciphers.mono_alphabetic_substitution.cli import (
    MonoAlphabeticSubstitutionCLI,
)
from cipher_algorithms.ciphers.one_time_pad.cli import OneTimePad
from cipher_algorithms.ciphers.playfair.cli import Playfair
from cipher_algorithms.ciphers.polyalphabetic_substitution_cipher.cli import (
    PolyalphabeticSubstitution,
)
from cipher_algorithms.ciphers.polybius_cipher.cli import Polybius
from cipher_algorithms.ciphers.polygram_substitution_cipher.cli import (
    PolygramSubstitution,
)
from cipher_algorithms.ciphers.rail_fence.cli import RailFence
from cipher_algorithms.ciphers.vigenere.cli import Vigenere

active_ciphers = {
    "base64": Base64,
    "bifid": Bifid,
    "caesar": Caesar,
    "columnar_transposition": ColumnarTransposition,
    "fractioned_morse": FractionalMorseCLI,
    "hill": Hill,
    "homophonic_substitution": HomophonicSubstitutionCLI,
    "mono_alphabetic_substitution": MonoAlphabeticSubstitutionCLI,
    "one_time_pad": OneTimePad,
    "playfair": Playfair,
    "polyalphabetic_substitution": PolyalphabeticSubstitution,
    "polybius": Polybius,
    "polygram_substitution": PolygramSubstitution,
    "rail_fence": RailFence,
    "vigenere": Vigenere,
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
