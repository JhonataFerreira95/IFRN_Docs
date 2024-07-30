def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

valor1 = int(input('Digite o primeiro valor positivo: '))
valor2 = int(input('Digite o segundo valor positivo: '))

soma_primos = 0
print('Números primos no intervalo:')
for num in range(valor1, valor2 + 1):
    if eh_primo(num):
        print(num)
        soma_primos += num

print(f'Somatório dos números primos: {soma_primos}')
print('Programa encerrado.')