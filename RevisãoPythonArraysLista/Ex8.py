'''Fazer um algoritmo que:
a) Leia duas variáveis compostas unidimensionais, contendo, cada uma, 25 elementos numéricos;
b) intercale os elementos desses dois conjuntos formando uma nova variável composta
unidimensional de 50 elementos;
c) Escreva o resultado obtido.'''

vet1 = []; vet2 = []; vet3 = []
for i in range(25):
  vet1.append(int(input("Digite um valor para o primeiro vetor: ")))
for i in range(25):
  vet2.append(int(input("Digite um valor para o segundo vetor: ")))
for i in range(25):
  vet3.append(vet1[i])
  vet3.append(vet2[i])
print(vet3)
