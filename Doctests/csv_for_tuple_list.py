import csv
from typing import List, Dict


def csv_for_tuple_list(path_file):
    with open(path_file, "r") as file:
        content_file = csv.DictReader(file)
        tuple_list = []
        for row in content_file:
            for word in row.items():
                if None not in word:
                    tuple_list.append(word)

    print(tuple_list)


# csv_for_tuple_list("text.csv")


def csv_for_list(path_file):
    with open(path_file, "r") as file:
        content_file = csv.reader(file)
        result = []
        characters_word = []

        for line in content_file:
            print(line)
            for word in line:
                result.append(word)
                for cha in word:
                    characters_word.append(cha)

        print(f"words: ${result}")
        print(f"caracteres: ${characters_word}")


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

    print(result)


prime_numbers([1, 2, 6, 4, 8, 9, 11, 15, 16, 23, 45])
