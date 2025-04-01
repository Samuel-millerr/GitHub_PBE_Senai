#EXERCICIO 01 - EXIBIÇÃO DE NOME
nome = "João"
print(nome)

#EXERCICIO 02 - OPERAÇÕES BÁSICAS
a = 5
b = 10

soma = a+b
subtracao = a-b
multiplicacao = a*b
divisao = a/b

print(f"O resultado das operações é: \nSoma: {soma} \nSubtração: {subtracao} \nMultiplicação: {multiplicacao}\nDivisão: {divisao}")

#EXERCICIO 02 - OPERAÇÕES BÁSICAS
a = 5
b = 10

soma = a+b
subtracao = a-b
multiplicacao = a*b
divisao = a/b

print(f"O resultado das operações é: \nSoma: {soma} \nSubtração: {subtracao} \nMultiplicação: {multiplicacao}\nDivisão: {divisao}")

#EXERCICIO 03 - DESCONTO APLICADO
preco = 50
desconto = 10
preco_final = preco-desconto

print(f"O preço inicial é de {preco} e o desconto é de {desconto}.")
print(f"O valor com desconto é {preco_final}.")

#EXERCICIO 04 - CALCULO
resultado = 10 + 5 * 2

print(f"O resultado da operação é: {resultado}")

#EXERCICIO 05 - CONVERSOR DE VARIÁVEL
numero_txt = "150"
numero = int(numero_txt)
print(f"O resultado de {numero_txt} * 2 é {numero*2}.")

#EXERCICIO 06 - LISTA DE NÚMEROS
numeros = [1, 2, 3, 4, 5]
print(numeros)
numeros[1] = 20
print(numeros)

#EXERCICIO 07 - SOMA DE VARIÁVEIS
a = float(input("Insira o primeiro número para a soma: "))
b = float(input("Insira o segundo número para a soma "))
print(f"A soma de {a:.1f} e {b:.1f} é {a+b:.1f}")

#EXERCICIO 08 - DIVISÃO DE VARIÁVEIS
x = float(input("Insira o primeiro número para a divisão: "))
y = float(input("Insira o segundo número para a divisão: "))
print(f"A divisão inteira de {x:.1f} e {y:.1f} é {(x // y):.1f}")

#EXERCICIO 09 - COMPARAÇÃO DE NÚMEROS
num1 = float(input("Insira o primeiro número para a verificação: "))
num2 = float(input("Insira o segundo número para a verificação: "))

print(f"{num1:.1f} é maior que {num2:.1f}? \n{num1 > num2}")

#EXERCICIO 10 - CALCULO ETÁRIO
idade = int(input("Insira a idade respectiva para o calculo: "))
print(f"Essa pessoa viveu aproximadamente {idade*365} dias")

#EXERCICIO 11 - POTENCIAÇÃO
base = float(input("Insira a base da potenciação: "))
expoente = int(input("Insira o expoente da potenciação: "))
print(f"O resultado da potenciação é {base**expoente:.1f}")

#EXERCICIO 12 - CONVERSÃO DE VARIÁVEL
preco = int(input("Insira o preço determinado: "))
preco_txt = str(preco)
print("O preço é R$" + preco_txt)

#EXERCICIO 13 - ÁREA DE UM CIRCULO
raio = float(input("Insira o raio do circulo em CM: "))
print(f"A área do circulo é {3.14 * raio**2} CM")

#EXERCICIO 14 - TROCA DE VARIÁVEIS
a = float(input("Insira o primeiro número: "))
b = float(input("Insira o segundo número: "))
print(f"{a:.1f}, {b:.1f}")

a, b = b,a
print(f"{a:.1f}, {b:.1f}")

#EXERCICIO 15 - MÉDIA DE NOTAS
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))

print(f"As notas com seus respectivos pesos são: \n{nota1:.1f} com o peso de 2 \n{nota2:.1f} com peso de 3 \n"
      f"{nota3:.2} com peso de 5 \nA média das notas é {(nota1*2 + nota2*3 + nota3*5)/(2+3+5):.2f}")


#EXERCICIO 16 - PLANO CARTESIANO
import math
x1 = float(input("Insira o X do primeiro ponto: "))
y1 = float(input("Insira o Y do primeiro ponto: "))
x2 = float(input("Insira o X do segundo ponto: "))
y2 = float(input("Insira o Y do segundo ponto: "))

distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(f"A distância entre os dois pontos é de {distancia:.2f}.")


