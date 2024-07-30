# Escreva um programa que leia uma lista de números inteiros fornecida
# pelo usuário e remova todos os elementos duplicados, mantendo a
# ordem original dos elementos. Ao final, apresente os valores fornecidos
# pelo usuário e o resultado do processamento da sua solução;

entrada = input("Digite uma lista de números inteiros separados por espaço: ")
numeros = list(map(int, entrada.split()))

lista_sem_duplicados = []

for numero in numeros:
    if numero not in lista_sem_duplicados:
        lista_sem_duplicados.append(numero)
print("Valores fornecidos:", numeros)
print("Resultado sem duplicados:", lista_sem_duplicados)