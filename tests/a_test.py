import csv


def test_sum_numbers():
    assert sum([1, 2, 3]) == 6


def test_sum_elements():
    assert [num * 3 for num in [1, 2, 3]] == [3, 6, 9]


def test_csv_for_tuple_list():
    text = "test_text.csv"
    with open(text, "r") as file:
        content_file = csv.DictReader(file)
        content_tuple = []
        for dict in content_file:
            for word in dict.items():
                content_tuple.append(word)
    assert content_tuple == [
        ("largura", "55"),
        (" altura", " 70"),
        (" tecido", " Aldodão"),
    ]
