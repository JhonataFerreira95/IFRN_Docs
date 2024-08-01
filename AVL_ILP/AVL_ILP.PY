# 1 – (20 pts) Você foi contratado para desenvolver um sistema que calcula descontos para um supermercado.
# As regras de desconto são as seguintes:
# ● Se o cliente tiver um cartão fidelidade e a compra for acima de R$ 500, aplicar um desconto de 10%.
# ● Se o cliente não tiver um cartão fidelidade, mas a compra for acima de R$ 1.000, aplicar um desconto
# de 5%.
# Escreva um programa que leia o valor da compra e se o cliente possui ou não um cartão fidelidade, e então
# calcule e mostre o valor final da compra após aplicar os descontos apropriados. Utilize alguma das estruturas
# condicionais estudadas para solucionar o problema.

"""
    AHFM:
    - A variavel cliente deveria ter um nome mais sugestivo, como por exemplo: valor_compra ou valor_compra_cliente
"""
cliente = float(input("Digite o valor da compra: "))
cartao = input("Você possui nosso cartão de fidelidade: ").lower()

desconto1 = cliente * 0.10
desconto2 = cliente * 0.05

"""
    AHFM:
    - Na linha 15 vocês deveriam ser mais explícito quanto ao valor que o usuário deveria digitar (sim ou não)
    - O que acontece se o usuário digitar algo diferente de sim ou não?
    - A linha de código em questão está tentando verificar duas condições antes de executar um bloco de código
      que presumivelmente segue essa linha. No entanto, há um erro lógico significativo na maneira como a 
      condição é formulada. Vamos decompô-la:
            if cliente >= 1000 and "sim" or "não" in cartao:
        1. cliente >= 1000: Esta é a primeira condição que verifica se a variável cliente tem um valor maior ou 
                            igual a 1000. Se cliente for, por exemplo, 1001, essa condição será verdadeira.
        2. and: Este é um operador lógico que exige que as condições de ambos os lados sejam verdadeiras para que 
                toda a expressão seja considerada verdadeira.
        3. "sim" or "não" in cartao: Aqui está o erro lógico. A intenção parece ser verificar se a variável cartao 
                                     contém a string "sim" ou "não". No entanto, a maneira como está escrita, a 
                                     expressão é dividida em duas partes:
            3.1. "sim": Isso é sempre avaliado como verdadeiro porque qualquer string não vazia em Python é 
                        considerada verdadeira em um contexto booleano.
            3.2. "não" in cartao: Isso verifica se a substring "não" está presente na variável cartao.

        - Devido ao uso do operador or, se "sim" for verdadeiro (o que sempre será), a expressão inteira após o and 
          será considerada verdadeira, independentemente do valor de cartao. Isso significa que a condição como um 
          todo será verdadeira se cliente >= 1000, ignorando efetivamente a intenção de verificar o conteúdo de cartao. 
        - A maneira correta de formular essa condição, se o objetivo é verificar se cartao contém "sim" ou "não" e se 
          cliente é maior ou igual a 1000, seria algo como:
            if cliente >= 1000 and ("sim" in cartao or "não" in cartao):
        - Essa correção garante que a condição só será verdadeira se cliente for maior ou igual a 1000 e cartao contiver 
          "sim" ou "não". 
        - No entanto, o seguimento para continuidade do programa não deveria ser a linha XX, pois essa condição serviu,
          ao fim e ao cabo, apenas para verificar se foi digitado sim ou não, pois se o cliente tiver comprado mais de 
          R$ 500,00, mas não tiver o cartão fidelidade não poderá receber desconto algum.
        - Esse erro lógico compromete toda a solução da questão. Caso o valor de entrada seja 1000 e "sim" o desconto será 
          de 5% ao invés dos 10% recomendado.
"""
if cliente >= 1000 and ("sim" or "não" in cartao):
    total_pagar = cliente - desconto2
    print("Você possui nosso cartão de fidelidade, sua compra recebeu um desconto de 5%, em cima do valor comprado, desconto foi de: {}. Total a ser pago: R$ {}".format(desconto2, total_pagar))
elif "sim" in cartao and cliente >= 500:
    total_pagar = cliente - desconto1
    print("Você possui nosso cartão de fidelidade, você ganhou um desconto de 10%, em cima do valor comprado, desconto foi de: {}. Total a ser pago: R$ {}".format(desconto1, total_pagar))
elif cliente >= 500:
    # AHFM: a variavel total_pagar não está sendo utilizada, portanto é desnecessária nesse contexto.
    total_pagar = cliente 
    print("Você não possui o nosso cartão de fidelidade, Total a ser pago: R$ {}".format(cliente))
print("Fim do programa!")

# AHFM RESULTADO DA QUESTÃO 01: 10pts



