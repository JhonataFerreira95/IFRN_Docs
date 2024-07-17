var = int(input("Digite o ano para saber se ele e bissexto: "))

result = var % 400
result2 = var % 4
result3 = var % 100

if result == 0 or result2 == 0 or result3 == 0:
    print("O ano é bissexto")
elif result != 0 or result2 != 0 or result3 != 0:
    print("O ano não é bissexto!")