nome = input("Digite o seu nome completo: ").strip()

resultado1 = nome.upper()
resultado2 = nome.lower()
resultado3 = len(nome)
resultado4 = nome.split()

primeiro_nome = resultado4[0]
quantidade_letras_primeiro_nome = len(primeiro_nome)  


print("O seu nome com todas as letras maiúsculas {}, seu nome com todas as letras minúsculas {}, quantas letras tem ao todo {}, quantas letras teu o primeiro nome {}.".format(resultado1, resultado2, resultado3, quantidade_letras_primeiro_nome - nome.count(" ")))

