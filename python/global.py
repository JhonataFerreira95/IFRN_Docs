cs2 = input("Ei, você joga cs2? (sim ou não): ").lower()

if "sim" in cs2:
    tempo = input("Joga a quanto tempo?: ")
    print("Que legal, {} é bastante tempo!".format(tempo))
elif "não" in cs2:
    print("Que pena!")
