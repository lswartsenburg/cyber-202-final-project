from importlib_resources import files


def get_dictionary():
    data_text = files("data").joinpath("10000words.txt").read_text()
    lines = [line.rstrip() for line in data_text.splitlines()]
    return set(lines)
