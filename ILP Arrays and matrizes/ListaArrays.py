# Escreva um programa que leia uma lista de números inteiros fornecida
# pelo usuário e remova todos os elementos duplicados, mantendo a
# ordem original dos elementos. Ao final, apresente os valores fornecidos
# pelo usuário e o resultado do processamento da sua solução;

# Lê a entrada do usuário
entrada = input("Digite uma lista de números inteiros, separados por espaço: ")

# Converte a entrada em uma lista de números inteiros
numeros = []
for num in entrada.split():
    try:
        numeros.append(int(num))  # Tenta converter cada entrada para inteiro
    except ValueError:
        print(f"'{num}' não é um número inteiro válido e será ignorado.")

# Inicializa uma lista para números únicos
numeros_unicos = []
vistos = set()

# Encontra números únicos
for numero in numeros:
    if numero not in vistos:
        vistos.add(numero)
        numeros_unicos.append(numero)

# Exibe as listas
print("Lista original:", numeros)
print("Lista sem duplicatas:", numeros_unicos)

# 2. Escreva um programa que leia uma lista de números inteiros fornecida
# pelo usuário e um número alvo. O programa deve encontrar todos os
# pares de números na lista cuja soma seja igual ao número alvo.
# 1. Exemplo: Digite os números separados por espaço: 2 4 3 5 7
