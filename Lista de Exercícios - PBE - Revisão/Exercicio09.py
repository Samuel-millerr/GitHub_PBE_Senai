# EXERCÍCIO 09 - CLASSIFICACÃO DE RPG

print(f"{"="*5} EXERCÍCIO 09 - RPG {"="*5}")
print("O RPG é definido por desafios, cada desafio tem um nível de dificuldade seguindo a tabela a baixo: ")
print("De 1 à 5 - Pequeno \nDe 6 a 10 - Médio \nDe 11 à 15 - Grande \n")
desafios = (3, 9, 12)

for desafio in desafios:
    if desafio < 1:
        output = "INVÁLIDO"
    elif desafio < 6:
        output = f"A classificação do desafio é {desafio} 'Pequeno'"
    elif desafio < 11:
        output = f"A classificação do desafio é {desafio} 'Médio'"
    elif desafio < 16:
        output = f"A classificação do desafio {desafio} é 'Grande'"
    else:
        output = "INVÁLIDO"
    print(output)
