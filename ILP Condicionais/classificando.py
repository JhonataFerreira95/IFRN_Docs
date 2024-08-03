from datetime import date

atual = date.today().year

nascimento = int(input("Digite o ano que você nasceu para classificação nos jogos: "))

idade = atual - nascimento

print("O atleta tem {} anos".format(idade))

if nascimento <= 9:
    print("Sua categoria é mirim!")
elif nascimento == 10 or nascimento <= 14:
    print("Sua categoria é infantil!")
elif nascimento == 15 or nascimento <= 19:
    print("Sua categoria é junior!")
elif nascimento == 20 or nascimento <= 26:
    print("Sua categoria é sênior!")
elif nascimento == 27 or nascimento >= 27:
    print("Sua categoria é master!")
print("Fim do programa!") 