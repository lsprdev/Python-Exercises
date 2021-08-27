'''Escreva um algoritmo que leia um vetor de 200 valores numéricos reais e os imprima na
ordem contrária em que foi lida.'''
num = []
for i in range(200):
  num.append(float(input("Digite um número: ")))
num.reverse()
print(f"{num}")
