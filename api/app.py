from flask import Flask, jsonify
from cipher_algorithms.ciphers.caesar.algo import caesar_cipher, Operation
from flasgger import APISpec, Schema, Swagger, fields
from apispec_webframeworks.flask import FlaskPlugin
from apispec.ext.marshmallow import MarshmallowPlugin


app = Flask(__name__)

spec = APISpec(
    title="Flasger Petstore",
    version="1.0.10",
    openapi_version="2.0",
    plugins=[
        FlaskPlugin(),
        MarshmallowPlugin(),
    ],
)


# Optional marshmallow support
class CategorySchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)


class PetSchema(Schema):
    category = fields.Nested(CategorySchema, many=True)
    name = fields.Str()


@app.route("/random")
def random_pet():
    """
    A cute furry animal endpoint.
    Get a random pet
    ---
    description: Get a random pet
    responses:
        200:
            description: A pet to be returned
            schema:
                $ref: '#/definitions/Pet'
    """
    pet = {"category": [{"id": 1, "name": "rodent"}], "name": "Mickey"}
    return jsonify(PetSchema().dump(pet))


@app.route("/add", methods=["POST"])
def create_pet(body: PetSchema):
    """Create a cute furry animal endpoint.
    ---
    post:
      description: Create a random pet
      parameters:
        - in: body
          name: body
          required: True
          schema:
                $ref: '#/definitions/Pet'
      security:
        - ApiKeyAuth: []
      responses:
        201:
          description: If pet is created
          content:
            application/json:
              status: string
    """
    return jsonify({"status": "New user created"}), 201


@app.route("/")
def hello_world():
    return caesar_cipher("HELLO WORLD", Operation.ENCRYPT, shift=1)


template = spec.to_flasgger(
    app, definitions=[CategorySchema, PetSchema], paths=[random_pet, create_pet]
)
swag = Swagger(app, template=template)
