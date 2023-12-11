from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from pydantic import BaseModel, Field

from cipher_algorithms.ciphers.columnar_transposition.algo import (
    encryptMessage,
    decryptMessage,
)

from ..common.schemas import ExceptionSchema

columnar_transposition_blueprint = APIBlueprint(
    "columnar_transposition", __name__, url_prefix="/columnar_transposition"
)


tag = Tag(
    name="Columnar Transposition cipher",
    description="Cipher functions for the Columnar Transposition cipher",
)


class ColumnarTranspositionEncryptSchema(BaseModel):
    message: str = Field(
        json_schema_extra={
            "example": "NOBODY GOES THERE ANY MORE BECAUSE ITS TOO CROWDED"
        },
    )
    key: str = Field(None, json_schema_extra={"example": "HELLO"})


class ColumnarTranspositionDecryptSchema(BaseModel):
    cipher: str = Field(
        json_schema_extra={
            "example": "MLYLWB TLVH GSVIV ZMB NLIV YVXZFHV RGH GLL XILDWVW"
        }
    )
    key: str = Field(json_schema_extra={"example": "HELLO"})


class ColumnarTranspositionResultSchema(
    ColumnarTranspositionEncryptSchema, ColumnarTranspositionDecryptSchema
):
    pass


@columnar_transposition_blueprint.post(
    "/encrypt",
    tags=[tag],
    summary="Uses the Columnar Transposition cipher to encrypt a message",
    responses={200: ColumnarTranspositionResultSchema, 422: ExceptionSchema},
)
def columnar_transposition_encrypt(body: ColumnarTranspositionEncryptSchema):
    cipher = decryptMessage(msg=body.message, key=body.key)
    response = ColumnarTranspositionResultSchema(
        cipher=cipher,
        message=body.message,
        key=body.key,
    )
    return response.model_dump(), 200


@columnar_transposition_blueprint.post(
    "/decrypt",
    tags=[tag],
    summary="Uses the Columnar Transposition cipher to decrypt a message",
    responses={200: ColumnarTranspositionResultSchema, 422: ExceptionSchema},
)
def columnar_transposition_decrypt(body: ColumnarTranspositionDecryptSchema):
    message = encryptMessage(cipher=body.cipher, key=body.key)
    response = ColumnarTranspositionResultSchema(
        cipher=body.cipher,
        message=message,
        key=body.key,
    )

    return response.model_dump(), 200
