# Construa um algoritmo que, dado o primeiro elemento e a razão de uma progressão
# aritmética (PA), imprima todos os n primeiros elementos da PA, onde n também é
# informado pelo usuário. Lembre-se que uma PA pode ser crescente ou decrescente.


pa = int(input("Digite a primeira progressão: "))
razao = int(input("Digite segunda razão: "))
imprima = int(input("Digite a quantidade de quantas que ele vai repetir: "))

for i in range(imprima):
 soma = razao * imprima
 result = pa + soma
 var = pa + i * razao
 print(var, end=",")

print(result)