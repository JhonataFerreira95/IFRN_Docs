r1 = float(input("Digite o valor da reta: "))
r2 = float(input("Digite o valor da reta: "))
r3 = float(input("Digite o valor da reta: "))



if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Podemos forma triângulo!")
    if r1 == r2 == r3 :
        print("Podemos forma um triângulo equilátero!")
    elif r1 == r2 != r3:
        print("Podemos forma um triângulo isóceles!")
elif r1 != r2 and r3 != r1 and r2 != r3:
    print("Podemos forma um triângulo escaleno!")


