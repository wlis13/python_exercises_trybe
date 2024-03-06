from ...src.analyzer import analyze_json_file, read_json_file
from unittest.mock import patch


def test_analyze_json_file():

    with patch("builtins.open") as mock_open:
        mock_open.return_value.__enter__.return_value.read.return_value = (
            '{"nome": "Maria", "idade": 31}'
        )

        first_result = analyze_json_file("invalid.json")
        assert first_result == "A pessoa do nome: Maria tem 31 anos de idade."

    with patch("builtins.open") as mock_open:
        mock_open.return_value.__enter__.return_value.read.return_value = (
            '{"nome": "Agenor", "idade": 86}'
        )

        second_result = analyze_json_file("invalid.json")
        assert second_result == "A pessoa do nome: Agenor tem 86 anos de idade."
