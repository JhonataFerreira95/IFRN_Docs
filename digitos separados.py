num = int(input("Digite um valor: "))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("Analisando o número {}.\nUnidade {}.\nDezena {}.\nCentena {}.\nMilhar {}.\n".format(num, u, d, c, m)) 