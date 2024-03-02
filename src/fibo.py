from typing import List


def fib(n: int):
    a, b = 0, 1
    while a < n:
        print(a, end=", ")
        a, b = b, a + b


def fib2(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib2(n - 1) + fib2(n - 2)


def fib3(n: int) -> List[int]:
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b

    return result


print(fib3(500))
