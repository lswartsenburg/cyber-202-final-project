from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from pydantic import BaseModel, Field

from cipher_algorithms.ciphers.vigenere.algo import vigenere, Operation

from ..common.schemas import ExceptionSchema


vigenere_blueprint = APIBlueprint("vigenere", __name__, url_prefix="/vigenere")


tag = Tag(
    name="Vigenere cipher", description="Cipher functions for the Vigenere cipher"
)


class VigenereEncryptSchema(BaseModel):
    message: str = Field(json_schema_extra={"example": "THE CAT IS OUT OF THE BAG"})
    key: str = Field(json_schema_extra={"example": "KOMRADE"})


class VigenereDecryptSchema(BaseModel):
    cipher: str = Field(json_schema_extra={"example": "CVQQCDXJWDQOXXJBRQTKIJPMX"})
    key: str = Field(json_schema_extra={"example": "KOMRADE"})


class VigenereResultSchema(VigenereEncryptSchema, VigenereDecryptSchema):
    pass


@vigenere_blueprint.post(
    "/encrypt",
    tags=[tag],
    summary="Uses the Vigenere cipher to encrypt a message",
    responses={200: VigenereResultSchema, 422: ExceptionSchema},
)
def vigenere_encrypt(body: VigenereEncryptSchema):
    cipher = vigenere(input=body.message, operation=Operation.ENCRYPT, key=body.key)
    response = VigenereResultSchema(cipher=cipher, message=body.message, key=body.key)
    return response.model_dump(), 200


@vigenere_blueprint.post(
    "/decrypt",
    tags=[tag],
    summary="Uses the Vigenere cipher to decrypt a message",
    responses={200: VigenereResultSchema, 422: ExceptionSchema},
)
def vigenere_decrypt(body: VigenereDecryptSchema):
    message = vigenere(input=body.cipher, operation=Operation.DECRYPT, key=body.key)
    response = VigenereResultSchema(cipher=body.cipher, message=message, key=body.key)

    return response.model_dump(), 200
