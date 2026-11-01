# Atividade: Classes e Objetos (Aula 02) - Teste da Questao 2

from aluno import Aluno

alunos = []

print("=== CADASTRO DE ALUNOS (Deixe o nome vazio para encerrar) ===")
while True:
    nome = input("Nome do aluno: ").strip()
    if nome == "":
        break
    matricula = input("Matrícula: ").strip()
    novo_aluno = Aluno(nome, matricula)
    alunos.append(novo_aluno)

# Atribuicao direta de notas e faltas aos alunos cadastrados,
# garantindo que pelo menos um aluno permaneca sem notas
if len(alunos) >= 1:
    alunos[0].notas.append(8.5)
    alunos[0].notas.append(7.0)
    alunos[0].faltas += 2

if len(alunos) >= 3:
    alunos[1].notas.append(5.5)
    alunos[1].faltas += 6
    # O terceiro aluno (alunos[2]) e demais ficam sem notas (notas = [])
elif len(alunos) == 2:
    # Se apenas 2 alunos forem digitados, o segundo fica sem notas e recebe faltas
    alunos[1].faltas += 6

print()
aluno_mais_faltas = None

for aluno in alunos:
    print(f"{aluno.nome} ({aluno.matricula})")
    print(f"Notas: {aluno.notas}")
    print(f"Faltas: {aluno.faltas}")

    if len(aluno.notas) > 0:
        media = sum(aluno.notas) / len(aluno.notas)
        print(f"Média: {media:.2f}\n")
    else:
        print("Média: sem notas\n")

    if aluno_mais_faltas is None or aluno.faltas > aluno_mais_faltas.faltas:
        aluno_mais_faltas = aluno

if aluno_mais_faltas is not None:
    print(f"Mais faltas: {aluno_mais_faltas.nome} ({aluno_mais_faltas.faltas})")