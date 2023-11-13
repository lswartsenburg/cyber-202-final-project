import argparse
from ciphers.caesar.main import Caesar


ciphers = {"caesar": Caesar}


def main():
    parser = argparse.ArgumentParser(
        prog="Cipher Algorithms",
        description="Implements various cipher algorithms",
        epilog="Thanks for trying our cipher algorithms",
    )

    subparsers = parser.add_subparsers(help="sub-command help", dest="cipher")
    subparsers.required = True

    for sub_parser_name, cipher in ciphers.items():
        sub_parser = subparsers.add_parser(
            sub_parser_name,
            help=f"Help text for the {sub_parser_name} cipher",
        )
        cipher.cipher_arg_parser(parser=sub_parser)
        sub_parser.set_defaults(cipher_class=cipher)

    args = parser.parse_args()

    cipher = args.cipher_class
    cipher(args)


if __name__ == "__main__":
    main()
