import json


def read_json_file(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def analyze_json_file(file_path) -> str:
    if not file_path.endswith(".json"):
        raise ValueError("O arquivo precise ser um aquivo JSON")

    data = read_json_file(file_path)
    return (
        f"A pessoa do nome: {data['nome']} "
        f"tem {data['idade']} anos de idade."
    )
