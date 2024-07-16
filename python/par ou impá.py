var = int(input("Digite um valor para saber se ele é par ou impar   : "))

result = var % 2

if result == 0:
    print("Ele é par")
elif result != 0:
    print("Ele é impar")