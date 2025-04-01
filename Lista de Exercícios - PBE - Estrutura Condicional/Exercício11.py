#EXERCÍCIO 11 - VERIFICAÇÃO DE ANO BISSEXTO
altura = float(input("Digite o sua altura em M (ex: 1.70): "))
peso = float(input("Digite seu peso em KG (ex: 64.8): "))

imc = peso/(altura**2)

if altura < 0 or peso < 0:
    print("Peso ou altura inválidos, tente novamente!")
    classificacao = ""
    x = ""
elif imc < 18.5:
    classificacao = "Abaixo do peso"
    x = "classificado"
elif imc < 25:
    classificacao = "Peso normal"
    x = "classificado"
elif imc < 30:
    classificacao = "Sobrepeso"
    x = "classificado"
else:
    classificacao = "Obesidade"
    x = "classificado"

if x != "":
    print(f"O seu IMC é de {imc:.2f}. \nClassificação: {classificacao}")


