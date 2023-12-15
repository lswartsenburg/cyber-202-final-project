from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from pydantic import BaseModel, Field

from cipher_algorithms.ciphers.rail_fence.algo import (
    encryptRailFence,
    decryptRailFence,
)

from ..common.schemas import ExceptionSchema

rail_fence_cipher_blueprint = APIBlueprint(
    "rail_fence_cipher", __name__, url_prefix="/rail_fence_cipher"
)

tag = Tag(
    name="Rail Fence cipher",
    description="Cipher functions for the Rail Fence cipher",
)


class RailFenceEncryptSchema(BaseModel):
    message: str = Field(
        json_schema_extra={"example": "the quick brown fox jumps over the lazy dog"},
    )
    key: int = Field(None, json_schema_extra={"example": 3})


class RailFenceDecryptSchema(BaseModel):
    cipher: str = Field(
        json_schema_extra={"example": "tqkofjsehadh uc rw o up vrtelz oeibnxmo  yg"}
    )
    key: int = Field(json_schema_extra={"example": 3})


class RailFenceResultSchema(RailFenceEncryptSchema, RailFenceDecryptSchema):
    pass


@rail_fence_cipher_blueprint.post(
    "/encrypt",
    tags=[tag],
    summary="Uses the Rail Fence cipher to encrypt a message",
    responses={200: RailFenceResultSchema, 422: ExceptionSchema},
)
def rail_fence_cipher_encrypt(body: RailFenceEncryptSchema):
    cipher = encryptRailFence(text=body.message, key=body.key)
    response = RailFenceResultSchema(
        cipher=cipher,
        message=body.message,
        key=body.key,
    )
    return response.model_dump(), 200


@rail_fence_cipher_blueprint.post(
    "/decrypt",
    tags=[tag],
    summary="Uses the Rail Fence cipher to decrypt a message",
    responses={200: RailFenceResultSchema, 422: ExceptionSchema},
)
def rail_fence_cipher_decrypt(body: RailFenceDecryptSchema):
    message = decryptRailFence(cipher=body.cipher, key=body.key)
    response = RailFenceResultSchema(
        cipher=body.cipher,
        message=message,
        key=body.key,
    )

    return response.model_dump(), 200
