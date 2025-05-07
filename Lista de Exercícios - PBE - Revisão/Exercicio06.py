# EXERCÍCIO 06 - APLICAÇÃO DE DESCONTO

print(f"{"="*5} EXERCÍCIO 06 - LOJA {"="*5}")
print("Bem vindo a nossa loja!! Segue abaixo a tebela de descontos dessa semana: ")

produtos = {
    "Bolsa": "50 ",
    "Calça": "120",
    "Tênis": "200"
}

print("   Produto   |   Valor Original   |   Valor com Desconto   ")
for chave, valor in produtos.items():
    print(f"    {chave}    |        R${valor}       |      R${int(valor)*1.1:.2f}    ")
