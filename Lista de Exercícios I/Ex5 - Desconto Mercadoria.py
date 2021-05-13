
"""Exercício 5"""

#Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
#preço a pagar.

preco_mer = float(input("Qual o preço da mercadoria sem o desconto?: "))
desc_mer = int(input("De quanto é o desconto(em %)?: "))

desc_mer = desc_mer/100

novo_preco = preco_mer - (desc_mer*preco_mer)

print("O desconto é de R${}".format(desc_mer*preco_mer))
print("Com o desconto, você deverá pagar R${}".format(novo_preco))
