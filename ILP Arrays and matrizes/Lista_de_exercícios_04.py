# 1. Escreva um programa que leia 10 valores inteiros e armazene em uma lista. O pro-
# grama deve imprimir no terminal quantos valores pares foram digitados pelo usuário.

# Dica: use o operador “%” para verificar se o número é par (ZERO é neutro, ZERO NÃO
# É PAR).

valores = []

for i in range(10):
    valor = int(input("Digite um valor inteiro: "))
    valores.append(valor) 
contador_pares = 0
for i in range(10):
    if valores[i] % 2 == 0 and valores[i] != 0: 
        contador_pares += 1
print(f"Qtd valores par: {contador_pares}")

# 2. Escreva um programa que recebe como entrada valores inteiros para criar duas listas

# de mesmo tamanho. O tamanho das listas deverá ser definido pelo usuário. O pro-
# grama deverá somar os valores pares e ímpar de cada uma das listas. Em seguida,

# comparar as somas e informar qual dos somatórios é maior ou se há um empate.

tamanho = int(input("Digite o tamanho das listas: "))


lista1 = [0] * tamanho
lista2 = [0] * tamanho

print("Digite os valores da primeira lista:")
for i in range(tamanho):
    lista1[i] = int(input())

print("Digite os valores da segunda lista:")
for i in range(tamanho):
    lista2[i] = int(input())

soma_par1 = 0
soma_impar1 = 0
soma_par2 = 0
soma_impar2 = 0

for i in range(tamanho):
    if lista1[i] % 2 == 0 and lista1[i] != 0:
        soma_par1 += lista1[i]
    elif lista1[i] % 2 != 0:
        soma_impar1 += lista1[i]

for i in range(tamanho):
    if lista2[i] % 2 == 0 and lista2[i] != 0:
        soma_par2 += lista2[i]
    elif lista2[i] % 2 != 0:
        soma_impar2 += lista2[i]

print(f"Soma listaPar1: {soma_par1}")
print(f"Soma listaPar2: {soma_par2}")

if soma_par1 < soma_par2:
    print("listaPar1 < listaPar2")
elif soma_par1 > soma_par2:
    print("listaPar1 > listaPar2")
else:
    print("listaPar1 = listaPar2")

print(f"Soma listaImpar1: {soma_impar1}")
print(f"Soma listaImpar2: {soma_impar2}")

if soma_impar1 < soma_impar2:
    print("listaImpar1 < listaImpar2")
elif soma_impar1 > soma_impar2:
    print("listaImpar1 > listaImpar2")
else:
    print("listaImpar1 = listaImpar2")

# 3. leia 10 valores inteiros e armazene em uma lista. O programa deve imprimir no terminal
# quantos valores pares foram digitados pelo usuário. Dica: use o operador “%” para
# verificar se o número é par (ZERO é neutro, ZERO NÃO É PAR).

valores = []

print("Digite 10 valores inteiros:")
for i in range(10):
    valor = int(input())
    valores.append(valor)

contador_pares = 0

for valor in valores:
    if valor % 2 == 0 and valor != 0:
        contador_pares += 1

print(f"Quantidade de valores par: {contador_pares}")

# Questão 04
# tamanho_da_lista = int(input('Digite o valor das listas: '))
# primeira_lista = []
# primeiro_valor_boolean = False
# primeiro_valor_numerico = 0
# elemento_desejado_cert = ['boolean', 'string', 'numero']

tamanho_da_lista = int(input('Digite o valor das listas: '))
primeira_lista = []
elemento_desejado_cert = ['boolean', 'string', 'numero']

