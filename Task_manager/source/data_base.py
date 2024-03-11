from source.services import (
    insert_task,
    get_all_tasks,
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
    return_formatted_list_value,
    return_title_values,
)


def db_get_all_tasks():
    content = get_all_tasks()
    print("TODAS AS TAREFAS:")
    for index, value in enumerate(content):
        print(f"Índice: ({index + 1})---------------------------")
        print(
            f"""
        Título - {value["title"]}
        Descrição - {value["description"]}
        Completa - {return_formatted_list_value(value["completed"])}
            """
        )


def db_get_one_task():
    content = get_all_tasks()
    return_title_values("ESCOLHA A TAREFA:", content)
    input_title = input("Digite o número da tarefa desejada: ")

    value_task = [
        task for task in content if int(task["id"]) == int(input_title)
    ][0]
    print("TAREFA SELECIONADA:")
    print(return_formatted_values(value_task))


def db_insert_task():
    title = input("Digite o título da nova tarefa: ")
    description = input("Digite a descrição da nova tarefa: ")
    insert_task(title, description)


def db_completed_task():
    content = get_all_tasks()
    tasks_not_complet = list_not_complet_task(content)
    return_title_values("TODAS AS TAREFAS INCOMPLETAS", tasks_not_complet)

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
    update_menu()
    selected_option_menu = input("Digite a opção de atualização: ")
    if selected_option_menu == "1":
        list_options = handle_update_all_value_task(selected_option_menu)
        update_task(
            content[input_title - 1]["id"],
            list_options[0],
            list_options[1],
            list_options[2],
        )
    elif selected_option_menu == "2":
        task = handle_update_one_value_task(
            selected_option_menu, content[input_title - 1]
        )
        update_task(
            task["id"],
            task["title"],
            task["description"],
            task["completed"],
        )
    else:
        print("Opção inválida.")


def db_list_not_complet_tasks():
    content = get_all_tasks()
    not_complet_task = list_not_complet_task(content)
    for value in not_complet_task:
        print(
            f"""
        TAREFAS INCOMPLETAS:

        {value['title']}
        {value['description']}
        {return_formatted_list_value(value['completed'])}
        """
        )


def db_remove_task():
    content = get_all_tasks()
    input_id = input("Digite o título da tafefa que você quer remover: ")
    for value in content:
        if int(value["id"]) == int(input_id):
            remove_task(value["id"])
        else:
            return "A tarefa não existe."
