import pytest

from python_utils.iterables import batched


@pytest.fixture(scope="module")
def data():
    return [150] * 50


def test_batched_even(data):
    for batch in batched(data, 50):
        assert len(batch) == 50

def test_batched_uneven(data):
    for index, batch in enumerate(batched(data, 32)):
        if index == 1:
            assert len(batch) == 18
        else:
            assert len(batch) == 32

