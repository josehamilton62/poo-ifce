# Atividade: Classes e Objetos (Aula 02) - Teste da Questao 1

from televisao import Televisao

# Criacao de tres televisores de marcas diferentes guardados em uma lista
tv1 = Televisao("Samsung", 43)
tv2 = Televisao("LG", 50)
tv3 = Televisao("Philco", 32)

televisores = [tv1, tv2, tv3]

# Alteracao direta de estado: ligando alguns e mantendo pelo menos um desligado
televisores[0].ligada = True
televisores[0].canal = 5
televisores[0].volume = 25

televisores[1].ligada = True
televisores[1].canal = 12
televisores[1].volume = 70

# O terceiro televisor (Philco 32") permanece desligado (ligada = False)

# Percurso da lista com laco for e impressao dos dados de cada televisor
for tv in televisores:
    if tv.ligada:
        print(
            f'{tv.marca} {tv.polegadas}" | Ligada | '
            f"Canal {tv.canal} | Volume {tv.volume}"
        )
    else:
        print(f'{tv.marca} {tv.polegadas}" | Desligada')

# Calculo das estatisticas finais
quantidade_ligados = 0
soma_polegadas = 0
maior_tv = None

for tv in televisores:
    if tv.ligada:
        quantidade_ligados += 1

    soma_polegadas += tv.polegadas

    if maior_tv is None or tv.polegadas > maior_tv.polegadas:
        maior_tv = tv

media_polegadas = soma_polegadas / len(televisores)

print(f"\nTelevisores ligados: {quantidade_ligados}")
print(f'Maior televisor: {maior_tv.marca} {maior_tv.polegadas}"')
print(f"Média de polegadas: {media_polegadas:.2f}")