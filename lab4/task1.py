import json

INPUT_FILE = "input.json"

def task() -> float:
    with open(INPUT_FILE, "r") as f:
        data = json.load(f)
    multiplyings = [dict_["score"] * dict_["weight"] for dict_ in data]
    return round(sum(multiplyings), 3)


print(task())
