from source.services import DATA_BASE

from source.services import (
    insert_task,
    completed_task,
    remove_task,
    update_task,
)

from source.util.data_base_util import (
    list_not_complet_task,
    return_formatted_values,
    update_menu,
    handle_update_all_value_task,
    handle_update_one_value_task,
    return_formatted_complete,
    return_title_values,
    return_formatted_data_base_tasks,
    return_formatted_data_base_title_tasks,
)


def db_get_all_tasks():
    if len(DATA_BASE) > 0:
        print("TODAS AS TAREFAS:")
        for index, value in enumerate(DATA_BASE):
            print(f"Índice: ({index + 1})---------------------------")
            print(
                f"""
            Título - {value["title"]}
            Descrição - {value["description"]}
            Completa - {return_formatted_complete(value["completed"])}
            Data de criação - {value["creation_date"]}
                """
            )
    else:
        print(
            """
              -> VOCÊ NÃO TEM TAREFAS. <-
              """
        )


def db_get_one_task():
    return_title_values("ESCOLHA A TAREFA:", DATA_BASE)
    input_title = input("Digite o número da tarefa desejada: ")

    value_task = [
        task for task in DATA_BASE if int(task["id"]) == int(input_title)
    ][0]
    print("TAREFA SELECIONADA:")
    print(return_formatted_values(value_task))


def db_insert_task():
    title = input("Digite o título da nova tarefa: ")
    description = input("Digite a descrição da nova tarefa: ")
    insert_task(title, description)


def db_completed_task():
    tasks_not_complet = list_not_complet_task(DATA_BASE)
    return_title_values("TODAS AS TAREFAS INCOMPLETAS", tasks_not_complet)

    get_input = input(
        "Digite o número referente a função que você deseja completar: "
    )
    choosed_task = tasks_not_complet[int(get_input) - 1]["id"]
    completed_task(choosed_task)


def db_update_task():
    return_formatted_data_base_title_tasks(DATA_BASE)

    input_title = int(input("Digite o número da tarefa desejada: "))
    print("Dados atuais da tarefa:")
    print(return_formatted_values(DATA_BASE[input_title - 1]))
    update_menu()
    selected_option_menu = input("Digite a opção de atualização: ")
    if selected_option_menu == "1":
        task = handle_update_all_value_task(
            selected_option_menu, DATA_BASE[input_title - 1]
        )
        update_task(task["id"], task)

    elif selected_option_menu == "2":
        task = handle_update_one_value_task(
            selected_option_menu, DATA_BASE[input_title - 1]
        )
        update_task(task["id"], task)
    else:
        print("Opção inválida.")


def db_list_not_complet_tasks():
    not_complet_task = list_not_complet_task(DATA_BASE)
    print(" TAREFAS INCOMPLETAS:")
    print(return_formatted_data_base_tasks(not_complet_task))


def db_remove_task():
    return_formatted_data_base_tasks(DATA_BASE)
    input_id = input("Digite o Índice da tafefa que você quer remover: ")
    for value in DATA_BASE:
        if int(value["id"]) is int(input_id):
            remove_task(value["id"])
        else:
            return "A tarefa não existe."
