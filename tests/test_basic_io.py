from dataclasses import dataclass
from datetime import datetime

import numpy as np
import pytest

from python_utils.basic_io import load_json, load_txt, save_json, save_txt


@dataclass
class DataClass:
    name: str
    value: int


@pytest.fixture(scope="module")
def text() -> list[str]:
    return ["This is a random text"] * 10


def test_txt(tmpdir, text):
    file = tmpdir.mkdir("test").join("file.txt")

    save_txt(text, file)
    restored = load_txt(file)

    assert text == restored


def test_json(tmpdir, text):
    values = [150] * 10
    data = dict(zip(text, values))
    file = tmpdir.mkdir("test").join("file.json")

    save_json(data, file)
    restored = load_json(file)

    assert data == restored


def test_json_numpy_array(tmpdir):
    data = np.arange(10)
    file = tmpdir.mkdir("test").join("file.json")

    save_json(data, file)
    restored = load_json(file)

    assert restored == list(range(10))


def test_json_numpy_float(tmpdir):
    original = [3.123] * 10
    data = np.array(original)
    file = tmpdir.mkdir("test").join("file.json")

    save_json(data, file)
    restored = load_json(file)

    assert restored == original


def test_json_datetime(tmpdir):
    data = datetime(2023, 10, 11, 12, 53)
    file = tmpdir.mkdir("test").join("file.json")

    save_json(data, file)
    restored = load_json(file)

    assert restored == "2023-10-11T12:53:00"


def test_json_dataclass(tmpdir):
    data = DataClass("test", 5)
    file = tmpdir.mkdir("test").join("file.json")

    save_json(data, file)
    restored = load_json(file)

    assert restored == {"name": "test", "value": 5}
