car = int(input("Digite quantos KM o seu carro está: "))

multa = car * 7

if car < 80:
    print("Sua velocidade está ok")
elif car > 80:
    print("Você foi multado em {}R$.".format(multa)) 