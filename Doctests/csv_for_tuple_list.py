import csv


def csv_for_tuple_list(path_file):
    with open(path_file, "r") as file:
        content_file = csv.DictReader(file)
        tuple_list = []
        for row in content_file:
            for word in row.items():
                if None not in word:
                    tuple_list.append(word)

    print(tuple_list)


csv_for_tuple_list("text.csv")
