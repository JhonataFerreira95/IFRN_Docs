km = float(input("Digite o valor percorrido: "))

result = km * 0.50
result2 = km * 0.45

if km <= 200:
    print("Sua viagem foi abaixo de 200km, sua taxa vai ser de {}.".format(result))
elif km >= 200:
    print("Sua viagem foi acima de 200km, recebeu um desconto de {}.".format(result2))