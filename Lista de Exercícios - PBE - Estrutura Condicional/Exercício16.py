#EXERCÍCIO 16 - CALCULO DE RAIZ QUADRADA
import math
numero = int(input("Insira o número para realizar a conta da raiz quadrada: "))

if numero < 0:
    print("Não é possível calcular a raiz quadrada um número negativo.")
elif numero > 100:
    print("Número muito grande, reduza para um valor abaixo de 100.")
else:
    print(f"A raiz quadrada do número {numero} é {math.sqrt(numero):.2f}")