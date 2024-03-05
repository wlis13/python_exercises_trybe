import pytest
from ..Doctests.main import mean
import sys


@pytest.mark.parametrize(
    "input_numbers, expected_result",
    [
        ([1, 2, 3, 4, 5], 3.0),
        pytest.param(
            [2.5, 3.75, 1.25, 4],
            2.875,
            marks=pytest.mark.skipif(
                sys.platform == "linux", reason="teste com marcador condicional"
            ),
            id="test_with_mark",
        ),
        ([8, 6, 3, 5], 5.5),
    ],
)
def test_mean(input_numbers, expected_result):
    assert mean(input_numbers) == expected_result


def test_mean_fail():
    with pytest.raises(ZeroDivisionError):
        mean([])
