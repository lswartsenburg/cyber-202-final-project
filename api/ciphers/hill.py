from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from pydantic import BaseModel, Field

from cipher_algorithms.ciphers.hill.algo import (
    encrypt,
    decrypt,
)

from ..common.schemas import ExceptionSchema

hill_blueprint = APIBlueprint("hill", __name__, url_prefix="/hill")


tag = Tag(
    name="Hill cipher",
    description="Cipher functions for the Hill cipher",
)


class HillEncryptSchema(BaseModel):
    message: str = Field(
        json_schema_extra={"example": "TESTINGABC"},
    )
    key: str = Field(None, json_schema_extra={"example": "HELLO"})


class HillDecryptSchema(BaseModel):
    cipher: str = Field(json_schema_extra={"example": "VQXVRTQYDA"})
    key: str = Field(json_schema_extra={"example": "HELLO"})


class HillResultSchema(HillEncryptSchema, HillDecryptSchema):
    pass


@hill_blueprint.post(
    "/encrypt",
    tags=[tag],
    summary="Uses the Hill cipher to encrypt a message",
    responses={200: HillResultSchema, 422: ExceptionSchema},
)
def hill_rest_encrypt(body: HillEncryptSchema):
    cipher = encrypt(body.message, body.key)
    response = HillResultSchema(
        cipher=cipher,
        message=body.message,
        key=body.key,
    )
    return response.model_dump(), 200


@hill_blueprint.post(
    "/decrypt",
    tags=[tag],
    summary="Uses the Hill cipher to decrypt a message",
    responses={200: HillResultSchema, 422: ExceptionSchema},
)
def hill_rest_decrypt(body: HillDecryptSchema):
    message = decrypt(body.cipher, body.key)
    response = HillResultSchema(
        cipher=body.cipher,
        message=message,
        key=body.key,
    )

    return response.model_dump(), 200
