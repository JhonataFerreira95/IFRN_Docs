fib = int(input("Digite um número inteiro positivo: "))

seven, six = 0, 1
count = 0


if fib <= 0:
    print("Por favor, digite um número inteiro positivo.")
elif fib == 1:
    print("Sequência de Fibonacci até", fib, ":")
    print(seven)
else:
    print("Sequência de Fibonacci:")
    while count < fib:
        print(seven, end=" ")
        c = seven + six
        seven = six
        six = c
        count += 1
print("\nTérmino do programa.")