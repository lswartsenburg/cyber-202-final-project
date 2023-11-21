from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from pydantic import BaseModel

from cipher_algorithms.ciphers.vigenere.algo import vigenere, Operation
from cipher_algorithms.helpers.char_conversion_27 import InvalidCharacterException

vigenere_blueprint = APIBlueprint("vigenere", __name__, url_prefix="/vigenere")


tag = Tag(
    name="Vigenere cipher", description="Cipher functions for the Vigenere cipher"
)


class VigenereEncryptSchema(BaseModel):
    message: str
    key: str


class VigenereDecryptSchema(BaseModel):
    cipher: str
    key: str


class VigenereResultSchema(VigenereEncryptSchema, VigenereDecryptSchema):
    pass


@vigenere_blueprint.post(
    "/encrypt",
    tags=[tag],
    summary="Uses the Vigenere cipher to encrypt a message",
    responses={200: VigenereResultSchema},
)
def vigenere_encrypt(body: VigenereEncryptSchema):
    try:
        cipher = vigenere(input=body.message, operation=Operation.ENCRYPT, key=body.key)
        response = VigenereResultSchema(
            cipher=cipher, message=body.message, key=body.key
        )
        return response.model_dump(), 200
    except Exception as e:
        return f"Unexpected error {type(e)}:\n\n{e}", 422


@vigenere_blueprint.post(
    "/decrypt",
    tags=[tag],
    summary="Uses the Vigenere cipher to decrypt a message",
    responses={200: VigenereResultSchema},
)
def vigenere_decrypt(body: VigenereDecryptSchema):
    try:
        message = vigenere(input=body.cipher, operation=Operation.DECRYPT, key=body.key)
        response = VigenereResultSchema(
            cipher=body.cipher, message=message, key=body.key
        )
        return response.model_dump(), 200
    except Exception as e:
        return f"Unexpected error {type(e)}:\n\n{e}", 422
