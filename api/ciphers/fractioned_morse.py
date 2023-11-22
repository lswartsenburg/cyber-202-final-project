from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from pydantic import BaseModel, Field

from cipher_algorithms.ciphers.fractioned_morse.algo import FractionedMorseCipher

from ..common.schemas import ExceptionSchema


fractioned_morse_blueprint = APIBlueprint(
    "fractioned_morse", __name__, url_prefix="/fractioned_morse"
)


tag = Tag(
    name="Fractioned Morse cipher",
    description="Cipher functions for the Fractioned Morse cipher",
)


class FractionedMorseEncryptSchema(BaseModel):
    message: str = Field(
        json_schema_extra={
            "example": "NOBODY GOES THERE ANY MORE BECAUSE ITS TOO CROWDED"
        }
    )
    key: str = Field(json_schema_extra={"example": "CROWDED"})


class FractionedMorseDecryptSchema(BaseModel):
    cipher: str = Field(
        json_schema_extra={
            "example": "IKUOKUBDZIKTCZQOAIFEIHPLKSAZCTHAMECTQXCZVNLUIWVMLGTG"
        }
    )
    key: str = Field(json_schema_extra={"example": "CROWDED"})


class FractionedMorseResultSchema(
    FractionedMorseEncryptSchema, FractionedMorseDecryptSchema
):
    intermediate_morse: str


@fractioned_morse_blueprint.post(
    "/encrypt",
    tags=[tag],
    summary="Uses the One Time Pad cipher to encrypt a message",
    responses={200: FractionedMorseDecryptSchema, 422: ExceptionSchema},
)
def one_time_pad_encrypt(body: FractionedMorseEncryptSchema):
    fractioned_morse = FractionedMorseCipher(key=body.key)
    cipher = fractioned_morse.encrypt(message=body.message)
    response = FractionedMorseResultSchema(
        cipher=cipher["cipher"],
        message=body.message,
        key=body.key,
        intermediate_morse=cipher["intermediate_morse"],
    )
    return response.model_dump(), 200


@fractioned_morse_blueprint.post(
    "/decrypt",
    tags=[tag],
    summary="Uses the One Time Pad cipher to decrypt a message",
    responses={200: FractionedMorseDecryptSchema, 422: ExceptionSchema},
)
def one_time_pad_decrypt(body: FractionedMorseDecryptSchema):
    fractioned_morse = FractionedMorseCipher(key=body.key)
    message = fractioned_morse.decrypt(cipher=body.cipher)
    response = FractionedMorseResultSchema(
        cipher=body.cipher,
        message=message["message"],
        key=body.key,
        intermediate_morse=message["intermediate_morse"],
    )

    return response.model_dump(), 200
