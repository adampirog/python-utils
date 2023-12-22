import pytest

from python_utils.imports import import_module


MODULE_CODE = """

def double(x):
    return x * 2
"""


@pytest.fixture(scope="module")
def python_file(tmpdir_factory) -> str:
    file = tmpdir_factory.mktemp("data").join("file.py")
    with open(file, "wt", encoding="utf-8") as handle:
        handle.write(MODULE_CODE)

    return str(file)


def test_import_module(python_file):
    module = import_module(python_file)
    func = getattr(module, "double")

    assert func
    assert func(3) == 6
