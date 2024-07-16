alternativa = input("Qual dessas empresa tem a CPU focada em jogos.\nAmd\nIntel\n").lower()     


if "amd" in alternativa:
    print("Certo, a empresa é a Amd!")
elif "intel" in alternativa:
    print("Errou, empresa que foca em jogos é AMD")