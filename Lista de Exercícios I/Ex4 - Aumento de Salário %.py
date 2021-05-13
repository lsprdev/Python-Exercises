
"""Exercício 4"""

#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
#porcentagem do aumento. Exiba o valor do aumento e do novo salário.

sal = float(input("Valor de seu salário: "))
porc = int(input("Quantos porcento de aumento?: "))

porc = porc/100

novo_sal = (sal*porc) + sal

print("O aumento foi de {}".format(sal*porc))
print("O novo salário é igual {}".format(novo_sal))