# 2 – (20 pts) Crie um programa para verificar a presença, ou ausência, de 100 valores fornecidos pelo usuário
# em um dado intervalo. Neste sentido o seu programa deverá realizar as seguintes ações:
# 1) Solicitar ao usuário dois valores inteiros e diferentes que determinarão o intervalo;
# 2) Solicitar ao usuário que sejam fornecidos 100 valores e verificar se esses valores estão contidos no
# intervalo;
# 3) Contabilizar os valores digitados pelo usuário que estejam contidos dentro do intervalo;
# 4) Exibir o maior valor digitado pelo usuário (pertencente ao intervalo) e o total de valores digitados
# pelo usuário que estão contidos dentro do intervalo.

print("Digite dois valores inteiros diferentes para determinar o intervalo:")
valor_inicial = int(input("Valor inicial: "))
valor_final = int(input("Valor final: "))
if valor_inicial > valor_final:
    valor_inicial, valor_final = valor_final, valor_inicial
contador = 0
maior_valor = float('-inf')

print("\nDigite 100 valores para verificar se estão dentro do intervalo.")

# AHFM: O valor do argumento de range não deveria ser 100?
for i in range(10):
    valor = int(input( "digite um valor "))
    
    if valor_inicial <= valor <= valor_final:
        contador += 1
        if valor > maior_valor:
            maior_valor = valor

if contador > 0:
    print(f"Maior valor dentro do intervalo é: {maior_valor}")
    print(f"Valores dentro do intervalo: {contador}")

print("fim")

# AHFM RESULTADO DA QUESTÃO 02: 20pts



# 3 – (20 pts) O Jogo do par ou ímpar. Crie um programa que simula um campeonato de par ou ímpar. O
# programa, ao ser iniciado, deve solicitar a quantidade de jogadores que irão disputar as partidas de par
# ou ímpar e distribuir esses jogadores em grupos, sempre com três jogadores, preferencialmente, e no
# mínimo 2. Divisão dos grupos: o campeonato deve ter no mínimo 2 e no máximo 9 jogadores. Caso o
# campeonato tenha de 2 a 3 jogadores, então deverá existir apenas um grupo e o campeão do grupo será
# o vencedor do campeonato. Caso o jogo tenha 4 jogadores, deverão ser criados dois grupos com dois
# jogadores; caso tenha 5 jogadores, deverá ser criado um grupo com 3 e outro com 2; caso tenha 6
# jogadores, deverão ser criados dois grupos com 3 jogadores e assim por diante. O campeonato deve ter
# no máximo 3 grupos e envolve duas fases: uma classificatória e a decisão final com aqueles que se
# classificaram par a fase final. Na fase classificatória, cada jogador de um grupo jogará uma vez contra os
# rivais desse mesmo grupo. Cada partida será disputada em um formato “melhor de 3”, ou seja, quem
# vencer duas rodas primeiro vence a partida. Se houver empate, esses dois jogadores deverão disputar
# uma partida entre si para decidir quem será o campeão do grupo. O caminho para a fase final se dará da
# seguinte forma: se o campeonato tiver apenas um grupo, o campeão do grupo será o campeão do
# campeonato. Se o campeonato tiver 2 ou 3 grupos, os campeões de cada grupo formarão um novo grupo
# e se enfrentarão na fase final nos mesmos moldes do que ocorreu na fase classificatória. O programa
# deverá solicitar ao usuário que seja informado a quantidade de participantes do campeonato e, em
# seguida, realizar automaticamente a divisão desses jogadores nos grupos. O programa também deverá
# simular o campeonato e apresentar os resultados das disputas em cada grupo de forma detalhada, bem
# como quem foi o vencedor em cada grupo. Posteriormente, fazer o mesmo e apresentar os resultados
# das disputas na fase final, caso haja mais de um jogador na fase final. Por fim, informar quem foi o
# vencedor do campeonato. Utilize a função randint() do pacote random do Python variando entre os
# valores 1 e 2 para cada jogada de cada jogador ao longo das disputas que forem simuladas pelo programa.
# Exemplo de uso da função randint():

import random

participantes = int(input("Digite a quantidade de participantes do campeonato: "))
if participantes < 2 or participantes > 9:
    # AHFM: O campeonato na verdade deve ter entre 2 e 9 jogadores
    print("Número inválido de participantes. O campeonato deve ter entre 4 e 9 playerses.")
else:
    if participantes <= 3:
        print("Grupo único com {} players(es)".format(participantes))
    else:
        grupos = participantes // 3
        
        players = 1
        for i in range(grupos):
            print("\n--- Grupo {} ---".format(i+1))
            for _ in range(3):
                print("players {}".format(players))
                wins = 0
                for _ in range(3):
                    jogada = random.randint(1, 2)
                    print("Jogada: {}".format("Par" if jogada == 1 else "Ímpar"))
                    if jogada == 1:
                        wins += 1
                print("Vitórias: {}".format(wins))
                players += 1
            print("Vencedor do Grupo {}: players {}".format(i+1, players-1))
    if grupos > 1:
        print("\n--- Fase Final ---")
        for i in range(grupos):
            print("Vencedor do Grupo {}: players {}".format(i+1, i*3 + 3))

# AHFM RESULTADO DA QUESTÃO 03: 0pts