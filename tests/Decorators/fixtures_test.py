from ...src.handle_numbers_and_string import show_your_input


def test_print_to_stdout(capsys):
    print("Hello World!")
    captured = capsys.readouterr()
    assert captured.out == "Hello World!\n"


def test_error_to_stderr(capsys):
    import sys

    sys.stderr.write("Error message\n")
    captured = capsys.readouterr()
    assert captured.err == "Error message\n"


def test_show_your_digit(monkeypatch):
    def mock_input(_):
        return "Python"

    monkeypatch.setattr("builtins.input", mock_input)
    output = show_your_input()
    assert output == "Você digitou: Python!"
