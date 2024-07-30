numero = int(input('Digite um número inteiro: '))
if numero > 0:
    soma = 0
    while numero != 0:
        resto = numero % 10
        numero = (numero - resto) // 10
        soma = soma + resto
    print(f'A soma dos dígitos do número é: {soma}')
else:
    print('Número inválido. Por favor, digite um número inteiro positivo.')

print('Programa encerrado.')

