def list_not_complet_task(content):
    tasks = [task for task in content if task["completed"] is False]
    return tasks


def return_formatted_values(task):
    if task["completed"] is False:
        completed = "Não"
    else:
        completed = "Sim"
    return f"""
    Título - {task["title"]}
    Descrição - {task["description"]}
    Completa - {completed}
    """
