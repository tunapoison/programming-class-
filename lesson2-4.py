produto = input("Escreve um produto a comprar: ")
quantidade = int(input("Escreve a quantidade: "))
preco = float(input("Escreve o preço do produto: "))

print(f"O valor a pagar por {quantidade} de {produto} é {quantidade * preco: .2f}")
print("O valor a pagar por {} unidades de {} é {}".format(quantidade, produto, quantidade * preco))
