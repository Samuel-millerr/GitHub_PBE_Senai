# EXERCÍCIO 10 - PALÍNDROMOS

print(f"{"="*5} EXERCÍCIO 10 - VERIFICAÇÃO DE PALÍNDROMOS {"="*5}")
print("Os títulos dos capítulos já foram recebidos, agora vamos verificar quais dos nomes são palíndromos.")
print("A seguir a lista dos capítulos e se eles são palíndromos: \n")
titulos = ("Ana Ana", "1DSTB-SENAI", "Subi no Onibus")

for titulo in titulos:
    if titulo.upper() == titulo[::-1].upper():
        print(titulo + " - É um palíndromo")
    else:
        print(titulo + " - Não é um palíndromo")