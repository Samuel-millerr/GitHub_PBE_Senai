#EXERCICIO 14 - TROCA DE VARIÁVEIS
a = float(input("Insira o primeiro número: "))
b = float(input("Insira o segundo número: "))
print(f"{a:.1f}, {b:.1f}")

a, b = b,a
print(f"{a:.1f}, {b:.1f}")