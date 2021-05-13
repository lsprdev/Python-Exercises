
"""Exercício 6"""

#Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
#esperada para a viagem.

dis = float(input("Qual a distância que você percorrerá em km?: "))
vel_med = float(input("Qual será sua velocidade média em km/h?: "))

temp = dis/vel_med

print("Seu tempo de viagem será de {0:1.5f} hora(s)".format(temp))
