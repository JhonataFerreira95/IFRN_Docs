#tuplas:
# 1. Escreva um programa que receba uma tupla de números inteiros e como
# saída uma nova tupla com os elementos pares da tupla original. Por
# exemplo, se a tupla for (1, 2, 3, 4, 5), o programa deve imprimir (2, 4).

tupla_original = (1, 2, 3, 4, 5)
tupla_pares = ()

for numero in tupla_original:
    if numero % 2 == 0:
        tupla_pares += (numero,)

print(tupla_pares)

# 2. Escreva um programa que receba uma tupla de strings e exiba uma nova
# tupla com as strings ordenadas alfabeticamente e sem repetições. Por
# exemplo, se a tupla for ("banana", "maçã", "laranja", "banana", "uva"), o
# programa deve imprimir ("banana", "laranja", "maçã", "uva").

tupla_original = ("banana", "maçã", "laranja", "banana", "uva")
tupla_unica = set(tupla_original)
tupla_ordenada = tuple(sorted(tupla_unica))

print(tupla_ordenada)

# Dicionários:
# 3. Escreva um programa que receba um dicionário que mapeia nomes de
# países para suas populações e exiba o nome do país com a maior
# população. Por exemplo, se o dicionário for {"Brasil": 211.8, "China":
# 1400.5, "Índia": 1366.4}, o programa deve exibir "China".