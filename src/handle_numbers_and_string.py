from typing import List
import json

list_numbers = [1, 2, 5, 8, 100, 20, 65, 89]


def filter_numbers(list_numbers: List[int]):
    filtered_numbers = list(filter(lambda x: x > 10, list_numbers))
    return filtered_numbers


def show_your_input():
    return f"Você digitou: {input('Digite alto: ')}!"


def generate_output(content, path):
    with open(path, "w", encoding="utf-8") as file:
        file.write(json.dumps(content))
