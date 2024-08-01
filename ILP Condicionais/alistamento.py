from datetime import date

atual = date.today().year

nasc = int(input("Digite o ano do nascimento: "))

idade = atual - nasc

print("Você nasceu em {} tem {} anos em {}".format(nasc, idade, atual))

if idade == 18:
    print("Agora é a hora exata que se alistar\n Você tem a idade {} necessária para se alistar".format(idade))
elif idade <= 18:
    saldo = 18 - idade
    print("Infezlimente você é muito novo para se alistar, ainda tem {} de idade.\n".format(idade))
    ano = atual + saldo
    print("Seu alistamento será em {}".format(ano))
elif idade >= 18:
    saldo = idade - 18
    print("Você tem {}, já passou da hora de ir se alistar, procure o alistamento mais rápido posssível".format(idade))
    ano = atual - saldo
    print("Seu alistamento deveria ser em {}".format(ano))
print("Fim do programa")