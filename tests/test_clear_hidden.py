from pathlib import Path

import pytest

from python_utils.clear_hidden import clear_hidden


@pytest.fixture(scope="function")
def directory(tmpdir_factory) -> Path:
    root = Path(tmpdir_factory.mktemp("data"))

    (root / ".ipynb_checkpoints").mkdir()
    (root / "__pycache__").mkdir()
    (root / "dummy").mkdir()

    subdir = root / "subdir"
    subdir.mkdir()

    (subdir / ".ipynb_checkpoints").mkdir()
    (subdir / "__pycache__").mkdir()
    (subdir / "dummy").mkdir()

    return root


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
