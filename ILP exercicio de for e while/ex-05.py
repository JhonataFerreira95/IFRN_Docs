
num = int(input('digite um numero para calcularmos o fatorial'))
 
def fatorial(num):
    if num < 0:
        print("Nao existe fatorial de numero negativo")

    elif num == 0:
        return 1

    else:
        fato = 1
        while num > 1:
            fato *= num
            num -= 1
        return fato
    
print("Fatorial do numero", num, "é", fatorial(num))