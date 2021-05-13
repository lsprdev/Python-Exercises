
"""Exercício 3"""

#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule
#o total em segundos.
dia = int(input("Quantidade de dias: "))
hora = int(input("Quantidade de horas: "))
min = int(input("Quantidade de minutos: "))
seg = int(input("Quantidade de segundos: "))

total_seg = (((dia*24)*60)*60) + ((hora*60)*60) + (min*60) + seg

print("{} dia(s), {} hora(s), {} minuto(s) e {} segundo(s) correspondem a {} segundos no total".format(dia, hora, min, seg, total_seg))
