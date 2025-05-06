# EXERCÍCIO 04 - GERADOR DE TABUADAS

print(f"{"="*5} EXERCÍCIO 03 - TABUADA {"="*5}")
print("Bem vindo ao gerador de tabuadas!! Nesse gerador ira ser gerado as tabuadas do 2, do 3 e do 4.")

numeros = {
    "numero 2": 2,
    "numero 3": 3,
    "numero 4": 4
}

for chave, valor in numeros.items():
    print(f"\nTabuada do {valor}")
    for i in range(11):
        print(f"{valor} * {i} = {valor*i}")

