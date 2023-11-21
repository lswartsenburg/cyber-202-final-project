from flask_openapi3 import Tag

from flask_openapi3 import APIBlueprint
from pydantic import BaseModel

from cipher_algorithms.ciphers.caesar.algo import caesar_cipher, Operation, break_cipher
from cipher_algorithms.helpers.dictionary import get_dictionary
from cipher_algorithms.helpers.char_conversion_27 import InvalidCharacterException

caesar_blueprint = APIBlueprint("caesar", __name__, url_prefix="/caesar")

tag = Tag(name="Caesar cipher", description="Cipher functions for the Caesar cipher")


class CaesarEncryptSchema(BaseModel):
    message: str
    shift: int


class CaesarDecryptSchema(BaseModel):
    cipher: str
    shift: int


class CaesarBreakSchema(BaseModel):
    cipher: str


class CaesarResultSchema(CaesarEncryptSchema, CaesarDecryptSchema):
    pass


@caesar_blueprint.post(
    "/encrypt",
    tags=[tag],
    summary="Uses the Caesar cipher to encrypt a message",
    responses={200: CaesarResultSchema},
)
def caesar_encrypt(body: CaesarEncryptSchema):
    """
    This is an encryption implementation of the Caesar cipther that accepts only upper case characters and space (27 characters). The
    space is at index 26.
    """
    try:
        cipher = caesar_cipher(
            input_value=body.message, operation=Operation.ENCRYPT, shift=body.shift
        )
        response = CaesarResultSchema(
            cipher=cipher, message=body.message, shift=body.shift
        )
        return response.model_dump(), 200
    except Exception as e:
        return f"Unexpected error {type(e)}:\n\n{e}", 422


@caesar_blueprint.post(
    "/decrypt",
    tags=[tag],
    summary="Uses the Caesar cipher to decrypt a message",
    responses={200: CaesarResultSchema},
)
def caesar_decrypt(body: CaesarDecryptSchema):
    """
    This is an decryption implementation of the Caesar cipther that accepts only upper case characters and space (27 characters). The
    space is at index 26.
    """
    try:
        message = caesar_cipher(
            input_value=body.cipher, operation=Operation.DECRYPT, shift=body.shift
        )
        response = CaesarResultSchema(
            message=message, cipher=body.cipher, shift=body.shift
        )
        return response.model_dump(), 200
    except Exception as e:
        return f"Unexpected error {type(e)}:\n\n{e}", 422


@caesar_blueprint.post(
    "/break",
    tags=[tag],
    summary="A somewhat efficient algorithm that breaks a caesar cipher",
    responses={200: CaesarResultSchema},
)
def caesar_break(body: CaesarBreakSchema):
    """
    This implementation uses a word dictionary to break a Caesar cipher
    """
    try:
        words = get_dictionary()
        result = break_cipher(body.cipher, words)
        response = CaesarResultSchema(
            message=result["message"], cipher=body.cipher, shift=result["shift"]
        )
        return response.model_dump(), 200
    except Exception as e:
        return f"Unexpected error {type(e)}:\n\n{e}", 422
