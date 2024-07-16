import random

computador = random.randint(0, 5)

var = int(input("Tente advinhar o número, dica está entre 0 e 5: "))

if var == computador:
    print("Parabéns, você acertou")
else:
    print("Tente novamente!")