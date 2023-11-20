from flask import Flask, jsonify
from cipher_algorithms.ciphers.caesar.algo import caesar_cipher, Operation
from flasgger import APISpec, Schema, Swagger, fields
from apispec_webframeworks.flask import FlaskPlugin
from apispec.ext.marshmallow import MarshmallowPlugin

from ciphers.caesar import caesar_blueprint, get_caesar_schemas, get_caesar_paths
from ciphers.vigenere import (
    vigenere_blueprint,
    get_vigenere_schemas,
    get_vigenere_paths,
)


app = Flask(__name__)

spec = APISpec(
    title="Cipher Algorithms REST API",
    version="0.0.1",
    openapi_version="2.0",
    plugins=[
        FlaskPlugin(),
        MarshmallowPlugin(),
    ],
)


@app.route("/hello")
def hello_world():
    return caesar_cipher("HELLO WORLD", Operation.ENCRYPT, shift=1)


swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "specs_route": "/",
    "hide_top_bar": True,
}

template = spec.to_flasgger(app)

swag = Swagger(
    app,
    template=template,
    config=swagger_config,
)

app.register_blueprint(caesar_blueprint)
app.register_blueprint(vigenere_blueprint)

app.run(debug=True, port=5001)
