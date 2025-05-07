# EXERCÍCIO 01 - ASSISTENTE DE LOJA

print(f"{"="*5} EXERCÍCIO 01 - PROMOÇÃO RELÂMPAGO {"="*5}")

# Definição dos preços dos produtos
precoProdutoA = 5
precoProdutoB = 8
precoProdutoC = 12

# Calculo do dobro do preço dos produtos
dobroProdutoA = precoProdutoA*2
dobroProdutoB = precoProdutoB*2
dobroProdutoC = precoProdutoC*2

# Exibir os valores antigos e novos dos produtos
print("A Black Friday chegou e com isso promoções imperdíveis, segue abaixo os valores antigos "
      "e novos de alguns produtos: \n")
print("Valor antigo:    Valor da Promoção:")
print(f" R${precoProdutoA}                  R${dobroProdutoA}")
print(f" R${precoProdutoB}                  R${dobroProdutoB}")
print(f" R${precoProdutoC}                 R${dobroProdutoC}")

# EXERCÍCIO 02 - SISTEMA DE BOAS VINDAS

print(f"{"="*5} EXERCÍCIO 02 - SEJA BEM VINDO! {"="*5}")
nomes = ("João", "Maria", "Carlos")

print("Seja bem vindo(a) ao nosso curso!!")
print("Agradecemos e desejamos boa sorte para nossos novos alunos: ")
for nome in nomes:
    print(f"> {nome}")

import random
from time import sleep
# EXERCÍCIO 03 - JOGO DE TABULEIRO

print(f"{"="*5} EXERCÍCIO 03 - DADO DE 10 FACES! {"="*5}")

print("Bem vindo ao nosso jogo de tabuleiro! Cuidado, existe uma regra específica no jogo. Seu objetivo principal é chegar até a posição 5"
      " \nGostaria de jogar o dado?")

posicao = 1
escolha = "1"
while escolha == "1":
    escolha = input(" [ 1 ] Jogar dado \n [ 2 ] Sair do jogo \n > ").strip()

    if escolha == "1":
        jogadaDado = random.randint(1, 10)
        print("O número do dado foi")
        for i in range (3):
            print(".")
            sleep(0.5)
        print(jogadaDado)

        if jogadaDado in (4, 7, 10) and jogadaDado % 2 == 0:
            print("Jogador Avança!")
            posicao += 1
        else:
            print("Jogador Recua!")
        print(f"Posição: {posicao}\n")

# EXERCÍCIO 04 - GERADOR DE TABUADAS

print(f"{"="*5} EXERCÍCIO 04 - TABUADA {"="*5}")
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

# EXERCÍCIO 05 - VERIFICADOR DE IDADE

print(f"{"="*5} EXERCÍCIO 05 - CINEMA {"="*5}")
print("Bem vindo!! Para ver o filme é necessário verificar a idade dos clientes. O filme tem classificação de 18 anos.")
print("A princípio temos 3 clientes: ")

clientes = {
    "Lucas": 15,
    "Pedro": 20,
    "Maria": 15
}

print("   Nome    |  Idade   ")
for chave, valor in clientes.items():
    print(f"   {chave}   |   {valor}   ")

print("")
for chave, valor in clientes.items():
    if valor < 18:
        print(f"{chave} não pode entrar no filme!")
    else:
        print(f"{chave} pode entrar no filme!")

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

# EXERCÍCIO 07 - VERIFICADOR DE POEMA

print(f"{"="*5} EXERCÍCIO 07 - POEMA {"="*5}")
print("Olá poeta, vamos verificar a quantidade de letras que tem nas palavras de seu poema, as palavras são as seguintes: ")

palavras = ("casa", "palavra", "python")
for palavra in palavras: print(palavra, end=" ")

print("\n\nSegue a contagem abaixo: ")
for palavra in palavras:
    print(f"{palavra}: {len(palavra)} letras")

# EXERCÍCIO 08 - CONVERSOR DE TEMPERATURA

print(f"{"="*5} EXERCÍCIO 08 - CELSIUS --> FAHRENHEIT {"="*5}")
print("Bem vindo ao conversor de temperatura, segue a baixo as temperaturas que foram convertidas: ")
grausCelsius = ("   30.0", "  100.0", "    0.0")

print("ºCELSIUS ----> ºFAHRENHEIT")
for celsius in grausCelsius:
    fahreheit = (float(celsius)* (9/5)) + 32
    print(f" {celsius}º ----> {fahreheit:.1f}º")

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

# EXERCÍCIO 11 - ESTUDO MATEMÁTICO

print(f"{"="*5} EXERCÍCIO 11 - FATORIAL {"="*5}")
print("Segue abaixo os fatoriais necessários para a realização do estudo: ")
numeros = (3, 7, 9, 25, 26)

for numero in numeros:
    fatorial = 1
    for i in range(1, numero+1):
        fatorial *= i
    print(f"{numero}! = {fatorial}")
