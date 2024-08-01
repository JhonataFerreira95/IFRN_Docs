salario = float(input("Digite o seu salário: "))

valor_da_casa = float(input("Digite o valor da casa que deseja comprar: "))

quantidade_anos_pagando = int(input("Digite em quanto tempo pretende pagar a casa: "))

prestacao_mensal = valor_da_casa / (quantidade_anos_pagando * 12)

mensal = salario * 0.30

if prestacao_mensal <= mensal:
    print("Você tem direito de comprar a casa desejada!")
else:
    print("Infelizmente seu salário não cobre a parcela mensal de 30%.")