for i in range(tamanho_da_lista):
    if i == 0:
        primeiro_valor = input('Digite o primeiro valor string: ')
        primeira_lista.append(primeiro_valor)
    elif i == 1:
        primeiro_valor_boolean = input('Digite o primeiro valor boolean (True/False): ')
        primeira_lista.append(primeiro_valor_boolean.lower() == 'true')
    elif i == 2:
        primeiro_valor_numerico = int(input('Digite o primeiro valor numerico: '))
        primeira_lista.append(primeiro_valor_numerico)
    else:
        elemento_desejado = input('Digite o tipo de elemento desejado (boolean/string/numero): ')
        while elemento_desejado not in elemento_desejado_cert:
            print('Elemento inválido.')
            elemento_desejado = input('Digite outro tipo de elemento desejado: ')
        
        if elemento_desejado == 'boolean':
            outro_valor_boolean = input('Digite outro valor boolean (True/False): ')
            primeira_lista.append(outro_valor_boolean.lower() == 'true')
        elif elemento_desejado == 'string':
            outro_valor_string = input('Digite outro valor string: ')
            primeira_lista.append(outro_valor_string)
        else:
            outro_valor_numerico = int(input('Digite outro valor numerico: '))
            primeira_lista.append(outro_valor_numerico)

print("Lista final:", primeira_lista)

# 5. Escreva um programa que receba como entrada uma sequência de valores inteiros.
# Para tanto, o programa deverá inicialmente solicitar ao usuário quantos valores serão
# fornecidos para análise e só depois solicitar os valores a serem analisados. A análise
# consistirá em identificar e apresentar a partir da sequência de valores fornecidos, o
# menor valor, o maior valor e a média aritmética dos valores.

quantidade = int(input("Digite a quantidade de valores: "))

valores = []
soma = 0

print("Digite os valores:")
for i in range(quantidade):
    valor = int(input())
    valores.append(valor)
    soma += valor 

menor_valor = valores[0]
maior_valor = valores[0]

for i in range(1, quantidade):
    if valores[i] < menor_valor:
        menor_valor = valores[i]
    if valores[i] > maior_valor:
        maior_valor = valores[i]


media = soma / quantidade

print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Média aritmética: {media:.0f}")

# 6. Crie um programa que solicite ao usuário uma lista de números inteiros e uma string
# de mesmo comprimento. O programa deve substituir os números nos índices ímpares
# da lista por caracteres correspondentes da string nos mesmos índices. Exiba a se-
# quência resultante, separada por um espaço em branco.

numeros = input("Digite a lista de números inteiros (separados por espaço): ").split()
string = input("Digite uma string de mesmo comprimento: ")

resultado = []

if len(numeros) != len(string):
    print("A lista de números e a string devem ter o mesmo comprimento.")
else:
    for i in range(len(numeros)):
        if i % 2 == 1:
            resultado.append(string[i])
        else:
            resultado.append(numeros[i])

    print(" ".join(resultado))

# 7. Para tanto, o programa deverá inicialmente solicitar ao usuário quantos valores serão
# fornecidos para análise e só depois solicitar os valores a serem analisados. A análise
# consistirá em identificar e apresentar a partir da sequência de valores fornecidos, o
# menor valor, o maior valor e a média aritmética dos valores.

quantidade = int(input("Digite a quantidade de valores: "))

valores = []
soma = 0

print("Digite os valores:")
for i in range(quantidade):
    valor = int(input())
    valores.append(valor) 
    soma += valor 

menor_valor = valores[0]
maior_valor = valores[0]

for i in range(1, quantidade):
    if valores[i] < menor_valor:
        menor_valor = valores[i]
    if valores[i] > maior_valor:
        maior_valor = valores[i]

media = soma / quantidade

print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Média aritmética: {media:.2f}") 

# 8. Escreva um programa que receba como entrada uma string constituída por uma se-
# quência de números inteiros separados por espaço. O programa deverá transformar

# essa string em uma lista de números inteiros e apresentar o resultado da soma dos
# valores das posições ímpares dessa lista. 

entrada = input("Digite uma sequência de números inteiros (separados por espaço): ")

numeros = list(map(int, entrada.split()))

soma = 0
valores_impares = []

for i in range(len(numeros)):
    if i % 2 == 1:
        soma += numeros[i]
        valores_impares.append(str(numeros[i])) 

resultado = "+".join(valores_impares)
print(f"{resultado} = {soma}")

