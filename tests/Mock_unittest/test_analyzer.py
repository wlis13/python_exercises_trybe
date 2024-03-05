from ...src.analyzer import analyze_json_file
from unittest.mock import patch


def test_analyze_json_file():

    with patch("builtins.open") as mock_open:
        mock_open.return_value.__enter__.return_value.read.return_value = (
            '{"nome": "Maria", "idade": 31}'
        )

        result = analyze_json_file("invalid.json")

        assert result == "A pessoa do nome: Maria tem 31 anos de idade."


# def test_second_analyzer_json_file():
#     mock_read_json_file = Mock(return_value={"nome": "Maria", "idade": 31})
#     invalid_json = "invalid.json"

#     with patch("analyzer.read_json_file", mock_read_json_file):
#         result = analyze_json_file(invalid_json)
#         assert result == "A pessoa do nome: Maria tem 31 anos de idade."
#   mock_read_json_file.assert_called_with(fake_file_path)
