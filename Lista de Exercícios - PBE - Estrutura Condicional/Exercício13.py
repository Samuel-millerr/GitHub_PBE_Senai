#EXERCÍCIO 13 - CLASSIFICAÇÃO DE TEMPERATURA
temperatura = float(input("Digite a temperatura para ser verificada em Celsius: "))

if temperatura < 10:
    print("Frio")
elif temperatura < 25:
    print("Aconchegante")
elif temperatura < 40:
    print("Quente")
else:
    print("Muito Quente")
