# Sabendo que hoje é o dia do desconto de 13% em qualquer camiseta que você comprar, 
# desenvolva um program para que você possa saber o valor do desconto e o valor final de uma camiseta que na semana passada,
# você viu que estava por valor de R$83

# Requisitos:
# Informa o valor do desconto, sabeno que o valor da camiseta é de R$83 e o desconto é de R$13%
# Informar o valor final, que é o valor da camisa de R$83 subtraído do valor do desconto

# Valor do desconto = valor da camisa (R$83) * 13%
# Valor final - Valor da camisa (R$83) - valor do desconto



Valor_desconto = 10.79
Valor_camisa = 83.00
print(round(Valor_camisa - Valor_desconto))

preco = 83.0
desconto = preco * (13/100)
Valor_camisa = preco - desconto
print(Valor_camisa)