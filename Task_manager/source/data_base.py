from services import insert_task, get_all_tasks, completed_task
from util.data_base_util import list_not_complet_task


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
    choosed_task = tasks_not_complet[get_input]["id"]
    completed_task(choosed_task)


def db_get_one_task():
    content = get_all_tasks()
    input_title = input("Digite o título da tarefa desejada: ")

    return [task for task in content if task["title"] == input_title][0]
