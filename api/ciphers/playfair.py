from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from pydantic import BaseModel, Field

from cipher_algorithms.ciphers.playfair.algo import (
    encrypt,
    decrypt,
)

from ..common.schemas import ExceptionSchema

playfair_blueprint = APIBlueprint("playfair", __name__, url_prefix="/playfair")


tag = Tag(
    name="Playfair cipher",
    description="Cipher functions for the Playfair cipher",
)


class PlayfairEncryptSchema(BaseModel):
    message: str = Field(
        json_schema_extra={"example": "TESTINGABC"},
    )
    key: str = Field(None, json_schema_extra={"example": "HELLO"})


class PlayfairDecryptSchema(BaseModel):
    cipher: str = Field(json_schema_extra={"example": "ROTUKPPGCD"})
    key: str = Field(json_schema_extra={"example": "HELLO"})


class PlayfairResultSchema(PlayfairEncryptSchema, PlayfairDecryptSchema):
    pass


@playfair_blueprint.post(
    "/encrypt",
    tags=[tag],
    summary="Uses the Playfair cipher to encrypt a message",
    responses={200: PlayfairResultSchema, 422: ExceptionSchema},
)
def playfair_rest_encrypt(body: PlayfairEncryptSchema):
    cipher = encrypt(body.message, body.key)
    response = PlayfairResultSchema(
        cipher=cipher,
        message=body.message,
        key=body.key,
    )
    return response.model_dump(), 200


@playfair_blueprint.post(
    "/decrypt",
    tags=[tag],
    summary="Uses the Playfair cipher to decrypt a message",
    responses={200: PlayfairResultSchema, 422: ExceptionSchema},
)
def playfair_rest_decrypt(body: PlayfairDecryptSchema):
    message = decrypt(body.cipher, body.key)
    response = PlayfairResultSchema(
        cipher=body.cipher,
        message=message,
        key=body.key,
    )

    return response.model_dump(), 200
