# Arquivo: tarefas.py
# Atividade de Revisão de Algoritmos: Aula 01 - Questão 3 (Controle de Tarefas)


def exibir_menu():
    print("\n===== CONTROLE DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Marcar tarefa como concluída")
    print("3 - Listar tarefas")
    print("0 - Sair")


def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto != "":
            return texto
        print("Erro: Este campo não pode ficar vazio. Tente novamente.")


def buscar_tarefa(tarefas, titulo):
    titulo_normalizado = titulo.strip().lower()
    for tarefa in tarefas:
        if tarefa["titulo"].strip().lower() == titulo_normalizado:
            return tarefa
    return None


def adicionar_tarefa(tarefas, titulo, descricao):
    if buscar_tarefa(tarefas, titulo) is not None:
        print(f"Aviso: A tarefa '{titulo}' já existe na lista.")
        return False

    nova_tarefa = {
        "titulo": titulo.strip(),
        "descricao": descricao.strip(),
        "status": "Pendente",
    }
    tarefas.append(nova_tarefa)
    print(f"Tarefa '{titulo}' adicionada com sucesso.")
    return True


def concluir_tarefa(tarefas, titulo):
    tarefa = buscar_tarefa(tarefas, titulo)
    if tarefa is None:
        print(f"Tarefa '{titulo}' não encontrada.")
        return False

    if tarefa["status"] == "Concluído":
        print(f"Aviso: A tarefa '{tarefa['titulo']}' já está concluída.")
        return False

    tarefa["status"] = "Concluído"
    print(f"Tarefa '{tarefa['titulo']}' marcada como concluída com sucesso.")
    return True


def listar_tarefas(tarefas):
    pendentes = []
    concluidas = []

    for tarefa in tarefas:
        if tarefa["status"] == "Pendente":
            pendentes.append(tarefa)
        else:
            concluidas.append(tarefa)

    print(f"\nPENDENTES ({len(pendentes)})")
    if not pendentes:
        print("Nenhuma tarefa")
    else:
        for indice, tarefa in enumerate(pendentes, start=1):
            print(f"{indice}. {tarefa['titulo']}: {tarefa['descricao']}")

    print(f"\nCONCLUÍDAS ({len(concluidas)})")
    if not concluidas:
        print("Nenhuma tarefa")
    else:
        for indice, tarefa in enumerate(concluidas, start=1):
            print(f"{indice}. {tarefa['titulo']}: {tarefa['descricao']}")


def main():
    tarefas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            titulo = ler_texto("Digite o título da tarefa: ")
            descricao = ler_texto("Digite a descrição da tarefa: ")
            adicionar_tarefa(tarefas, titulo, descricao)
        elif opcao == "2":
            titulo = ler_texto("Digite o título da tarefa a concluir: ")
            concluir_tarefa(tarefas, titulo)
        elif opcao == "3":
            listar_tarefas(tarefas)
        elif opcao == "0":
            print("Encerrando o controle de tarefas. Até logo!")
            break
        else:
            print("Opção inválida! Escolha uma opção de 0 a 3.")


if __name__ == "__main__":
    main()