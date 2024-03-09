def get_options():
    return (
        "Sair",
        "Adicionar tarefa",
        "Completar tarefa",
        "Listar todas as tarefas",
        "Listar tarefas pendêntes",
        "Deletar tarefa",
    )


def main():
    print("> Opções:")
    print("")
    for index, option in enumerate(get_options()):
        print(f"{index}: {option}")

    selected_option = int(input("> Digite a opção desejada: "))

    try:
        print(selected_option)
    except IndexError:
        print("> Opção inválida")


if __name__ == "__main__":
    main()
