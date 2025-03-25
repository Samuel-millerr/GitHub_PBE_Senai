#EXERCÍCIO 05 - POSITIVO OU NEGATIVO
numero = float(input("Insira o número: "))

if numero == 0:
    print(f"O número é {numero:.0f}")
elif numero > 0:
    print(f"O número {numero:.1f} é maior que zero!")
else:
    print(f"O número {numero:.1f} é menor que zero!")
