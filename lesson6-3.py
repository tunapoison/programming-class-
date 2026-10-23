num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
op = input("Escolhe a operação que pretende usar entre os dois números (+ - / *): ")

if op == "+":
    print(f"O resultado é {num1 + num2}.")
elif op == "-":
    print(f"O resultado é {num1 - num2}.")
elif op == "/":
    print(f"O resultado é {num1 / num2}.")
elif op == "*":
    print(f"O resultado é {num1 * num2}.")
else:
    print("Valor inválido.")