from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from pydantic import BaseModel, Field
from typing import Optional
import json

from cipher_algorithms.ciphers.polygram_substitution_cipher.algo import (
    encrypt,
    decrypt,
)

from ..common.schemas import ExceptionSchema

polygram_substitution_cipher_blueprint = APIBlueprint(
    "polygram_substitution_cipher", __name__, url_prefix="/polygram_substitution_cipher"
)

tag = Tag(
    name="Polygram Substitution cipher",
    description="Cipher functions for the Polygram Substitution cipher",
)


class PolygramSubstitutionEncryptSchema(BaseModel):
    message: str = Field(json_schema_extra={"example": "ABCD"})
    key: Optional[str] = Field(
        None, json_schema_extra={"example": '{"AB": "ZY", "CD": "XW"}'}
    )


class PolygramSubstitutionDecryptSchema(BaseModel):
    cipher: str = Field(json_schema_extra={"example": "ZYXW"})
    key: Optional[str] = Field(
        None, json_schema_extra={"example": '{"AB": "ZY", "CD": "XW"}'}
    )


class PolygramSubstitutionResultSchema(
    PolygramSubstitutionEncryptSchema, PolygramSubstitutionDecryptSchema
):
    pass


@polygram_substitution_cipher_blueprint.post(
    "/encrypt",
    tags=[tag],
    summary="Uses the Polygram Substitution cipher to encrypt a message",
    responses={200: PolygramSubstitutionResultSchema, 422: ExceptionSchema},
)
def polygram_substitution_cipher_encrypt(body: PolygramSubstitutionEncryptSchema):
    key = None
    if body.key is not None:
        key = json.loads(body.key)

    cipher = encrypt(text=body.message, key=key)
    response = PolygramSubstitutionResultSchema(
        cipher=cipher,
        message=body.message,
        key=body.key,
    )
    return response.model_dump(), 200


@polygram_substitution_cipher_blueprint.post(
    "/decrypt",
    tags=[tag],
    summary="Uses the Polygram Substitution cipher to decrypt a message",
    responses={200: PolygramSubstitutionResultSchema, 422: ExceptionSchema},
)
def polygram_substitution_cipher_decrypt(body: PolygramSubstitutionDecryptSchema):
    key = None
    if body.key is not None:
        key = json.loads(body.key)

    message = decrypt(text=body.cipher, key=key)
    response = PolygramSubstitutionResultSchema(
        cipher=body.cipher,
        message=message,
        key=body.key,
    )

    return response.model_dump(), 200
