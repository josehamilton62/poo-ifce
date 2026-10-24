# Arquivo: alunos.py
# Atividade de Revisão de Algoritmos: Aula 01 - Questão 2 (Cadastro de Alunos e Notas)


def exibir_menu():
    print("\n===== CADASTRO DE ALUNOS =====")
    print("1 - Adicionar aluno")
    print("2 - Atualizar notas")
    print("3 - Remover aluno")
    print("4 - Exibir alunos e notas")
    print("5 - Exibir médias")
    print("0 - Sair")


def ler_nome(mensagem):
    while True:
        nome = input(mensagem).strip().title()
        if nome != "":
            return nome
        print("Erro: O nome do aluno não pode ficar em branco. Tente novamente.")


def ler_nota(mensagem):
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            nota = float(entrada)
            if 0.0 <= nota <= 10.0:
                return nota
            print("Erro: A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Erro: Entrada inválida! Digite um número válido (ex.: 7.5).")


def ler_quatro_notas():
    notas = []
    for i in range(1, 5):
        nota = ler_nota(f"Digite a nota N{i} (0 a 10): ")
        notas.append(nota)
    return notas


def adicionar_aluno(alunos, nome, notas):
    if nome in alunos:
        print(
            f"Aviso: O(A) aluno(a) '{nome}' já está cadastrado(a). "
            "Utilize a opção 2 (Atualizar notas) para alterar suas notas."
        )
        return False
    alunos[nome] = notas
    print(f"Aluno(a) '{nome}' cadastrado(a) com sucesso.")
    return True


def atualizar_notas(alunos, nome, notas):
    if nome in alunos:
        alunos[nome] = notas
        print(f"Notas de '{nome}' atualizadas com sucesso.")
        return True
    print(f"Aluno(a) '{nome}' não encontrado(a).")
    return False


def remover_aluno(alunos, nome):
    if nome in alunos:
        del alunos[nome]
        print(f"Aluno(a) '{nome}' removido(a) com sucesso.")
        return True
    print(f"Aluno(a) '{nome}' não encontrado(a).")
    return False


def calcular_media(notas):
    return sum(notas) / len(notas)


def exibir_alunos(alunos):
    print("\n--- ALUNOS E NOTAS ---")
    if not alunos:
        print("Nenhum aluno cadastrado")
        return
    for nome, notas in alunos.items():
        notas_formatadas = ", ".join(f"{n:.2f}" for n in notas)
        print(f"- {nome}: [{notas_formatadas}]")


def exibir_medias(alunos):
    print("\n--- MÉDIAS DOS ALUNOS ---")
    if not alunos:
        print("Nenhum aluno cadastrado")
        return
    for nome, notas in alunos.items():
        media = calcular_media(notas)
        print(f"- {nome}: Média = {media:.2f}")


def main():
    alunos = {
        "Ana": [8.5, 7.0, 9.2, 6.8],
        "Carlos": [5.5, 6.0, 7.5, 8.0],
        "Mariana": [9.0, 8.5, 10.0, 9.8],
        "Lucas": [6.5, 7.2, 5.8, 6.9],
        "Fernanda": [7.8, 8.2, 7.0, 8.5],
    }

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = ler_nome("Digite o nome do aluno: ")
            notas = ler_quatro_notas()
            adicionar_aluno(alunos, nome, notas)
        elif opcao == "2":
            nome = ler_nome("Digite o nome do aluno para atualizar as notas: ")
            notas = ler_quatro_notas()
            atualizar_notas(alunos, nome, notas)
        elif opcao == "3":
            nome = ler_nome("Digite o nome do aluno a remover: ")
            remover_aluno(alunos, nome)
        elif opcao == "4":
            exibir_alunos(alunos)
        elif opcao == "5":
            exibir_medias(alunos)
        elif opcao == "0":
            print("Encerrando o cadastro de alunos. Até logo!")
            break
        else:
            print("Opção inválida! Escolha uma opção de 0 a 5.")


if __name__ == "__main__":
    main()