from pathlib import Path

import pytest

from python_utils.clear_hidden import clear_hidden


@pytest.fixture(scope="function")
def directory(tmp_path) -> Path:

    (tmp_path / ".ipynb_checkpoints").mkdir()
    (tmp_path / "__pycache__").mkdir()
    (tmp_path / "dummy").mkdir()

    subdir = tmp_path / "subdir"
    subdir.mkdir()

    (subdir / ".ipynb_checkpoints").mkdir()
    (subdir / "__pycache__").mkdir()
    (subdir / "dummy").mkdir()

    return tmp_path


def test_clear_flat(directory):
    clear_hidden(directory, recursive=False)

    result = list(directory.rglob("*"))

    assert len(result) == 5
    for item in directory.glob("*"):
        assert "py" not in item.name


def test_clear_recursive(directory):
    clear_hidden(directory, recursive=True)

    result = list(directory.rglob("*"))

    assert len(result) == 3
    for item in result:
        assert "py" not in item.name
