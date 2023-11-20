from flask import Blueprint, Flask, jsonify

from flasgger import APISpec, Schema, Swagger, fields

vigenere_blueprint = Blueprint("vigenere", __name__, url_prefix="/vigenere")


class VigenereEncryptSchema(Schema):
    message = fields.Str(required=True)
    shift = fields.Int(required=True)


class VigenereDecryptSchema(Schema):
    cipher = fields.Str(required=True)
    shift = fields.Int(required=True)


class VigenereResultSchema(VigenereEncryptSchema, VigenereDecryptSchema):
    pass


@vigenere_blueprint.route("/encrypt", methods=["POST"])
def encrypt(body: VigenereEncryptSchema):
    """Create a cute furry animal endpoint.
    ---
    post:
      description: Encrypt a message using the Caesar cipher with specified shift
      parameters:
        - in: body
          name: body
          required: True
          schema:
            $ref: '#/definitions/CaesarEncrypt'
      responses:
        201:
          description: If encryption succeeded
          schema:
            $ref: '#/definitions/CaesarResult'
    """
    return "Hello"


def get_vigenere_schemas():
    return [VigenereEncryptSchema, VigenereDecryptSchema, VigenereResultSchema]


def get_vigenere_paths():
    return [encrypt]
