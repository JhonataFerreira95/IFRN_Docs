# 1. Escreva um programa que receba uma tupla de números inteiros e como
# saída uma nova tupla com os elementos pares da tupla original. Por
# exemplo, se a tupla for (1, 2, 3, 4, 5), o programa deve imprimir (2, 4).

tupla_original = (1, 2, 3, 4, 5)
tupla_pares = ()

for numero in tupla_original:
    if numero % 2 == 0:
        tupla_pares += (numero,)

print(tupla_pares)
