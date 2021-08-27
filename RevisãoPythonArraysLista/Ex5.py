'''Ler um vetor de 100 elementos numéricos e verificar se existem elementos iguais a 30. Se
existirem, escrever as posições em que estão armazenados.'''

vet = []
import random as rd

vet = [rd.randint(0,99) for i in range (99)]

#pos = [vet.index(num)+1 for num in vet if num == 30] // Primeira tentativa que as vezes estava dando problemas
pos = vet.index(30)+1 if 30 in vet else None
print(vet)

print(f"Posições: {pos}")
