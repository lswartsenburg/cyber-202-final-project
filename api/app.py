import traceback

from flask_openapi3 import Info
from flask_openapi3 import OpenAPI, APIBlueprint
from flask import redirect

from .ciphers.bifid import bifid_blueprint
from .ciphers.caesar import caesar_blueprint
from .ciphers.columnar_transposition import columnar_transposition_blueprint
from .ciphers.fractioned_morse import fractioned_morse_blueprint
from .ciphers.homophonic_substitution import homophonic_substitution_blueprint
from .ciphers.mono_alphabetic_substitution import mono_alphabetic_substitution_blueprint
from .ciphers.one_time_pad import one_time_pad_blueprint
from .ciphers.polyalphabetic_substitution import polyalphabetic_substitution_blueprint
from .ciphers.polybius import polybius_blueprint
from .ciphers.polygram_substitution import polygram_substitution_cipher_blueprint
from .ciphers.rail_fence import rail_fence_cipher_blueprint
from .ciphers.vigenere import vigenere_blueprint

from .common.schemas import ExceptionSchema
from cipher_algorithms.helpers.char_conversion_27 import InvalidCharacterException
from cipher_algorithms.ciphers.polygram_substitution_cipher.algo import (
    UnsupportedCharacterError,
)


info = Info(title="Cipher Algorithm API", version="0.0.1")
app = OpenAPI(__name__, info=info, doc_prefix="/docs", swagger_url="/")
v1_api = APIBlueprint("api/v1", __name__, url_prefix="/api/v1")
ciphers = APIBlueprint("ciphers", __name__, url_prefix="/ciphers")


@app.errorhandler(InvalidCharacterException)
def handle_invalid_char_exception(err):
    error_response = ExceptionSchema(
        code=422, name=f"{type(err)}", description=f"{err}"
    )
    return error_response.model_dump(), 422


@app.errorhandler(UnsupportedCharacterError)
def handle_unsupported_char_exception(err):
    error_response = ExceptionSchema(
        code=422, name=f"{type(err)}", description=f"{err}"
    )
    return error_response.model_dump(), 422


@app.errorhandler(Exception)
def handle_exception(err):
    app.logger.error(f"Unknown Exception: {str(err)}")
    app.logger.debug(
        "".join(
            traceback.format_exception(etype=type(err), value=err, tb=err.__traceback__)
        )
    )
    exception = ExceptionSchema(
        code=500,
        name="ServerError",
        description="Aaaah, something went wrong. This one is on us.",
    )

    return exception.model_dump(), 500


@app.route("/")
def homepage():
    return redirect("docs")


ciphers.register_api(bifid_blueprint)
ciphers.register_api(caesar_blueprint)
ciphers.register_api(columnar_transposition_blueprint)
ciphers.register_api(fractioned_morse_blueprint)
ciphers.register_api(homophonic_substitution_blueprint)
ciphers.register_api(mono_alphabetic_substitution_blueprint)
ciphers.register_api(one_time_pad_blueprint)
ciphers.register_api(polyalphabetic_substitution_blueprint)
ciphers.register_api(polybius_blueprint)
ciphers.register_api(polygram_substitution_cipher_blueprint)
ciphers.register_api(rail_fence_cipher_blueprint)
ciphers.register_api(vigenere_blueprint)


v1_api.register_api(ciphers)
app.register_api(v1_api)
