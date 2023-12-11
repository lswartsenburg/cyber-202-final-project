from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from pydantic import BaseModel, Field

from cipher_algorithms.ciphers.base64.algo import (
    encrypt,
    decrypt,
)

from ..common.schemas import ExceptionSchema

base64_blueprint = APIBlueprint("base64", __name__, url_prefix="/base64")


tag = Tag(
    name="Base64 cipher",
    description="Cipher functions for the Base64 cipher",
)


class Base64EncryptSchema(BaseModel):
    message: str = Field(
        json_schema_extra={"example": "testingabc"},
    )


class Base64DecryptSchema(BaseModel):
    cipher: str = Field(json_schema_extra={"example": "dGVzdGluZ2FiYw=="})


class Base64ResultSchema(Base64EncryptSchema, Base64DecryptSchema):
    pass


@base64_blueprint.post(
    "/encrypt",
    tags=[tag],
    summary="Uses the Base64 cipher to encrypt a message",
    responses={200: Base64ResultSchema, 422: ExceptionSchema},
)
def base64_rest_encrypt(body: Base64EncryptSchema):
    cipher = encrypt(body.message)
    response = Base64ResultSchema(
        cipher=cipher,
        message=body.message,
    )
    return response.model_dump(), 200


@base64_blueprint.post(
    "/decrypt",
    tags=[tag],
    summary="Uses the Base64 cipher to decrypt a message",
    responses={200: Base64ResultSchema, 422: ExceptionSchema},
)
def base64_rest_decrypt(body: Base64DecryptSchema):
    message = decrypt(body.cipher)
    response = Base64ResultSchema(
        cipher=body.cipher,
        message=message,
    )

    return response.model_dump(), 200
