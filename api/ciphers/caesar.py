from flask import Blueprint, Flask, jsonify

from flasgger import APISpec, Schema, Swagger, fields

caesar_blueprint = Blueprint("caesar", __name__, url_prefix="/caesar")


class CaesarEncryptSchema(Schema):
    message = fields.Str(required=True)
    shift = fields.Int(required=True)


class CaesarDecryptSchema(Schema):
    cipher = fields.Str(required=True)
    shift = fields.Int(required=True)


class CaesarResultSchema(CaesarEncryptSchema, CaesarDecryptSchema):
    pass


@caesar_blueprint.route("/encrypt", methods=["POST"])
def encrypt():
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


def get_caesar_schemas():
    return [CaesarEncryptSchema, CaesarDecryptSchema, CaesarResultSchema]


def get_caesar_paths():
    return [encrypt]
