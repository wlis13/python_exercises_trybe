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


def get_one_task(id):
    content = get_all_tasks()
    if len(content) > 0:
        for index, value in enumerate(content):
            if content[index]["id"] is id:
                return value
    else:
        return "Sua lista de tarefas está vazia."


def insert_task(title, description):
    content = get_all_tasks()
    new_task = prepare_values(title, description, content)
    content.append(new_task)
    content = sort_data_base(content)
    with open(DATABASE_PATH, "w") as file:
        file.write(json.dumps(content))


def update_task(id, task):
    if isinstance(task, dict):
        content = get_all_tasks()
        for index, value in enumerate(content):
            if int(value["id"]) == int(id):
                content[index] = task

        with open(DATABASE_PATH, "w") as file:
            file.write(json.dumps(content))
    else:
        print(task)


def remove_task(id):
    content = get_all_tasks()
    new_list = []
    if len(content) > 0:
        for value in content:
            if int(value["id"]) != int(id):
                new_list.append(value)
    try:
        with open(DATABASE_PATH, "w") as file:
            file.write(json.dumps(new_list))
    except ValueError:
        return "Tarefa inválida."


def completed_task(id):
    content = get_all_tasks()
    for index, value in enumerate(content):
        if value["id"] == id:
            content[index]["completed"] = True

    with open(DATABASE_PATH, "w") as file:
        file.write(json.dumps(content))


def exit_app():
    sys.exit(0)
