from unittest.mock import patch
from ...tests.Mock_unittest.mock_json import (
    alberto_mock_file_json,
    agenor_mock_file_json,
    maria_mock_file_json,
)
from ...src.analyzer import analyze_json_file, read_json_file
import pytest


def test_analyze_json_file():
    with patch("builtins.open") as mock_file:
        mock_file.return_value.__enter__.return_value.read.return_value = (
            maria_mock_file_json
        )

        assert (
            analyze_json_file("invalid.json")
            == "A pessoa do nome: Maria tem 30 anos de idade."
        )

    with patch("builtins.open") as mock_file:
        mock_file.return_value.__enter__.return_value.read.return_value = (
            alberto_mock_file_json
        )
        assert (
            analyze_json_file("invalid.json")
            == "A pessoa do nome: Alberto tem 56 anos de idade."
        )
        mock_file.assert_called_with("invalid.json", "r")


def test_analyzer_json_file_propagates_exception():
    with pytest.raises(FileNotFoundError):
        assert analyze_json_file("invalid.json")

    with patch("builtins.open") as mock_file:
        mock_file.return_value.__enter__.return_value.read.return_value = (
            agenor_mock_file_json
        )
        with pytest.raises(ValueError):
            assert analyze_json_file("invalid.txt")


def test_read_json_file():
    with patch("builtins.open") as mock_file:
        mock_file.return_value.__enter__.return_value.read.return_value = (
            '{"nome": "Maria", "idade": 31}'
        )

        result = read_json_file("invalid.json")
        assert result == {"nome": "Maria", "idade": 31}
        mock_file.assert_called_with("invalid.json", "r")
