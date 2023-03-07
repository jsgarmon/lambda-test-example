import os
import json


def load_fixture(filename):
    path = os.path.join("./tests/fixtures", filename)

    with open(path, "r") as this:
        event = json.load(this)

    return event
