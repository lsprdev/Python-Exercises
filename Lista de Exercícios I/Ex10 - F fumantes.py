"""Exercício 10"""

#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
#quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
#perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
#total de dias.

quant_cig = int(input("Quantos cigarros você fuma por dia?: "))
quant_anos = float(input("Por quantos anos você já fumou?: "))

total_dias = quant_anos*365

quanttotal_cig = quant_cig*total_dias

print("Total de dias de vida perdidos: {0:1.2f} dias".format((quanttotal_cig*10)/1440))
