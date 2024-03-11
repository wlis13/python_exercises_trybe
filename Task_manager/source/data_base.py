from source.services import (
    insert_task,
    get_all_tasks,
    completed_task,
    remove_task,
)
from source.util.data_base_util import (
    list_not_complet_task,
    return_formatted_values,
)


def db_get_all_tasks():
    content = get_all_tasks()
    for value in content:
        print(
            f"""
            Título - {value["title"]}
            Descrição - {value["description"]}
            Completa - {str(value["completed"]).upper()}
            """
        )


def db_insert_task():
    title = input("Digite o título da nova tarefa: ")
    description = input("Digite a descrição da nova tarefa: ")
    insert_task(title, description)


def db_completed_task():
    content = get_all_tasks()
    tasks_not_complet = list_not_complet_task(content)
    for index, value in enumerate(tasks_not_complet):
        print(f"{index + 1} - {value['title']}")

    get_input = input(
        "Digite o número referente a função que você deseja completar: "
    )
    choosed_task = tasks_not_complet[int(get_input) - 1]["id"]
    completed_task(choosed_task)


def db_update_task():
    content = get_all_tasks()
    for index, value in enumerate(content):
        print(f"{index + 1} - Título - {value['title']}")

    input_title = int(input("Digite o número da tarefa desejada: "))
    print("Dados atuais da tarefa:")
    print(return_formatted_values(content[input_title - 1]))


def db_get_one_task():
    content = get_all_tasks()
    input_title = input("Digite o título da tarefa desejada: ")

    return [task for task in content if task["title"] == input_title][0]


def db_list_not_complet_tasks():
    content = get_all_tasks()
    return list_not_complet_task(content)


def db_remove_task():
    content = get_all_tasks()
    input_title = input("Digite o título da tafefa que você quer remover: ")
    for value in content:
        if value["title"] == input_title:
            remove_task(value["id"])
        else:
            return "A tarefa não existe."
