# Fun Cipher Algorithms

This repo implements various ciphers in easy to follow Python code. To make it convenient to test out various ciphers, a CLI command as well as a REST API are build on top of the ciphers. The purpose of this project is purely for educational purposes and the intend is to support people getting more familiar with cyptography. In addition to having a clean Python implementation of the ciphers, as well as easy to use interfaces, we hope to add informational literature about each cipher in the future. Most ciphers implemented in this repository never had, or no longer have any practical use in cryptography. 
Each cipher attempts to use the most efficent data structures to support achieving the lowest possible computational complexity (often `O(n)`), but none of them have been implemented with the intend to be the fastest implementation. We optimized for readability.

## Features

### Ciphers
The following ciphers have been implemented. The table contains a break down of which functions are implemented for each cipher, and the state of the current implementation.

| Cipher                      | Encrypt | Decrypt | Break | No known issues | Input validation | Has unit tests |
| --------------------------- | ------- | ------- | ----- | --------------- | ---------------- | -------------- |
| Base64                      | ✅       | ✅       | ❌     | ✅               | ❌                | ✅              |
| Bifid                       | ✅       | ✅       | ❌     | ❌               | ❌                | ✅              |
| Caesar                      | ✅       | ✅       | ✅     | ✅               | ✅                | ✅              |
| Columnar Transposition      | ✅       | ✅       | ❌     | ❌               | ❌                | ✅              |
| Fractioned Morse            | ✅       | ✅       | ❌     | ✅               | ✅                | ✅              |
| Hill                        | ✅       | ✅       | ❌     | ✅               | ❌                | ✅              |
| Homophonic Substitution     | ✅       | ✅       | ❌     | ✅               | ✅                | ✅              |
| Monoalphabetic Cipher       | ✅       | ✅       | ❌     | ✅               | ✅                | ✅              |
| One Time Pad                | ✅       | ✅       | ❌     | ✅               | ✅                | ✅              |
| Playfair                    | ✅       | ✅       | ❌     | ❌               | ❌                | ✅              |
| Polyalphabetic Substitution | ✅       | ✅       | ❌     | ❌               | ❌                | ✅              |
| Polybius                    | ✅       | ✅       | ❌     | ✅               | ❌                | ✅              |
| Polygram Substitution       | ✅       | ✅       | ❌     | ✅               | ❌                | ✅              |
| Rail Fence                  | ✅       | ✅       | ❌     | ✅               | ❌                | ✅              |
| Vigenere                    | ✅       | ✅       | ❌     | ✅               | ✅                | ✅              |

### Interfaces
The easiest way to try out a cipher is by using one of the 2 interfaces that are implemented for each cipher. In the future, we might add a HTML interface to allow for easier interaction.

#### CLI
`ciphy` is the binary that executes all our ciphers. This project uses argparse to parse arugments passed to a CLI tool. Follow the installation instructions further down in the readme to see how the command is installed. 

![](docs/cli_recording.gif)

```
ciphy caesar encrypt --message "HELLO" --shift "3"
```


#### REST API
We implemented a REST API on top of all the cipher algorithms. The REST API is using the Flask web framework [running on Heroku](https://cipher-algorithms-d6b034dd885b.herokuapp.com/docs/), and automatically generates an [OpenAPI](https://www.openapis.org/) definition. The webserver also produces three versions of commonly used documentation tools:
- [Swagger docs](https://cipher-algorithms-d6b034dd885b.herokuapp.com/docs/)
- [Redoc](https://cipher-algorithms-d6b034dd885b.herokuapp.com/docs/redoc)
- [Rapidoc](https://cipher-algorithms-d6b034dd885b.herokuapp.com/docs/rapidoc)

The OpenAPI definition will make it easy to publish this API on marketplaces like [Rapid API](https://rapidapi.com/).

Either use one of the automatically generated documentation websites, or use cURL to try out the API:

```
curl --location 'https://cipher-algorithms-d6b034dd885b.herokuapp.com/api/v1/ciphers/caesar/decrypt' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
    "cipher": "Test This Message",
    "shift": "2"
}'
```

### Development environment
This repository has some basic CI set up:
- Github actions runs a linter and all unit tests on each commit for 3 python versions
- Any commit to the Heroku branch start an automated deployment to Heroku
- VS code config has 3 debug configurations set up: debugging the module, debugging the Web interface, debugging a single file






## Development
### Installing the python module and ciphy CLI
1. (optional) 
Create a virtual environment if you don't have one already
```
python3 -m venv .venv
```

Activate the virtual environment
```
source .venv/bin/activate
```
2. Install this package with pip
```
pip install .
```
### Installing dependencies for local development and the REST API
1. (optional) 
Create a virtual environment if you don't have one already
```
python3 -m venv .venv
```

Activate the virtual environment
```
source .venv/bin/activate
```
2. Install dependencies
```
pip install -r requirements.txt
```

## Running the API locally
```
python -m flask --app "api/app.py" run
```

## Running the CLI locally
As a Python module:
```
python -m cipher_algorithms caesar encrypt --message "HELLO" --shift "3"
```
With the CLI:
```
ciphy caesar encrypt --message "HELLO" --shift "3"
```

### Testing
Add tests to the `tests` folder in the root. Run `pytest` to execute all tests.

### Deployment
To deploy to [https://cipher-algorithms-d6b034dd885b.herokuapp.com/](https://cipher-algorithms-d6b034dd885b.herokuapp.com/), create a pull request to the heroku branch. Once the request is merged, a deployment will automatically start. Example: [https://github.com/lswartsenburg/cyber-202-final-project/pull/17](https://github.com/lswartsenburg/cyber-202-final-project/pull/17)

### Example of adding a new algorithm
This is an example commit of adding a new algorithm to the library, including the CLI and REST interface:
[https://github.com/lswartsenburg/cyber-202-final-project/pull/4/files](https://github.com/lswartsenburg/cyber-202-final-project/pull/4/files)