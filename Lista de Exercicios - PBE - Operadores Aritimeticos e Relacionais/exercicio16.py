#EXERCICIO 16 - PLANO CARTESIANO
import math
x1 = float(input("Insira o X do primeiro ponto: "))
y1 = float(input("Insira o Y do primeiro ponto: "))
x2 = float(input("Insira o X do segundo ponto: "))
y2 = float(input("Insira o Y do segundo ponto: "))

distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(f"A distância entre os dois pontos é de {distancia:.2f}.")
