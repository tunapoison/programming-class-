nome = input("Digite o seu nome: ")
faltas = int(input("Digite a quantidade de faltas no ano letivo: "))

notas = []
count = 0

while count < 3:
    nota = int(input("Digite a sua nota (0-20): "))

    if nota < 0 or nota > 20:
        print("Valor inválido.")
        continue

    count +=1
    notas.append(nota)

media = sum(notas) / len(notas)

if faltas > 10:
    print("Reprovado por notas.")
else:
    if media >= 10:
        print("Aprovado.")
    elif media < 10:
        print("Reprovado por média.")