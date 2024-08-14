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