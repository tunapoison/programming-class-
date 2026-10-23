num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

print("Somar  +")
print("Subtrair  -")
print("Dividir  /")
print("Multiplicar  *")
print("Potenciar  **")
print("Módulo (resto)  %")

op = input("Escolhe a operação que pretende usar entre os dois números: ")

match op:
    case "+":
        print(f"O resultado é {num1 + num2}.")
    case "-":
        print(f"O resultado é {num1 - num2}.")
    case "/":
        print(f"O resultado é {num1 / num2}.")
    case "*":
        print(f"O resultado é {num1 * num2}.")
    case "**":
        print(f"O resultado é {num1 ** num2}.")
    case "%":
        print(f"O resultado é {num1 % num2}.")
    case _:
        print("Valor inválido.")