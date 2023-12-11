from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from pydantic import BaseModel, Field

from cipher_algorithms.ciphers.bifid_cipher.algo import (
    bifid_encrypt,
    bifid_decrypt,
)

from ..common.schemas import ExceptionSchema

bifid_blueprint = APIBlueprint("bifid", __name__, url_prefix="/bifid")


tag = Tag(
    name="Bifid cipher",
    description="Cipher functions for the Bifid cipher",
)


class BifidEncryptSchema(BaseModel):
    message: str = Field(
        json_schema_extra={
            "example": "NOBODY GOES THERE ANY MORE BECAUSE ITS TOO CROWDED"
        },
    )
    key: str = Field(None, json_schema_extra={"example": "HELLO"})


class BifidDecryptSchema(BaseModel):
    cipher: str = Field(
        json_schema_extra={
            "example": "MLYLWB TLVH GSVIV ZMB NLIV YVXZFHV RGH GLL XILDWVW"
        }
    )
    key: str = Field(json_schema_extra={"example": "HELLO"})


class BifidResultSchema(BifidEncryptSchema, BifidDecryptSchema):
    pass


@bifid_blueprint.post(
    "/encrypt",
    tags=[tag],
    summary="Uses the Bifid cipher to encrypt a message",
    responses={200: BifidResultSchema, 422: ExceptionSchema},
)
def bifid_rest_encrypt(body: BifidEncryptSchema):
    cipher = bifid_encrypt(plaintext=body.message, keyword=body.key)
    response = BifidResultSchema(
        cipher=cipher,
        message=body.message,
        key=body.key,
    )
    return response.model_dump(), 200


@bifid_blueprint.post(
    "/decrypt",
    tags=[tag],
    summary="Uses the Bifid cipher to decrypt a message",
    responses={200: BifidResultSchema, 422: ExceptionSchema},
)
def bifid_rest_decrypt(body: BifidDecryptSchema):
    message = bifid_decrypt(ciphertext=body.cipher, keyword=body.key)
    response = BifidResultSchema(
        cipher=body.cipher,
        message=message,
        key=body.key,
    )

    return response.model_dump(), 200
