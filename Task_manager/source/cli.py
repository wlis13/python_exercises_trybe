from services import exit_app, update_task, get_all_tasks
from data_base import db_insert_task, db_completed_task, db_get_one_task


def get_options():
    return (
        {"Sair", exit_app},
        {"Adicionar tarefa", db_insert_task},
        {"Completar tarefa", db_completed_task},
        {"Atualizar tarefa", update_task},
        {"Listar todas as tarefas", get_all_tasks},
        {"Listar uma tarefa", db_get_one_task},
        {"Listar tarefas pendêntes"},
        {"Deletar tarefa"},
    )


def main():
    while True:
        print("> Opções:")
        print("")
        for index, option in enumerate(get_options()):
            print(f"{index + 1}: {option[0]}")

        selected_option = int(input("> Digite a opção desejada: "))
        try:
            selected_option = get_options()[selected_option][1]
            selected_option()
        except IndexError:
            print("> Opção inválida")


if __name__ == "__main__":
    main()
