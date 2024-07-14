# O print é para exibir informações no terminal.
print ("Quero meu primeiro emprego")

# Variáveis, o papel da variável é armazenar dados, seja texto, arquivos inteiros, númeoros e afins.

# Variável boolean
is_python = True
is_java = False

# armazenando condições
ingressos = 50
compradores = 250
tem_ingressos_suficiente = (ingressos >= compradores)
print (tem_ingressos_suficiente)

#fixação

# Introdução ao INPUT, armazena entrada de dados do usuário. único problema do INPUT é que ele retorna os valores em string, e em certos momentos precisamos faze a conversão.
# Conversão com FLOA e INT. Idade=int, peso=float.

nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
peso = float(input("Digite seu peso:"))

# Forma de saber o tipo da variável é utilizando o TYPE.

print(nome)
print(type(idade))
print(type(peso))

# Operadores

soma = 1+1
multiplicacao = 27*30
divisao = 28/7
potencia = 7**9

print ("soma", soma)
print ("multiplicacao", multiplicacao)
print ("divisao", divisao)
print ("potencia", potencia)

# condicionais, o que é condições? É a mudança de fluxo baseado na condição.

idade = int(input("qual a sua idade:"))

# Blocos de instrução, os blocos de construção estão alinhados a condição acima. Por isso o código é jogado para frente, geralmente usamos um TAB para alinha o bloco com a condição acima.

if idade >=18:
    print("Permitido a entrada!")
else:
    print("Acesso negado")

# Fixação!

salario = float(input("Informe seu salário:"))

if salario <= 3000:
    print("prgramador junior")
elif salario > 3000 and salario <=6000:
    print("Programador pleno")
elif salario > 6000 and salario <=15000:
    print("Programador senior")
else:
    print("Gerente de projetos")         

# Utilização do ELIF=Ou, então.   AND para por mais uma condição mo seu if/else/elif.

# Listas, as listas tem um index:0, 1, 2, [...] Sempre começam com o 0. Caso queira acesesar o índice da lista 1, você acessa a posição 0, caso queira acessar o índice 3, você acessa a posição 2. E assim por diante.
# Alterando os itens da lista.

lista_numeros = [1, 2, 3]

lista_numeros[0] = 5

print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])

numeros = [1, 2, 3]
strings = ["Joao", "Maria", "Bruxa"]
decimais = [10.8, 15.2, 33.3]

#As listas podem ter diferentes dados, como nomes, números decimais, strings, números inteiros e qualquer outro tipo de dados.

#fixação

lista_vazia =[]
lista_vazia.append("Olá")
lista_vazia.append("Mundo")
print(lista_vazia)

#Total de itens da lista EX:

numeros = [10, 9, 8, 7, 6]

print ("total:", len(numeros))
print ("menor valor:", min(numeros))
print ("maior valor:", max(numeros))

#repetições

#FOR, loop que percorre sequências, repertindo ações para cada elemento.
for x in range(10):
    print(x)
# WHILE, loop que executa ações enquanto a condição for verdadeira.
while True:
    print("se eu rodar script meu pc morre")

#Aqui vemos um sistema de automação FOR X IN. A função RANGE cria uma sequência de números, e assim como de 0 a 4 são 5 números percorridos. O x é atribuido como valor 0 no inicio, então na execução vai de [0,1,2,3,4], de 0~4 são 5 número, dentro do código são execução dentro do loop. Como visto anteriormente esse é o processo de listagem. Valor 3 tem como acesso o 2 e assim por diante.
    #for x in range(5):

#fixação

for x in range(300):
    codigo_aluno = input("RM:")
    nota = float (input("Nota:"))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

print ("quantidade de notas", len(notas))

for n in notas:
    codigo_aluno = n [0]
    nota = n [1]
    print("O RM", codigo_aluno, "tirou a nota", nota)

# Exemplo com WHILE=Enquanto.

notas = []

contador = 1

while contador <=5:
    codigo_aluno = inpuy("RM:")
    nota = float (input("Nota:"))
    resultado = [codigo_aluno]
    nota.append(resultado)

    # alternativ: contador +=1

    contador = contador + 1

print ("quantidade_notas", len(notas))

# Dicionários usam chave e valor para armazenar informações

#Exemplo:

pessoa = {
    "nome":"programador python",
    "idade":27,
    "peso":70.2
}

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['peso'])

#Fixação

player = {
    "nome":"Bass",
    "level":1,
    "hp":100,
    "exp":0,
    "dano":5,
}

#lista de inimigos

npcs = [
    {"nome":"Monstrinho", "dano": 2, "hp": 50, "exp": 5},
    {"nome":"Monstro", "dano": 5, "hp": 100, "exp": 10},
    {"nome":"Monstrão", "dano": 10, "hp": 150, "exp": 15},
    {"nome":"Chefão", "dano":40, "hp": 300, "exp":50},
]

#Chat de mensagens

import os

mensagens = []

nome = input("Nome:")
    
while True:    
    
    #Limpando terminal
    
    os.system('cls')
    if len (mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m ['texto'])

    print("______________")
    
    #Obtendo texto

    texto = input("mensagem:")
    if texto == "fim":
        break

    #Adicionando mensagem na lista 
    
    mensagens.append({
        "nome":nome,
        "texto":texto
    })

    #Funções são blocos reutilizáveis de códigos para agilizar tarefas e deixar o código mais dinâmico. Além de realizar tarefas específicas, no lugar de repetir o código diversas vezes até atingir o objetivo, podemos criar uma função e chama-lá assim que for necessário.
    #Dessa forma, aproveitamos código ao invês de replicar, deixando o código cada vez maior, duplicando ou triplicando os lugares que precisam de manuntenção.
    
    #Exemplo:
def minha_funcao(valor1, valor2):
    return valor1 + valor2

while True:
    valor1 = int(input("valor1:"))
    valor2 = int(input("valor2:"))
    resposta = minha_funcao (10, 10)

    print(valor1,"+", valor2, "=", resposta)

#Parâmetros, são dados para função, nem sempre a função vai retorna alguma coisa mas é possível ela retorna com RETURN.

#Fixação

fluxo_caixa = []

print("------------")
print("@Fluxo caixa")
print("------------")
print("1 - adicionar receita")
print("2 - adicionar receita")
print("\n#Digite outro numero para encerrar#\n")

def adiconar_transacao():
    nome = input ("nome:")
    valor = float(input("valor:"))
    flurxo_caixa.append({
        "nome":nome,
        "valor":valor
        })

while True:
    opcao = int (input("Digite a opção"))

    if opcao == 1:
        adiconar_transacao()
    elif opcao == 2:
        adiconar_transacao()
    else:
        break

    total = 0 
    for fc in fluxo_caixa:
        print("nome:", fc ['nome'], ", valor:R$", fc ['valor'])
        total = total + fc ['valor']
    print("Salario atual: R$", total)    