# 9. Escreva um programa que receba como entrada uma string várias palavras separadas
# por espaço. O programa deverá verificar e apresentar a quantidade de ocorrência de

# cada palavra no texto repassado como entrada para o programa. Os sinais de pontu-
# ação não devem ser contabilizados, como por exemplo “.” Ou “,”.

import string

entrada = input("Digite uma sequência de palavras: ")

entrada = entrada.translate(str.maketrans("", "", string.punctuation)).lower()

palavras = entrada.split()

contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1
resultado = "; ".join([f"{palavra}={contagem[palavra]}" for palavra in contagem])
if resultado:
    print(resultado + ";")
else:
    print("Nenhuma palavra foi inserida.")

# 10. Escreva um programa que leia 9 valores inteiros e armazene em uma matriz 3x3. O

# programa deve informar quantos valores ímpares foram digitados pelo usuário e impri-
# mir a matriz no formato 3x3. Dica: use o operador “%” para verificar se o número é
# ímpar.

matriz = []

quantidade_impares = 0

print("Digite 9 valores inteiros:")
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i+1}][{j+1}]: "))
        linha.append(valor)
        if valor % 2 != 0:
            quantidade_impares += 1
    matriz.append(linha)
print("Matriz:")
for linha in matriz:
    print(" ".join(map(str, linha)))

print(f"Quantidade de números ímpares: {quantidade_impares}")

# 11. Escreva um programa que solicite ao usuário o valor das duas dimensões de uma
# matriz. Em seguida, solicite ao usuário e armazene nessa matriz uma quantidade de

# valores inteiros correspondente ao tamanho necessário para preencher todas as posi-
# ções da matriz. O programa deverá exibir a matriz de dimensões “m por n” informar o

# resultado da soma de cada LINHA da matriz.

linhas = int(input("Digite o número de Linhas: "))
colunas = int(input("Digite o número de Colunas: "))

matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite os valores da posição: ({i},{j}): "))
        linha += [valor]
    matriz += [linha]

for i in range(linhas):
    soma_linha = 0
    for j in range(colunas):
        soma_linha += matriz[i][j] 
    print(f"{matriz[i]} = {soma_linha}")

# 12. Escreva um programa que solicite ao usuário o valor das duas dimensões de uma
# matriz. Em seguida, solicite ao usuário e armazene nessa matriz uma quantidade de
# valores inteiros correspondente ao tamanho necessário para preencher todas as posi-
# ções da matriz. O programa deverá exibir a matriz de dimensões “m por n” informar o
# resultado da soma de cada COLUNA da matriz.

m = int(input("Digite o número de linhas (m): "))
n = int(input("Digite o número de colunas (n): "))

matriz = [[0] * n for _ in range(m)]

print(f"Digite {m * n} valores inteiros:")
for i in range(m):
    for j in range(n):
        matriz[i][j] = int(input(f"Digite o valor para a posição [{i + 1}][{j + 1}]: "))
for i in range(m):
    for j in range(n):
        if j == n - 1:
            print(matriz[i][j], end="")
        else:
            print(matriz[i][j], end=" ")
    print()
for j in range(n):
    soma_coluna = 0
    for i in range(m):
        soma_coluna += matriz[i][j]
    print(f"Coluna{j + 1}: {soma_coluna}")

# 13. Escreva um programa que armazene valores inteiros em duas matrizes A e B de tama-
# nho 3x3. Em seguida gere uma terceira matriz C 3x3 formada pelos maiores valores

# de cada posição comparando as duas primeiras matrizes A e B.

linhas = 3
colunas = 3
matriz_a = []
matriz_b = []
matriz_resultante = [[0 for _ in range(linhas)] for _ in range(colunas)]

print("Primeira matriz")
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor das poisições ({i},{j}): "))
        linha += [valor]
    matriz_a += [linha]

print("Segunda matriz")
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor das poisições ({i},{j}): "))
        linha += [valor]
    matriz_b += [linha]

