r1 = float(input("Digite o valor da reta: "))
r2 = float(input("Digite o valor da reta: "))
r3 = float(input("Digite o valor da reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Podemos forma triângulo!")
else:
    print("Seguimento acima não pode forma um triângulo!")
