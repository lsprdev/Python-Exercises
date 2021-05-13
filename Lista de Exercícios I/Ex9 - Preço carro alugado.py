
"""Exercício 9"""

#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
#usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.


quant_dia = int(input("O carro foi alugado por quantos dias?: "))
quant_km = float(input("Quantidade de km percorridos com o carro alugado: "))

precototal_dia = quant_dia*60
precototal_km = quant_km*0.15

print("O preço a pagar será de R${}".format(precototal_dia+precototal_km))
