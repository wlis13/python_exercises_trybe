from constants import DATABASE_PATH
from util.service_util import remove_zero, prepare_values, sort_data_base
import json


def get_all_tasks():
    try:
        with open(DATABASE_PATH, "r") as file:
            content = json.load(file)
            return content
    except json.JSONDecodeError:
        return []


def get_one_task(id):
    content = get_all_tasks()
    if len(content) > 0:
        for index, value in enumerate(content):
            if content[index]["id"] is id:
                return value
    else:
        return "O banco de dados está vazio."


def insert_task(title, description):
    content = get_all_tasks()
    object_value = prepare_values(title, description, content)
    content.append(object_value)
    content = sort_data_base(content)
    with open(DATABASE_PATH, "w") as file:
        file.write(json.dumps(content))


def update_task():
    return True


def remove_task(id):
    content = get_all_tasks()
    new_list = []
    if len(content) > 0:
        for index, value in enumerate(content):
            if content[index]["id"] != remove_zero(id):
                new_list.append(value)

    with open(DATABASE_PATH, "w") as file:
        file.write(json.dumps(new_list))