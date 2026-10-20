# Programa que calcula a soma de nºs pares num determinado intervalo
# Calcula quantos nºs impares existem nesse intervalo

num1 = int(input("Digite o menor número do intervalo: "))
num2 = int(input("Digite o maior número do intervalo: "))

par = 0
impar = 0

for i in range(num1, num2+1):
    if i % 2 == 0:
        par += i
    else:
        impar += 1

print(f"A soma dos nºs pares é {par}.")
print(f"A quantidade de números impares é {impar}.")