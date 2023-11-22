from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from pydantic import BaseModel, Field
from typing import Optional

from cipher_algorithms.ciphers.mono_alphabetic_substitution.algo import (
    MonoAlphabeticSubstitution,
    DEFAULT_CHARS,
)

from ..common.schemas import ExceptionSchema

mono_alphabetic_substitution_blueprint = APIBlueprint(
    "mono_alphabetic_substitution", __name__, url_prefix="/mono_alphabetic_substitution"
)


tag = Tag(
    name="Mono Alphabetic Substitution cipher",
    description="Cipher functions for the Mono Alphabetic Substitution cipher",
)


class MonoAlphabeticSubstitutionEncryptSchema(BaseModel):
    message: str = Field(
        json_schema_extra={
            "example": "NOBODY GOES THERE ANY MORE BECAUSE ITS TOO CROWDED"
        },
    )
    key: Optional[str] = Field(None, json_schema_extra={"example": DEFAULT_CHARS[::-1]})


class MonoAlphabeticSubstitutionDecryptSchema(BaseModel):
    cipher: str = Field(
        json_schema_extra={
            "example": "MLYLWB TLVH GSVIV ZMB NLIV YVXZFHV RGH GLL XILDWVW"
        }
    )
    key: str = Field(json_schema_extra={"example": DEFAULT_CHARS[::-1]})


class MonoAlphabeticSubstitutionResultSchema(
    MonoAlphabeticSubstitutionEncryptSchema, MonoAlphabeticSubstitutionDecryptSchema
):
    pass


@mono_alphabetic_substitution_blueprint.post(
    "/encrypt",
    tags=[tag],
    summary="Uses the Mono Alphabetic Substitution cipher to encrypt a message",
    responses={200: MonoAlphabeticSubstitutionResultSchema, 422: ExceptionSchema},
)
def mono_alphabetic_substitution_encrypt(body: MonoAlphabeticSubstitutionEncryptSchema):
    mono_alphabetic_substitution = MonoAlphabeticSubstitution(key=body.key)
    cipher = mono_alphabetic_substitution.encrypt(message=body.message)
    response = MonoAlphabeticSubstitutionResultSchema(
        cipher=cipher,
        message=body.message,
        key="".join(mono_alphabetic_substitution.key),
    )
    return response.model_dump(), 200


@mono_alphabetic_substitution_blueprint.post(
    "/decrypt",
    tags=[tag],
    summary="Uses the Mono Alphabetic Substitution cipher to decrypt a message",
    responses={200: MonoAlphabeticSubstitutionResultSchema, 422: ExceptionSchema},
)
def mono_alphabetic_substitution_decrypt(body: MonoAlphabeticSubstitutionDecryptSchema):
    mono_alphabetic_substitution = MonoAlphabeticSubstitution(key=body.key)
    message = mono_alphabetic_substitution.decrypt(cipher=body.cipher)
    response = MonoAlphabeticSubstitutionResultSchema(
        cipher=body.cipher,
        message=message,
        key="".join(mono_alphabetic_substitution.key),
    )

    return response.model_dump(), 200
