# 1. Escreva um programa para ler e armazenar valores em uma matriz de
# tamanho m por n. A quantidade de linhas e colunas deve ser definida
# pelo usuário e a matriz deve ser inicializada com valor 0 em todas as
# posições. O programa deverá solicitar ao usuário um valor inteiro
# positivo para armazenar em cada uma das posições da matriz. Caso o
# usuário digite um valor negativo, esse valor deverá ser dobrado e
# tornado positivo e em seguida inserido na respectiva posição. Ao final,
# exiba os valores da matriz resultante. Considere que os valores de m=2
# e n=3 e as entradas conforme exemplo:
# Entrada: 1 -2 5 Saída: 1 4 5
# 3 4 -4 3 4 8

m = 2  # número de linhas
n = 3  # número de colunas

matriz = [[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        while True:
            entrada = input("Digite um valor para a posição ({}, {}): ".format(i, j))
            if entrada:
                try:
                    valor = int(entrada)
                    if valor < 0:
                        valor = abs(valor * 2)
                    matriz[i][j] = valor
                    break 
                except ValueError:
                    print("Por favor, insira um número inteiro válido.")
print("Matriz resultante:")
for linha in matriz:
    print(" ".join(str(valor) for valor in linha))

# 2. Escreva um programa para ler e armazenar valores em duas matrizes (matriz1
# e matriz2) de tamanho m por n. A quantidade de linhas e colunas deve ser
# definida pelo usuário, bem como os valores de cada matriz. O Programa
# deverá comparar os valores de cada posição e criar uma nova matriz inserindo
# o valor 1, caso o valor matriz1 seja maior que o matriz2, inserir o valor 2 caso
# o valor de matriz2 seja maior que o de matriz1, ou zero caso contrário. Ao final
# exiba os valores das 3 matrizes.
# matriz1 = [ matriz2 = [ matriz_resultado = [
# [1, 5, 7], [3, 2, 9], [2, 1, 2],
# [8, 3, 9], [8, 3, 1], [0, 0, 1],
# [4, 6, 2] [1, 8, 7], [1, 2, 2],
# ] ] ]

m = int(input("Digite o número de linhas: "))
n = int(input("Digite o número de colunas: "))

matriz1 = [[0 for _ in range(n)] for _ in range(m)]
matriz2 = [[0 for _ in range(n)] for _ in range(m)]
matriz_resultado = [[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        while True:
            entrada = input("Digite um valor para matriz1 na posição ({}, {}): ".format(i, j))
            if entrada:
                try:
                    matriz1[i][j] = int(entrada)
                    break 
                except ValueError:
                    print("Por favor, insira um número inteiro válido.")
for i in range(m):
    for j in range(n):
        while True:
            entrada = input("Digite um valor para matriz2 na posição ({}, {}): ".format(i, j))
            if entrada:
                try:
                    matriz2[i][j] = int(entrada)
                    break
                except ValueError:
                    print("Por favor, insira um número inteiro válido.")
for i in range(m):
    for j in range(n):
        if matriz1[i][j] > matriz2[i][j]:
            matriz_resultado[i][j] = 1
        elif matriz1[i][j] < matriz2[i][j]:
            matriz_resultado[i][j] = 2
        else:
            matriz_resultado[i][j] = 0
print("Matriz 1:")
for linha in matriz1:
    print(" ".join(str(valor) for valor in linha))

print("Matriz 2:")
for linha in matriz2:
    print(" ".join(str(valor) for valor in linha))

print("Matriz Resultado:")
for linha in matriz_resultado:
    print(" ".join(str(valor) for valor in linha))