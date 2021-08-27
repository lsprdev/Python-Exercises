'''Faça um algoritmo que leia um vetor que contém as notas de 30 alunos. Imprima o maior
valor, o menor valor, a média da turma e a quantidade de notas abaixo da média.'''

notas = []; abaixo = []
for i in range (30):
  notas.append(float(input(f"Digite a nota {i+1}: ")))

media = sum(notas)/30
abaixo = [nota for nota in notas if nota < media]

print(f"Todas as Notas: {notas}")
print(f"Média da turma: {media}")
print(f"Maior nota: {max(notas)}")
print(f"Menor nota: {min(notas)}")
print(f"Quantidade de notas abaixo da média: {len(abaixo)}")
