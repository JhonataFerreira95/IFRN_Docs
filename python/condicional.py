tempo = int(input("Quantos anos seu carro tem?: "))

if tempo <= 4:
    print("Seu caro é novo!")
elif tempo <= 10 or 14:
    print("Seu carro é mediano")
elif tempo >= 15:
    print("Seu carro é velho!")
print("Fim do programa!")