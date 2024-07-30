num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

if(num1< 0 or num2 < 0):
    print("Por favor, digite valores positivos.")
else:
    for num in range(num1, num2 + 1):
        print(num)
print("Fim do programa.")