from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from pydantic import BaseModel, Field

from cipher_algorithms.ciphers.one_time_pad.algo import one_time_pad

from ..common.schemas import ExceptionSchema


one_time_pad_blueprint = APIBlueprint(
    "one_time_pad", __name__, url_prefix="/one_time_pad"
)


tag = Tag(
    name="One Time Pad cipher",
    description="Cipher functions for the One Time Pad cipher",
)


class OneTimePadEncryptSchema(BaseModel):
    message: str = Field(json_schema_extra={"example": "PEACE"})
    key: str = Field(json_schema_extra={"example": "LFNNY"})


class OneTimePadDecryptSchema(BaseModel):
    cipher: str = Field(json_schema_extra={"example": "ZQMKX"})
    key: str = Field(json_schema_extra={"example": "LFNNY"})


class OneTimePadResultSchema(OneTimePadEncryptSchema, OneTimePadDecryptSchema):
    pass


@one_time_pad_blueprint.post(
    "/encrypt",
    tags=[tag],
    summary="Uses the One Time Pad cipher to encrypt a message",
    responses={200: OneTimePadResultSchema, 422: ExceptionSchema},
)
def one_time_pad_encrypt(body: OneTimePadEncryptSchema):
    cipher = one_time_pad(input=body.message, key_with_spaces=body.key)
    response = OneTimePadResultSchema(cipher=cipher, message=body.message, key=body.key)
    return response.model_dump(), 200


@one_time_pad_blueprint.post(
    "/decrypt",
    tags=[tag],
    summary="Uses the One Time Pad cipher to decrypt a message",
    responses={200: OneTimePadResultSchema, 422: ExceptionSchema},
)
def one_time_pad_decrypt(body: OneTimePadDecryptSchema):
    message = one_time_pad(input=body.cipher, key_with_spaces=body.key)
    response = OneTimePadResultSchema(cipher=body.cipher, message=message, key=body.key)

    return response.model_dump(), 200
