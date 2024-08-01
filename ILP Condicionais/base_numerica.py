while True:
    try:
        base = int(input("Digite um número inteiro positivo: "))
        
        if base < 0:
            print("Por favor, digite um número inteiro positivo.")
            continue

        print("Qual base desejada:\n[1] Binário\n[2] Octal\n[3] Hexadecimal\n")
       
        opcao = int(input("Digite sua opção: "))

        if opcao == 1:
            print("{} convertido para binário é igual {}".format(base, bin(base)[2:]))
            break
        elif opcao == 2:
            print("{} convertido para octal é igual {}".format(base, oct(base)[2:]))
            break
        elif opcao == 3:
            print("{} convertido para hexadecimal é igual {}".format(base, hex(base)[2:]))
            break
        else:
            print("Opção inválida, tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro positivo.")

# Cara, eu juro, tentei faze os calculos sem os conversores naturais do python e isso ficou imenso
# # Solicita um número decimal ao usuário
# numero_decimal = int(input("Digite um número decimal: "))

# # Inicializa uma lista para armazenar os restos
# restos = []

# # Enquanto o número decimal for maior que 0
# while numero_decimal > 0:
#     # Calcula o quociente e o resto
#     quociente = numero_decimal // 2
#     resto = numero_decimal % 2
    
#     # Adiciona o resto à lista
#     restos.append(resto)
    
#     # Atualiza o número decimal para o quociente
#     numero_decimal = quociente

# # Os restos estão na ordem inversa, então invertemos a lista
# restos.reverse()

# # Converte a lista de restos em uma string
# numero_binario = ''.join(str(bit) for bit in restos)

# # Exibe o resultado
# print("O número em binário é:", numero_binario)



