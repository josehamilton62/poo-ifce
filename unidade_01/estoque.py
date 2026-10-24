# Arquivo: estoque.py
# Atividade de Revisão de Algoritmos: Aula 01 - Questão 1 (Estoque de Produtos)


def exibir_menu():
    print("\n===== ESTOQUE DA LOJA =====")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Atualizar quantidade")
    print("4 - Exibir estoque")
    print("0 - Sair")


def ler_nome(mensagem):
    while True:
        nome = input(mensagem).strip().title()
        if nome != "":
            return nome
        print("Erro: O nome do produto não pode ficar em branco. Tente novamente.")


def ler_quantidade(mensagem):
    while True:
        entrada = input(mensagem).strip()
        try:
            quantidade = int(entrada)
            if quantidade >= 0:
                return quantidade
            print("Erro: A quantidade deve ser um número inteiro maior ou igual a zero.")
        except ValueError:
            print("Erro: Entrada inválida! Digite apenas números inteiros.")


def adicionar_produto(estoque, nome, quantidade):
    if nome in estoque:
        print(
            f"Aviso: O produto '{nome}' já está cadastrado no estoque. "
            "Utilize a opção 3 (Atualizar quantidade) para alterar seu saldo."
        )
        return False
    estoque[nome] = quantidade
    print(f"Produto '{nome}' adicionado com sucesso ({quantidade} unidade(s)).")
    return True


def remover_produto(estoque, nome):
    if nome in estoque:
        estoque.pop(nome)
        print(f"Produto '{nome}' removido com sucesso.")
        return True
    print(f"Produto '{nome}' não encontrado no estoque.")
    return False


def atualizar_quantidade(estoque, nome, quantidade):
    if nome in estoque:
        estoque[nome] = quantidade
        print(f"Quantidade do produto '{nome}' atualizada com sucesso para {quantidade}.")
        return True
    print(f"Produto '{nome}' não encontrado no estoque.")
    return False


def exibir_estoque(estoque):
    print("\n--- PRODUTOS EM ESTOQUE ---")
    if not estoque:
        print("Estoque vazio")
        return
    for nome, quantidade in estoque.items():
        print(f"- {nome}: {quantidade} unidade(s)")


def main():
    estoque = {}

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = ler_nome("Digite o nome do produto: ")
            quantidade = ler_quantidade("Digite a quantidade inicial: ")
            adicionar_produto(estoque, nome, quantidade)
        elif opcao == "2":
            nome = ler_nome("Digite o nome do produto a remover: ")
            remover_produto(estoque, nome)
        elif opcao == "3":
            nome = ler_nome("Digite o nome do produto a atualizar: ")
            quantidade = ler_quantidade("Digite a nova quantidade: ")
            atualizar_quantidade(estoque, nome, quantidade)
        elif opcao == "4":
            exibir_estoque(estoque)
        elif opcao == "0":
            print("Encerrando o sistema de estoque. Até logo!")
            break
        else:
            print("Opção inválida! Escolha uma opção de 0 a 4.")


if __name__ == "__main__":
    main()