'''Escreva um algoritmo que leia um conjunto de 10 notas, armazene-as em uma variável
composta chamada NOTA e calcule e imprima a sua média.'''
nota = []
for i in range (11):
  nota.append(float(input(f"Digite a nota {i}: ")))

print(f"Média: {sum(nota)/10}")
