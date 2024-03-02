from typing import List


def sum_two_numbers(a, b):
    """Retorna a soma de dois números recebidos por parâmetro

    Exemplos
    --------
    >>> sum_two_numbers(0,0)
    0
    >>> sum_two_numbers(2, 2)
    4
    """
    return a + b


def mean(numbers: List[int]) -> float:
    """
    Calcula a média de uma lista de números.

    >>> my_list = [1, 2, 3, 4, 5]
    >>> mean(my_list)
    3.0
    >>> mean([2.5, 3.75, 1.25, 4])
    2.875
    >>> mean([])
    Divisão por zero.
    """
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        print("Divisão por zero.")


def sum_list(list: List[int]) -> int:
    """
    Retorna a soma dos inteiros de uma lista
    >>> sum_list([1,2,3,4,5])
    15
    >>> sum_list([45, 45, 10, 50])
    150
    """
    total = 0
    for n in list:
        total += n

    return total
