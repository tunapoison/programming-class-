# Estrutura de seleção múltipla - PG 62
# Usar if loops é uma alternativa

dia = int(input("Escreve um número para que representa um dia da semana (1-7): "))
match dia:
    case 1:
        print("O dia é segunda-feira.")
    case 2:
        print("O dia é terça-feira.")
    case 3:
        print("O dia é quarta-feira.")
    case 4:
        print("O dia é quinta-feira.")
    case 5:
        print("O dia é sexta-feira.")
    case 6:
        print("O dia é sábado.")
    case 7:
        print("O dia é domingo.")
    case _:
        print("Valor inválido.")

# ou

if dia == 1:
    print("O dia é segunda-feira.")
elif dia == 2:
    print("O dia é terça-feira.")
elif dia == 3:
    print("O dia é quarta-feira.")
elif dia == 4:
    print("O dia é quinta-feira.")
elif dia == 5:
    print("O dia é sexta-feira.")
elif dia == 6:
    print("O dia é sábado.")
elif dia == 7:
    print("O dia é domingo.")
else:
    print("Valor inválido.")