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
        json_schema_extra={
            "example": "NOBODY GOES THERE ANY MORE BECAUSE ITS TOO CROWDED"
        },
    )


class PolybiusDecryptSchema(BaseModel):
    cipher: str = Field(
        json_schema_extra={
            "example": "MLYLWB TLVH GSVIV ZMB NLIV YVXZFHV RGH GLL XILDWVW"
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
    response = PolybiusResultSchema(
        cipher=cipher,
        message=body.message,
        key=body.key,
    )
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
        key=body.key,
    )

    return response.model_dump(), 200
