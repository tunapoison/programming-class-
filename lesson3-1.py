nome = input("Digite o seu nome: ")
peso = float(input("Digite o seu peso: "))
if peso < 70:
    dif = 70.0 - peso
    print(f"Falta ao {nome} {dif: .2f} kg para antingir os 70 kg.")
else:
    dif = peso - 70.0
    print(f"Pesa mais {dif: .2f} kg do que os 70 kg.")