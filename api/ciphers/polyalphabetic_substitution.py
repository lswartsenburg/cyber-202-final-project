from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from pydantic import BaseModel, Field

from cipher_algorithms.ciphers.polyalphabetic_substitution_cipher.algo import (
    encrypt,
    decrypt,
)

from ..common.schemas import ExceptionSchema

polyalphabetic_substitution_blueprint = APIBlueprint(
    "polyalphabetic_substitution", __name__, url_prefix="/polyalphabetic_substitution"
)

tag = Tag(
    name="Polyalphabetic Substitution cipher",
    description="Cipher functions for the Polyalphabetic Substitution cipher",
)


# TODO Update values
class PolyalphabeticSubstitutionEncryptSchema(BaseModel):
    message: str = Field(
        json_schema_extra={
            "example": "NOBODY GOES THERE ANY MORE BECAUSE ITS TOO CROWDED"
        },
    )
    key: str = Field(None, json_schema_extra={"example": "HELLO"})


# TODO Update values
class PolyalphabeticSubstitutionDecryptSchema(BaseModel):
    cipher: str = Field(
        json_schema_extra={
            "example": "MLYLWB TLVH GSVIV ZMB NLIV YVXZFHV RGH GLL XILDWVW"
        }
    )
    key: str = Field(json_schema_extra={"example": "HELLO"})


class PolyalphabeticSubstitutionResultSchema(
    PolyalphabeticSubstitutionEncryptSchema, PolyalphabeticSubstitutionDecryptSchema
):
    pass


@polyalphabetic_substitution_blueprint.post(
    "/encrypt",
    tags=[tag],
    summary="Uses the Polyalphabetic Substitution cipher to encrypt a message",
    responses={200: PolyalphabeticSubstitutionResultSchema, 422: ExceptionSchema},
)
def polyalphabetic_substitution_encrypt(body: PolyalphabeticSubstitutionEncryptSchema):
    cipher = encrypt(text=body.message, keyword=body.key)
    response = PolyalphabeticSubstitutionResultSchema(
        cipher=cipher,
        message=body.message,
        key=body.key,
    )
    return response.model_dump(), 200


@polyalphabetic_substitution_blueprint.post(
    "/decrypt",
    tags=[tag],
    summary="Uses the Polyalphabetic Substitution cipher to decrypt a message",
    responses={200: PolyalphabeticSubstitutionResultSchema, 422: ExceptionSchema},
)
def polyalphabetic_substitution_decrypt(body: PolyalphabeticSubstitutionDecryptSchema):
    message = decrypt(text=body.cipher, keyword=body.key)
    response = PolyalphabeticSubstitutionResultSchema(
        cipher=body.cipher,
        message=message,
        key=body.key,
    )

    return response.model_dump(), 200
