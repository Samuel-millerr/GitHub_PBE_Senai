# EXERCÍCIO 07 - VERIFICADOR DE POEMA

print(f"{"="*5} EXERCÍCIO 07 - POEMA {"="*5}")
print("Olá poeta, vamos verificar a quantidade de letras que tem nas palavras de seu poema, as palavras são as seguintes: ")

palavras = ("casa", "palavra", "python")
for palavra in palavras: print(palavra, end=" ")

print("\n\nSegue a contagem abaixo: ")
for palavra in palavras:
    print(f"{palavra}: {len(palavra)} letras")

