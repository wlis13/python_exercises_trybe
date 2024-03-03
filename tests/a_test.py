from ..src.fibo import fib2, fib3
from ..src.other_modules.asterisks import asterisks, other_asterisks
from ..src.handle_numbers_and_string import generate_output
import os
import pytest
import sys


def test_sum_numbers(my_list):
    assert sum(my_list) == 6


def test_fib3():
    result = fib3(8)
    assert result == [0, 1, 1, 2, 3, 5]


@pytest.mark.skip(reason="Somente para teste")
def test_fib2():
    result = fib2(10)
    assert result == 55


@pytest.mark.skipif(sys.platform == "windows", reason="Não suportado no windowns")
def test_asterisks(high_list):
    result = asterisks(high_list)
    assert result == "*****\n*****\n*****\n*****\n*****"


def test_other_asteriks():
    result = other_asterisks(5)
    assert result == "*****\n*****\n*****\n*****\n*****"


def test_generate_output(tmp_path):
    content = {"a": 1}
    output_path = tmp_path / "tes_path_lib.json"

    generate_output(content, output_path)

    assert os.path.isfile(output_path)
    with open(output_path, "r") as file:
        assert file.read() == '{"a": 1}'
