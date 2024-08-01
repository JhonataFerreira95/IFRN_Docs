num1 = int(input("Digite um número: "))

num2 = int(input("Digite um número: "))

if num1 > num2:
    print("primeiro valor {} é maior que o segundo valor {}".format(num1,num2))
elif num2 > num1:
    print("segundo valor {} é maior que o primeiro valor {}".format(num2,num1))
elif num1 == num2:
    print("O valor {} é igual ao valor {}".format(num1, num2))
print("Fim do programa")