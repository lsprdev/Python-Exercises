'''Repita o algoritmo acima, porém imprima quantos valores estão acima da média.'''

notas = []; acima = []
for i in range (10):
  notas.append(float(input(f"Digite a nota {i+1}: ")))
media = sum(notas)/10
acima = [nota for nota in notas if nota > media]
print(f"Média: {media}")
print(f"Notas acima da média: {acima}")
print(f"Quantidade de notas acima da média: {len(acima)}")