for i in range(colunas):
    for j in range(linhas):
        if matriz_a[i][j] > matriz_b[i][j]:
            matriz_resultante[i][j] = matriz_a[i][j]
        if matriz_a[i][j] < matriz_b[i][j]:
            matriz_resultante[i][j] = matriz_b[i][j]
        else:
            matriz_resultante[i][j] = matriz_a[i][j]
print("Matriz a")
for _ in matriz_a:
    print(_)
print("Matriz b")
for _ in matriz_b:
    print(_)

print("matriz resultante:")

for _ in matriz_resultante:
    print(_)

# 14. Escreva um programa que armazene valores inteiros em uma matrize de tamanho
# 4x4. Em seguida exiba a soma dos elementos que estão em índices de linha ímpar e
# coluna par.

matriz = [[0] * 4 for _ in range(4)]

print("Digite 16 valores inteiros para a matriz 4x4:")
for i in range(4):
    for j in range(4):
        while True:
            entrada = input(f"Digite o valor para a posição [{i + 1}][{j + 1}]: ")
            if entrada.strip() == "":
                print("Por favor, insira um valor inteiro.")
            else:
                try:
                    matriz[i][j] = int(entrada)
                    break
                except ValueError:
                    print("Por favor, insira um valor inteiro válido.")
soma = 0
elementos = []

for i in range(4):
    for j in range(4):
        if i % 2 != 0 and j % 2 == 0:
            soma += matriz[i][j]
            elementos.append(matriz[i][j])
print("Resultado:")
print(" + ".join(map(str, elementos)), "=", soma)


# 15. Escreva um programa que, dada uma matriz de números inteiros aleatórios variando
# entre 100 e 999 de dimensões ‘m’ por ‘n’, ambos podendo variar de 2 a 10, realize os

# seguintes passos: solicite ao usuário as dimensões da matriz; apresente a matriz ge-
# rada de forma aleatória; informe o valor e posição do maior e menor valor na matriz.

import random

matriz = []
linhas = random.randint(2,10)
colunas = random.randint(2,10)

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = random.randint(100,999)
        linha.append(valor)
    matriz.append(linha)

menor_valor = matriz[0][0]
maior_valor = matriz[0][0]
menor_posicao = (0,0)
maior_posicao = (0,0)

for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] < menor_valor:
            menor_valor = matriz[i][j]
            menor_posicao = (i,j)
        if matriz[i][j] > maior_valor:
            maior_valor = matriz [i][j]
            maior_posicao = (i,j)
            
print("Matriz")
for _ in matriz:
    print(_)

print(f"Menor valor: {menor_valor} ({menor_posicao})")
print(f"Maior valor: {maior_valor} ({maior_posicao})")

# 16. Escreva um programa que realiza o produto matricial entre duas matrizes de dimen-
# sões 3x3. Os valores das duas matrizes devem ser gerados de forma aleatória com
# números inteiros aleatórios variando entre 1 e 9. Ao final, apresente as duas matrizes
# geradas de forma aleatória, bem como a matriz resultante do produto.

import random

