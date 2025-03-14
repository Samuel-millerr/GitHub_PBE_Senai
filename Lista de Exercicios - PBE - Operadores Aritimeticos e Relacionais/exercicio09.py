#EXERCICIO 09 - COMPARAÇÃO DE NÚMEROS
num1 = float(input("Insira o primeiro número para a verificação: "))
num2 = float(input("Insira o segundo número para a verificação: "))

print(f"{num1:.1f} é maior que {num2:.1f}? \n{num1 > num2}")
print(f"{num2:.1f} é maior que {num1:.1f}? \n{num2 > num1}")
print(f"Os números {num1:.1f} e {num2:.1f} são iguais? \n{num1 == num2}")