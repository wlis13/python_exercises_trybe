from typing import List

list_numbers = [1, 2, 5, 8, 100, 20, 65, 89]


def filter_numbers(list_numbers: List[int]):
    filtered_numbers = list(filter(lambda x: x > 10, list_numbers))
    print(filtered_numbers)


filter_numbers(list_numbers)
