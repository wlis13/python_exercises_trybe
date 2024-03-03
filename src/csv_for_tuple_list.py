import csv
from typing import List, Dict


def csv_for_tuple_list_file(path_file):
    with open(path_file, "r") as file:
        content_file = csv.DictReader(file)
        tuple_list = []
        for row in content_file:
            for tn in row.items():
                tuple_list.append(tn)

    return tuple_list


def csv_for_list(path_file):
    with open(path_file, "r") as file:
        content_file = csv.reader(file)
        value = []
        for v in content_file:
            value.append(v)

        return value


def prime_numbers(numbers: List[int]) -> Dict[str, str]:
    result = {}
    for num in numbers:
        if num <= 1:
            result[f"{num}"] = "Não é primo"
        else:
            count = 0
            for tn in range(2, int(num**0.5) + 1):
                if num % tn == 0:
                    count += 1
            if count > 0:
                result[f"{num}"] = "Não é primo."
            else:
                result[f"{num}"] = "É primo."

    return result
