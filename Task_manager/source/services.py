from source.constants import DATABASE_PATH
from source.util.service_util import (
    prepare_values,
    sort_data_base,
)
import json
import sys


def get_all_tasks():
    try:
        with open(DATABASE_PATH, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


DATA_BASE = get_all_tasks()


def get_one_task(id):
    if len(DATA_BASE) > 0:
        for index, value in enumerate(DATA_BASE):
            if DATA_BASE[index]["id"] is id:
                return value
    else:
        return "Sua lista de tarefas está vazia."


def insert_task(title, description):
    new_task = prepare_values(title, description, DATA_BASE)
    DATA_BASE.append(new_task)
    new_data_base = sort_data_base(DATA_BASE)
    with open(DATABASE_PATH, "w") as file:
        file.write(json.dumps(new_data_base))


def update_task(id, task):
    if isinstance(task, dict):
        for index, value in enumerate(DATA_BASE):
            if int(value["id"]) == int(id):
                DATA_BASE[index] = task

        with open(DATABASE_PATH, "w") as file:
            file.write(json.dumps(DATA_BASE))
    else:
        print(task)


def remove_task(id):
    new_data_base = []
    if len(DATA_BASE) > 0:
        for value in DATA_BASE:
            if int(value["id"]) != int(id):
                new_data_base.append(value)
    try:
        with open(DATABASE_PATH, "w") as file:
            file.write(json.dumps(new_data_base))
    except ValueError:
        return "Tarefa inválida."


def completed_task(id):
    for value in DATA_BASE:
        if value["id"] == id:
            value["completed"] = True

    with open(DATABASE_PATH, "w") as file:
        file.write(json.dumps(DATA_BASE))


def exit_app():
    sys.exit(0)
