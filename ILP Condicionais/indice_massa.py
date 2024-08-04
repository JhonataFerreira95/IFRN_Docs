peso = float(input("Digite o seu peso (Kg): "))
altura = float(input("Digite a sua altura (M): "))

calculo = peso / (altura * altura)

if calculo <= 18.5:
    print("Seu IMC é {:.2f}, abaixo do peso.".format(calculo))
elif 18.5 < calculo <= 24.9:
    print("Seu IMC é {:.2f}, peso ideal.".format(calculo))
elif 25 <= calculo <= 29.9:
    print("Seu IMC é {:.2f}, sobrepeso.".format(calculo))
elif 30 <= calculo <= 39.9:
    print("Seu IMC é {:.2f}, obesidade.".format(calculo))
else:
    print("Seu IMC é {:.2f}, obesidade mórbida.".format(calculo))
