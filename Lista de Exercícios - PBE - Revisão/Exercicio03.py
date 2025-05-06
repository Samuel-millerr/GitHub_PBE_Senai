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