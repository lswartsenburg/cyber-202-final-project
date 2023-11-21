from flask_openapi3 import Info
from flask_openapi3 import OpenAPI, APIBlueprint
from flask import redirect

from .ciphers.caesar import caesar_blueprint
from .ciphers.vigenere import (
    vigenere_blueprint,
)


info = Info(title="Cipher Algorithm API", version="0.0.1")
app = OpenAPI(__name__, info=info, doc_prefix="/docs", swagger_url="/")
v1_api = APIBlueprint("api/v1", __name__, url_prefix="/api/v1")
ciphers = APIBlueprint("ciphers", __name__, url_prefix="/ciphers")


@app.route("/")
def homepage():
    return redirect("docs")


ciphers.register_api(caesar_blueprint)
ciphers.register_api(vigenere_blueprint)


v1_api.register_api(ciphers)
app.register_api(v1_api)
