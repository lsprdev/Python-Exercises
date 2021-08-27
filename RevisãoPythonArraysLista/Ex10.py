'''Faça um algoritmo que leia um conjunto de 10 elementos reais e os coloque em um vetor.
Construa um segundo vetor formado da seguinte maneira:
• Os elementos de ordem par são os correspondentes do primeiro vetor multiplicados por 3.
• Os elementos de ordem ímpar são os correspondentes do primeiro vetor divididos por 2.
• Imprima os dois vetores.'''

vet1 = []

vet2 = []

for i in range(4):
  vet1.append(float(input("Digite um número: ")))
for i in vet1:
  if i % 2 == 0:
    vet2.append(i*3)
  else:
    vet2.append(i/2)

print(f"Primeiro Vetor: {vet1}")
print(f"Segundo Vetor: {vet2}")