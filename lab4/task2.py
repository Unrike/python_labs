import json, csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as f:
        reader = csv.DictReader(f)
        list_ = []
        for row in reader:
            dict_ ={fieldname: row[fieldname] for fieldname in reader.fieldnames}
            list_.append(dict_)

    with open(OUTPUT_FILENAME, "w") as out:
        json.dump(list_, out, indent=4)



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
