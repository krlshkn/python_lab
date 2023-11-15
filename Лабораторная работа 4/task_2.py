# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    data = []
    with open(INPUT_FILENAME, mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            data.append(row)
        with open(OUTPUT_FILENAME, mode='w') as outfile:
            json.dump(data, outfile, indent=4)
    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
