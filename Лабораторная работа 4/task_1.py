# TODO решите задачу
import json


def task() -> float:
    with open("input.json") as file:
        list = json.load(file)
        summ = sum(map(lambda pair: pair["score"] * pair["weight"], list))
    return round(summ, 3)


print(task())
