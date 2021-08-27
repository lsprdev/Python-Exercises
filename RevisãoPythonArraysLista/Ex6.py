'''Fazer um algoritmo que calcule e escreva o somatório dos valores armazenados numa variável
composta unidimensional (vetor) A, de 100 elementos numéricos a serem lidos do dispositivo
de entrada.'''
num = []
for i in range(100):
  num.append(int(input("Digite um número: ")))
print(f"Soma: {sum(num)}")
