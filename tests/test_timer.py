from pytest import fixture

from python_utils.timer import format_delta


@fixture(scope="module")
def time_value():
    return 3.2132


def test_formatter_no_formatting(time_value):
    delta = format_delta(time_value, digits=-1)

    assert delta == "0:00:03.213200"


def test_formatter_no_microseconds(time_value):
    delta = format_delta(time_value, digits=0)

    assert delta == "0:00:03"


def test_formatter(time_value):
    delta = format_delta(time_value, digits=2)

    assert delta == "0:00:03.21"
