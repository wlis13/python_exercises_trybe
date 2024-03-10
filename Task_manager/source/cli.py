from source.services import (
    exit_app,
    update_task,
)
from source.data_base import (
    db_insert_task,
    db_completed_task,
    db_get_one_task,
    db_list_not_complet_tasks,
    db_remove_task,
    db_get_all_tasks,
)


def get_options():
    return (
        ["Sair", exit_app],
        ["Adicionar tarefa", db_insert_task],
        ["Completar tarefa", db_completed_task],
        ["Atualizar tarefa", update_task],
        ["Listar todas as tarefas", db_get_all_tasks],
        ["Listar uma tarefa", db_get_one_task],
        ["Listar tarefas pendêntes", db_list_not_complet_tasks],
        ["Deletar tarefa", db_remove_task],
    )


def main():
    while True:
        print("> Opções:")
        print("")
        for index, option in enumerate(get_options()):
            print(f"{index + 1}: {option[0]}")

        selected_option = int(input("> Digite a opção desejada: "))
        try:
            selected_option = get_options()[selected_option - 1][1]
            selected_option()
        except IndexError:
            print("> Opção inválida")


if __name__ == "__main__":
    main()
