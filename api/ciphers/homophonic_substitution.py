from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from pydantic import BaseModel, Field
from typing import Optional

from cipher_algorithms.ciphers.homophonic_substitution.algo import (
    HomophonicSubstitution,
)
import json

from ..common.schemas import ExceptionSchema

CIPHER_NAME = "Homophonic Substitution"
EXAMPLE_KEY_STRING = '{"A":["21","27","31","40"],"B":["15"],"C":["01","33"],"D":["20","34"],"E":["22","28","32","36","37"],"F":["05"],"G":["17"],"H":["14"],"I":["02","29","38","41"],"J":["19"],"K":["03"],"L":["07","39","42"],"M":["09","43"],"N":["12","48","97"],"O":["18","60","85"],"P":["26","44"],"Q":["25"],"R":["24","49"],"S":["10","30","45","99"],"T":["06","96","55"],"U":["16","94"],"V":["23"],"W":["13"],"X":["11"],"Y":["08"],"Z":["04"]}'

homophonic_substitution_blueprint = APIBlueprint(
    "homophonic_substitution", __name__, url_prefix="/homophonic_substitution"
)


tag = Tag(
    name=f"{CIPHER_NAME} cipher",
    description=f"Cipher functions for the {CIPHER_NAME} cipher",
)


class HomophonicSubstitutionEncryptSchema(BaseModel):
    message: str = Field(
        json_schema_extra={
            "example": "NOBODY GOES THERE ANY MORE BECAUSE ITS TOO CROWDED"
        },
    )
    key: Optional[str] = Field(None, json_schema_extra={"example": EXAMPLE_KEY_STRING})


class HomophonicSubstitutionDecryptSchema(BaseModel):
    cipher: str = Field(
        json_schema_extra={
            "example": "481815853408 17603230 9614362437 274808 43852436 15320121943032 025530 968560 33491813343734"
        }
    )
    key: str = Field(json_schema_extra={"example": EXAMPLE_KEY_STRING})


class HomophonicSubstitutionResultSchema(
    HomophonicSubstitutionEncryptSchema, HomophonicSubstitutionDecryptSchema
):
    pass


@homophonic_substitution_blueprint.post(
    "/encrypt",
    tags=[tag],
    summary=f"Uses the {CIPHER_NAME} to encrypt a message",
    responses={200: HomophonicSubstitutionResultSchema, 422: ExceptionSchema},
)
def homophonic_substitution_encrypt(body: HomophonicSubstitutionEncryptSchema):
    key = None
    try:
        key = json.loads(body.key)
    except Exception as e:
        response = ExceptionSchema(code=422, name=f"{type(e)}", description=f"{e}")
        return response.model_dump(), 422

    homophonic_substitution = HomophonicSubstitution(key=key)
    cipher = homophonic_substitution.encrypt(message=body.message)
    response = HomophonicSubstitutionResultSchema(
        cipher=cipher,
        message=body.message,
        key=json.dumps(homophonic_substitution.key),
    )
    return response.model_dump(), 200


@homophonic_substitution_blueprint.post(
    "/decrypt",
    tags=[tag],
    summary=f"Uses the {CIPHER_NAME} cipher to decrypt a message",
    responses={200: HomophonicSubstitutionResultSchema, 422: ExceptionSchema},
)
def homophonic_substitutionn_decrypt(body: HomophonicSubstitutionDecryptSchema):
    key = None
    try:
        key = json.loads(body.key)
    except Exception as e:
        response = ExceptionSchema(code=422, name=f"{type(e)}", description=f"{e}")
        return response.model_dump(), 422

    homophonic_substitution = HomophonicSubstitution(key=key)
    message = homophonic_substitution.decrypt(cipher=body.cipher)
    response = HomophonicSubstitutionResultSchema(
        cipher=body.cipher,
        message=message,
        key=json.dumps(homophonic_substitution.key),
    )

    return response.model_dump(), 200
