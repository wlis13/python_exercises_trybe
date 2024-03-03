from typing import List


def asterisks(list: List[int]) -> str:
    result = ""
    for n in list:
        result += "*" * len(list)
        if n < len(list):
            result += "\n"
    return result


def other_asterisks(number: int) -> str:
    result = ""
    for n in range(number):
        for _ in range(number):
            result += "*"

        if n < number - 1:
            result += "\n"

    return result
