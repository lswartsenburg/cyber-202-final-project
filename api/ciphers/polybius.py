from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from pydantic import BaseModel, Field

from cipher_algorithms.ciphers.polybius_cipher.algo import (
    encrypt_polybius,
    decrypt_polybius,
)

from ..common.schemas import ExceptionSchema

polybius_blueprint = APIBlueprint("polybius", __name__, url_prefix="/polybius")

tag = Tag(
    name="Polybius cipher",
    description="Cipher functions for the Polybius cipher",
)


class PolybiusEncryptSchema(BaseModel):
    message: str = Field(
        json_schema_extra={"example": "the quick brown fox jumps over the lazy dog"},
    )


class PolybiusDecryptSchema(BaseModel):
    cipher: str = Field(
        json_schema_extra={
            "example": "44 23 15 41 45 24 13 25 12 42 34 52 33 21 34 53 24 45 32 35 43 34 51 15 42 44 23 15 31 11 55 54 14 34 22"
        }
    )


class PolybiusResultSchema(PolybiusEncryptSchema, PolybiusDecryptSchema):
    pass


@polybius_blueprint.post(
    "/encrypt",
    tags=[tag],
    summary="Uses the Polybius cipher to encrypt a message",
    responses={200: PolybiusResultSchema, 422: ExceptionSchema},
)
def polybius_encrypt(body: PolybiusEncryptSchema):
    cipher = encrypt_polybius(plain_text=body.message)
    response = PolybiusResultSchema(cipher=cipher, message=body.message)
    return response.model_dump(), 200


@polybius_blueprint.post(
    "/decrypt",
    tags=[tag],
    summary="Uses the Polybius cipher to decrypt a message",
    responses={200: PolybiusResultSchema, 422: ExceptionSchema},
)
def polybius_decrypt(body: PolybiusDecryptSchema):
    message = decrypt_polybius(cipher_text=body.cipher)
    response = PolybiusResultSchema(
        cipher=body.cipher,
        message=message,
    )

    return response.model_dump(), 200
