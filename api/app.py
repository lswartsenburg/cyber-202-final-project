from flask import Flask
from cipher_algorithms.ciphers.caesar.algo import caesar_cipher, Operation

app = Flask(__name__)


@app.route("/")
def hello_world():
    return caesar_cipher("HELLO WORLD", Operation.ENCRYPT, shift=1)
