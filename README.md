# Cipher Algorithms


## Development

### Running the code
The recommended development tool is Visual Studio. 

#### VS code
1. Install this package with pip
```
pip3 install .
```
2. Update launch.json with command line arguments
3. Run the debugger (F5)

#### Other
1. Install this package with pip
```
pip3 install .
```
2. Use python to execute the CLI from the root of the project. Example:
```
python cipher_algorithms/main.py caesar break --cipher "WHVWCWKLVCPHVVDJH"
```

### Testing
Add tests to the `tests` folder in the root. Run `pytest tests` to execute all tests.

### Example of adding a new algorithm
This is an example commit of adding a new algorithm to the library:
https://github.com/lswartsenburg/cyber-202-final-project/pull/4/files