from src.fibo import fib2, fib3


def test_sum_numbers(my_list):
    assert sum(my_list) == 6


def test_fib3():
    result = fib3(8)
    assert result == [0, 1, 1, 2, 3, 5]


def test_fib2():
    result = fib2(10)
    assert result == 55
