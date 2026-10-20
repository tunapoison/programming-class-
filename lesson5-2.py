# Programa que calcula a média de 6 notas da disciplina

notas = []

count = 0

while count < 6:
    nota = int(input("Digite a nota da disciplina (0-20): "))

    if nota < 0 or nota > 20:
        print("Nota inválida. Tente novamente.")
        continue

    count += 1
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"A média das notas é {round(media)} valores.")