matriz_A = [[0] * 3 for _ in range(3)]
matriz_B = [[0] * 3 for _ in range(3)]
matriz_resultante = [[0] * 3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        matriz_A[i][j] = random.randint(1, 9)
for i in range(3):
    for j in range(3):
        matriz_B[i][j] = random.randint(1, 9)
for i in range(3):
    for j in range(3):
        for k in range(3):
            matriz_resultante[i][j] += matriz_A[i][k] * matriz_B[k][j]
print("Matriz A:")
for i in range(3):
    for j in range(3):
        if j == 2:
            print(matriz_A[i][j], end="")
        else:
            print(matriz_A[i][j], end=" ")
    print() 
print("Matriz B:")
for i in range(3):
    for j in range(3):
        if j == 2:
            print(matriz_B[i][j], end="")
        else:
            print(matriz_B[i][j], end=" ")
    print()
print("Matriz Resultante:")
for i in range(3):
    for j in range(3):
        if j == 2:
            print(matriz_resultante[i][j], end="")
        else:
            print(matriz_resultante[i][j], end=" ")
    print()

# 17. Escreva um programa que realiza o produto matricial entre duas matrizes de dimen-
# sões ‘j’ por ‘k’ e ‘m’ por ‘n’ fornecidas pelo usuário. Os valores das duas matrizes devem

# ser gerados de forma aleatória com números inteiros aleatórios variando entre dois
# valores, também fornecidos pelo usuário. Ao final, apresente as duas matrizes geradas
# de forma aleatória, bem como a matriz resultante do produto. Caso não seja possível
# realizar o produto matricial, informe a impossibilidade ao usuário e as duas matrizes
# geradas.

import random

linhas_a = int(input("Digite o valor de linhas da primeira matriz: "))
colunas_a = int(input("Digite o valor de colunas da primeira matriz: "))
linhas_b = int(input("Digite o valor de linhas da segunda matriz: "))
colunas_b = int(input("Digite o valor de colunas da seunda matriz: "))

if colunas_a != linhas_b:
    print("Impossibilidade de realizar o produto matricial")
else:

    matriz_a =[]
    matriz_b = []
    matriz_resultante = [[0 for _ in range(colunas_b)] for _ in range(linhas_a)]

    numero_aleatorio_inicial = int(input("Digite o valor do número alatorio inical: "))
    numero_aleatorio_final = int(input("Digite o valor do número alatorio inical: "))

    for i in range (linhas_a):
        linha_a = []
        for j in range(colunas_a):
            valor_a = random.randint(numero_aleatorio_inicial,numero_aleatorio_final)
            linha_a.append(valor_a)
        matriz_a.append(linha_a)

    for i in range (linhas_b):
        linha_b = []
        for j in range(colunas_b):
            valor_b = random.randint(numero_aleatorio_inicial,numero_aleatorio_final)
            linha_b.append(valor_b)
        matriz_b.append(linha_b)

    linhas_a = len(matriz_a)
    colunas_a = len(matriz_a[0])
    linha_b = len(matriz_b)
    colunas_b = len(matriz_b[0])

    for i in range(linhas_a):
        for j in range(colunas_b):
            for k in range(colunas_a):
                matriz_resultante[i][j] += matriz_a[i][k] * matriz_b[k][j]

    for linha in matriz_resultante:
        print(linha)

# 18. Escreva um programa que leia uma matriz de dimensões 3x6 com valores reais. Em
# seguida, o programa deverá imprimir a soma de todos os elementos das colunas ím-
# pares; imprima a média aritmética dos elementos da segunda e quarta colunas; subs-
# titua os valores da sexta coluna pela soma dos valores das colunas 4 e 5; Exiba a
# matriz modificada e a matriz original.

matriz = [[0.0] * 6 for _ in range(3)]

print("Digite 18 valores reais para a matriz 3x6:")
for i in range(3):
    for j in range(6):
        matriz[i][j] = float(input(f"Digite o valor para a posição [{i + 1}][{j + 1}]: "))
soma_colunas_impares = 0.0
soma_coluna_2 = 0.0
soma_coluna_4 = 0.0
soma_coluna_5 = 0.0
for i in range(3):
    for j in range(6):
        if j % 2 != 0:
            soma_colunas_impares += matriz[i][j]
        if j == 1:
            soma_coluna_2 += matriz[i][j]
        if j == 3:
            soma_coluna_4 += matriz[i][j]
        if j == 4:
            soma_coluna_5 += matriz[i][j]
media_colunas_2_4 = (soma_coluna_2 + soma_coluna_4) / 6.0 
for i in range(3):
    matriz[i][5] = matriz[i][3] + matriz[i][4]
print("Soma das colunas ímpares:", soma_colunas_impares)
print("Média aritmética das colunas 2 e 4:", media_colunas_2_4)
print("Matriz Modificada:")
for i in range(3):
    for j in range(6):
        if j == 5:
            print(matriz[i][j], end="")
        else:
            print(matriz[i][j], end=" ")
    print()
print("Matriz Original:")
for i in range(3):
    for j in range(6):
        if j == 5:
            print(matriz[i][j], end="")
        else:
            print(matriz[i][j], end=" ")
    print()