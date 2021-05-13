"""Exercício 11"""

#Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado
#a um milhão.

val = str(2 ** 1000000)

quant_dig = len(val)

print("O total de digitos de 2 elevado a 1 Milhão é: {}".format(quant_dig))