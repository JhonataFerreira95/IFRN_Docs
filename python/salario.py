var = float(input("Digite o valor do seu salário: "))

aumento = var * 0.10
aumento2 = var * 0.15
result = var + aumento
result2 = var + aumento2


if var >= 1250.00:
    print("Parabéns, você recebeu um aumento de 10% no seu salário, que agora será {}".format(result))
elif var <= 1250.00:
    print("Parabéns, você recebeu um aumento de 15% no seu salário, que agora será {}".format(result2))