def list_not_complet_task(content):
    tasks = [task for task in content if task["completed"] is False]
    return tasks


def return_formatted_complete(value):
    if value is False:
        return "Não"
    else:
        return "Sim"


def return_formatted_values(task):
    return f"""
    Título - {task["title"]}
    Descrição - {task["description"]}
    Completa - {return_formatted_complete(task["completed"])}
    Data de criação - {task["creation_date"]}
    """


def return_title_values(title, data_base):
    print(title)
    print()
    for index, data in enumerate(data_base):
        print(f"{index + 1} - {data['title']}")
    print()


def return_formatted_data_base_tasks(data_base):
    for index, value in enumerate(data_base):
        print(
            f"""
        Índice: {index + 1}
        Título - {value["title"]}
        Descrição - {value["description"]}
        Completa? - {return_formatted_complete(value["completed"])}
        Data de criação - {value["creation_date"]}
        """
        )


def return_formatted_data_base_title_tasks(data_base):
    if len(data_base) > 0:
        for index, value in enumerate(data_base):
            print(f"Índice: {index + 1} -> Título - {value['title']}")
    else:
        print("VOCÊ NÃO TEM TAREFAS.")


def update_menu():
    print(
        """
    1 - Alterar todos os dados
    2 - Alterar um dos dados
    3 - Manter os dados atuais
    """
    )


def handle_boolean_value(value):
    if value == "1":
        return True
    elif value == "2":
        return False
    else:
        return "Opção inválida."


def handle_add_value_task(task, new_title, new_description, new_completed):
    task["title"] = new_title
    task["description"] = new_description
    task["completed"] = new_completed
    return task


def handle_update_all_value_task(input_value, task):
    if input_value == "1":
        new_title = input("Digite o novo título: ")
        new_description = input("Digite a nova descrição: ")
        print("A tarefa está completa?")
        print("1 - Sim")
        print("2 - Não")
        new_completed = input("Digite 1 para Sim e 2 para Não: ")
        return handle_add_value_task(
            task,
            new_title,
            new_description,
            handle_boolean_value(new_completed),
        )
    else:
        return "Opção inválida."


def handle_select_title(title, task):
    task["title"] = title
    return task


def handle_select_description(description, task):
    task["description"] = description
    return task


def handle_select_completed(completed, task):
    if completed == "1":
        task["completed"] = True
        return task
    elif completed == "2":
        task["completed"] = False
        return task
    else:
        print("Opção inválida.")


def handle_update_one_value_task(input_value, task):
    if input_value == "2":
        print("1 - Título")
        print("2 - Descrição")
        print("3 - Completa")
        selected_option = input(
            "Escolha qual informação você quer atualizar: "
        )
        if selected_option == "1":
            title = input("Digite o novo título: ")
            return handle_select_title(title, task)
        elif selected_option == "2":
            description = input("Digite a nova descrição: ")
            return handle_select_description(description, task)
        elif selected_option == "3":
            print("A tarefa está completa?")
            print("1 - Sim")
            print("2 - Não")
            completed = input("Digite 1 para Sim e 2 para Não: ")
            return handle_select_completed(completed, task)
        else:
            return "Opção inválida."
