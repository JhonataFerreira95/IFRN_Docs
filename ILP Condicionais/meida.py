num1 = float(input("Digite a sua primeira nota: "))
num2 = float(input("Digite a sua segunda nota: "))

soma = num1 + num2 
media = soma / 2

if media <= 5.0:
    print("Sua média {} foi abaixo de 5, então está reprovado!".format(media))
elif media <= 5.0 or media <= 6.9:
    print("Sua média {} está baixo de 7, então você está em recuperação!".format(media))
elif media >= 7:
    print("Sua média {} está acima de 7, você está aprovado!".format(media))