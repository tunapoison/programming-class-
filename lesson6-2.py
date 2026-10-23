altura = int(input("Digite a sua altura em centímetros: "))
sexo = input("Digite o seu sexo (M/F): ")
match sexo:
    case "M"|"m": # M ou m
        print(f"O seu peso ideal é {52 + (0.75 * (altura - 152.4)):.2f} kilogramas.")
    case "F"|"f": # F ou f
        print(f"O seu peso ideal é {52 + (0.67 * (altura - 152.4)):.2f} kilogramas.")
    case _:
        print("Valor inválido.")

#ou

if sexo == "M" or sexo == "m":
    print(f"O seu peso ideal é {52 + (0.75 * (altura - 152.4)):.2f} kilogramas.")
elif sexo == "F" or sexo == "f":
    print(f"O seu peso ideal é {52 + (0.67 * (altura - 152.4)):.2f} kilogramas.")
else:
    print("Valor inválido.")