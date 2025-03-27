#EXERCÍCIO 08 - VERIFICAÇÃO DE DESCONTO
valor_compra = float(input("Insira o valor total da compra: "))

if valor_compra < 100:
    desconto = valor_compra*0.05
    valor_descontado = valor_compra-desconto
elif valor_compra > 500:
    desconto = valor_compra*0.15
    valor_descontado = valor_compra-desconto
elif valor_compra <= 0:
    desconto = ""
    valor_descontado = ""
    print("Valor Inválido!")
else:
    desconto = valor_compra*0.1
    valor_descontado = valor_compra-desconto

if desconto != "":
    print("Segue abaixo as informações sobre o desconto: ")
    print("Valor Inicial: R$", valor_compra)
    print("Desconto: R$", desconto)
    print("Valor com Desconto: R$", valor_descontado)
else:
    print("")
