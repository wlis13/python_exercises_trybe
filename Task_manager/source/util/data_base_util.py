def list_not_complet_task(content):
    tasks = [task for task in content if task["completed"] is False]
    return tasks
