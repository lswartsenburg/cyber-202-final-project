from abc import ABC, abstractmethod


class Cipher(ABC):
    @classmethod
    @abstractmethod
    def cipher_arg_parser(parser):
        pass
