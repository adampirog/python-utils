import pytest

from python_utils.basic_io import load_json, load_txt, save_json, save_txt


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
