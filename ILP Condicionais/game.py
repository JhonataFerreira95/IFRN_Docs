import time
import random

opcoes = ["Papel", "Pedra", "Tesoura"]

jogada = int(input("Suas ações:\n [1] Tesoura\n [2] Papel\n [3] Pedra\n"))


jogada_computador = random.randint(1, 3)

if jogada == 1:
    print("Você jogou TESOURA!")
elif jogada == 2:
    print("Você jogou PAPEL!")
elif jogada == 3:
    print("Você jogou PEDRA!")
else:
    print("Jogada inválida!")
    exit()

print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO!!!")
time.sleep(1)
print("=============|||=============")
print(f"Computador jogou {opcoes[jogada_computador - 1]}!")
print("=============|||=============")
3
if (jogada == 1 and jogada_computador == 3) or (jogada == 2 and jogada_computador == 1) or (jogada == 3 and jogada_computador == 2):
    print("Você ganhou!")
elif jogada == jogada_computador:
    print("Empate!")
else:
    print("Você perdeu!")