import json
from functools import cache
from importlib.resources import files

@cache
def _load():
    return json.loads(files("thermo_py").joinpath("data/thermo_data.json").read_text())

def get(compound, section):
    entry = _load().get(compound)
    if entry is None:
        raise KeyError(f"{compound} NOT FOUND")
    if section not in entry:
        raise KeyError(f"{compound} HAS NO ATTRIBUTE {section}")
    return entry[section]