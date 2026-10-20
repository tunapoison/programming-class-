num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número diferente: "))

if num1 == num2:
    print("Os números são iguais.")
elif num1 > num2:
    print(f"O maior é {num1}.")
else:
    print(f"O maior é {num2}.")