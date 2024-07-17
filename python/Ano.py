var = int(input("Digite o ano para saber se ele e bissexto: "))

result = var % 400

if result == 0:
    print("O ano é bissexto")
elif result != 0:
    print("O ano não é bissexto!")