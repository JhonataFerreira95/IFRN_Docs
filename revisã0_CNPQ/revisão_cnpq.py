import sys  # Importa o modulo sys, mas não é usado no codgo

# Pede ao usuario quantos processos deseja simular e converte a entrada para um inteiro
numero_de_processos = int(input("Quantos processos deseja simular? "))
processos = []  # Cria uma lista vazia para armazenar os tempos dos procosses

# Inicia um loop que vai de 0 até o numero de processos que o usuario digitou
for count in range(numero_de_processos):
    # Pede para o usuario digitar o tempo do processo atual
    tempo = int(input(f"Digite o tempo do processo {count + 1}: "))
    processos.append(tempo)  # Adiciona o tempo digitado à lista de processos

# Pergunta ao usuario qual algoritmo deseja usar
algoritmo = input("Escolha o algoritmo que deseja usar (Fifo/SJF/RR): ")

# Verifica se o algoritmo escolhido é SJF (Shortest Job First)
if algoritmo.upper() == "SJF":
    sorted_processes = []  # Cria uma lista para armazenar os processos ordenados
    temp_processes = processos.copy()  # Faz uma copia da lista de processos

    # Continua enquanto ainda houver processos na lista temp_processes
    while len(temp_processes) > 0:
        min_index = 0  # Inicializa min_index como 0 para encontrar o menor tempo
        # Inicia um loop para comparar os tempos dos procosses
        for i in range(1, len(temp_processes)):
            # Verifica se o tempo do processo atual é menor que o tempo do processo no min_index
            if temp_processes[i] < temp_processes[min_index]:
                min_index = i  # Atualiza min_index se encontrar um tempo menor

        sorted_processes.append(temp_processes[min_index])  # Adiciona o menor tempo à lista ordenada
        temp_processes.pop(min_index)  # Remove o processo com o menor tempo da lista original

    turnaround_times = []  # Cria uma lista para armazenar os tempos de turnaround
    total_turnaround_time = 0  # Inicializa o tempo total de turnaround como 0

    # Itera sobre a lista de processos ordenados
    for i in range(len(sorted_processes)):
        turnaround_time = 0  # Inicializa o tempo de turnaround do processo atual como 0
        # Soma os tempos de todos os processos até o atual
        for j in range(i + 1):
            turnaround_time += sorted_processes[j]

        turnaround_times.append(turnaround_time)  # Adiciona o tempo de turnaround à lista
        total_turnaround_time += turnaround_time  # Soma o tempo de turnaround ao total

    # Calcula o tempo medio de turnaround
    tempo_medio = total_turnaround_time / len(sorted_processes)

    print("O tempo de turnaround de cada processo foi:")  # Informa que os tempos serão exibidos
    print(" ".join(map(str, turnaround_times)))  # Imprime os tempos de turnaround
    print(f"O tempo médio foi de {tempo_medio:.2f}")  # Imprime o tempo medio formatado
else:
    print("Algoritmo não suportado.")  # Informa que o algoritmo não é suportado