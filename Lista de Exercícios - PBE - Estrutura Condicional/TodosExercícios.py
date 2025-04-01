#EXERCÍCIO 01 - IDENTIFICAÇÃO DE PAR OU IMPAR
numero = int(input("Insira o número que será verificado: "))

if numero % 2 == 0:
    print(f"O número {numero} é par!")
else:
    print(f"O número {numero} é impar!")

#EXERCÍCIO 02 - MAIOR OU MENOR QUE 10
numero = float(input("Insira o número a ser verificado: "))

if numero > 10:
    print("O número é MAIOR a 10!")
elif numero == 10:
    print("O número é IGUAL a 10!")
else:
    print("O número é MENOR que 10!")

#EXERCÍCIO 03 - VERIFICAÇÃO DE IDADE
idade = int(input("Insira a idade da pessoa: "))

if idade < 0:
    print("IDADE NÃO CORRESPONDENTE!")
elif idade < 18:
    print("MENOR DE IDADE!")
else:
    print("MAIOR DE IDADE!")

#EXERCÍCIO 04 - PODE VOTAR?
idade = int(input("Insira a idade para realizar a verificação de voto: "))

if idade < 0:
    print("IDADE INVÁLIDA!")
elif idade < 16:
    print(f"A idade de {idade} anos não tem obrigação de voto.")
elif idade < 18 or idade > 59:
    print("O VOTO É FACULTATIVO!")
else:
    print("O VOTO É OBRIGATÓRIO!")

#EXERCÍCIO 05 - POSITIVO OU NEGATIVO
numero = float(input("Insira o número: "))

if numero == 0:
    print(f"O número é {numero:.0f}")
elif numero > 0:
    print(f"O número {numero:.1f} é maior que zero!")
else:
    print(f"O número {numero:.1f} é menor que zero!")

#EXERCÍCIO 06 - VERIFICAÇÃO DE NOTA
nota = float(input("Insira a nota do aluno: "))

if nota < 0 or nota > 10:
    print("Nota inválida!")
elif nota <= 2:
    print(f"Nota {nota} se classifica como: 'E'")
elif nota <= 4:
    print(f"Nota {nota} se classifica como: 'D'")
elif nota <= 6:
    print(f"Nota {nota} se classifica como: 'C'")
elif nota <= 8:
    print(f"Nota {nota} se classifica como: 'B'")
elif nota <= 10:
    print(f"Nota {nota} se classifica como: 'A'")

#EXERCÍCIO 07 - TEM DESCONTO?
idade = int(input("Insira a idade para ser verificada: "))

if idade < 0:
    print("IDADE INVÁLIDA!")
elif idade <= 12 or idade >=60:
    print("Essa pessoa TEM direito ao desconto!")
else:
    print("Essa pessoa NÃO TEM direito ao desconto!")

#EXERCÍCIO 08 - VERIFICAÇÃO DE TRIANGULO
lado_01 = float(input("Insira o primeiro lado do triangulo: "))
lado_02 = float(input("Insira o segundo lado do triangulo: "))
lado_03 = float(input("Insira o terceiro lado do triangulo: "))

if lado_01+lado_02 < lado_03 or lado_01+lado_03 < lado_02 or lado_02+lado_03 < lado_01:
    print("Essa forma não é um triangulo!")
elif lado_01 == lado_02 == lado_03:
    print("O triangulo é EQUILÁTERO!")
elif lado_01 == lado_02 and lado_01 != lado_03 or lado_01 == lado_03 and lado_01 != lado_03 or lado_02 == lado_03 and lado_03 != lado_01:
    print("O triangulo é ISÓSCELES!")
else:
    print("O triangulo é ESCALENO!")

#EXERCÍCIO 09 - VERIFICAÇÃO DE DESCONTO
valor_compra = float(input("Insira o valor total da compra: "))

if valor_compra < 100:
    desconto = valor_compra*0.05
    valor_descontado = valor_compra-desconto
elif valor_compra > 500:
    desconto = valor_compra*0.15
    valor_descontado = valor_compra-desconto
elif valor_compra <= 0:
    desconto = ""
    valor_descontado = ""
    print("Valor Inválido!")
else:
    desconto = valor_compra*0.1
    valor_descontado = valor_compra-desconto

if desconto != "":
    print("Segue abaixo as informações sobre o desconto: ")
    print("Valor Inicial: R$", valor_compra)
    print("Desconto: R$", desconto)
    print("Valor com Desconto: R$", valor_descontado)
else:
    print("")

#EXERCÍCIO 10 - VERIFICAÇÃO DE ANO BISSEXTO
ano = int(input("Insira o ano a ser verificado: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 100 == 0 and ano % 400 == 0:
    print("O ano é bissexto!")
else:
    print("O ano não é bissexto!")

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

#EXERCÍCIO 12 - CRESCENTE E DECRESCENTE
num_01 = float(input("Insira o primeiro número: "))
num_02 = float(input("Insira o segundo número: "))
num_03 = float(input("Insira o terceiro número: "))

if num_01 == num_02 == num_03:
    print("Os números são todos iguais.")
elif num_01 > num_02 > num_03 or num_03 == num_02 < num_01 or num_01 == num_02 > num_03:
    print("Ordem Decrescente.")
elif num_03 > num_02 > num_01 or num_01 == num_02 < num_03 or num_02 == num_03 > num_01:
    print("Ordem Crescente.")
else:
    print("Os números estão e ordem aleatória.")

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

#EXERCÍCIO 14 - FORMATO DE DATA 1.0
data = input("Insira a data no seguinte formato (dd/mm/aaaa): ")

if len(data) == 10 and data[2] == "/" and data[5] == "/":

    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:10])

    if dia > 31 or mes > 12:
        print("Insira um valor correto para o dia ou mês.")
    else:
        print(f"{ano}/{mes:02d}/{dia:02d}")
else:
    print("Formato Inválido, digite no formado correto (dd/mm/aaaa).")

#EXERCÍCIO 15 - VALIDAÇÃO DE SENHA
import re

print("Critérios para criação de uma nova senha:")
print("• Pelo menos 8 caracteres.")
print("• Pelo menos uma letra maiúscula.")
print("• Pelo menos uma letra minúscula.")
print("• Pelo menos um número.")
print("• Pelo menos um caractere especial (@, #, $, %, &).")

senha = input("\nDigite a senha: ")
criterios = []

if len(senha) < 8:
    criterio_quant_caracter = bool(0)
    criterios.append("A senha não tem 8 ou mais caracteres.")
else:
    criterio_quant_caracter = bool(1)

if re.search(r"[a-z]", senha):
    criterio_minusculas = bool(1)
else:
    criterio_minusculas = bool(0)
    criterios.append("A senha não possui letras minusculas")

if re.search("[A-Z]", senha):
    criterio_maiusculas = bool(1)
else:
    criterio_maiusculas = bool(0)
    criterios.append("A senha não possui letras maiúsculas.")

if re.search(r"\d", senha):
    criterio_numero = bool(1)
else:
    criterio_numero = bool(0)
    criterios.append("A senha não possui nenhum número.")

if re.search("[@#$%&]", senha):
    criterio_especial = bool(1)
else:
    criterio_especial = bool(0)
    criterios.append("A senha não possui nenhum caractere especial.")

if len(criterios) == 0:
    print("Senha Válida! A senha segue todos os critérios estabelecidos.")
else:
    print("Senha Inválida! Os critérios abaixo não foram seguidos.")
    for criterio in criterios:
        print(criterio)

#EXERCÍCIO 16 - CALCULO DE RAIZ QUADRADA
import math
numero = int(input("Insira o número para realizar a conta da raiz quadrada: "))

if numero < 0:
    print("Não é possível calcular a raiz quadrada um número negativo.")
elif numero > 100:
    print("Número muito grande, reduza para um valor abaixo de 100.")
else:
    print(f"A raiz quadrada do número {numero} é {math.sqrt(numero):.2f}")

#EXERCÍCIO 17 - FORMATO DE DATA 2.0
data = input("Insira a data no seguinte formato (dd/mm/aaaa): ")

if len(data) == 10 and data[2] == "/" and data[5] == "/":

    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:10])

    if ano % 4 == 0 and ano % 100 != 0 or ano % 100 == 0 and ano % 400 == 0:
        ano_bissexto = "sim"
    else:
        ano_bissexto = "nao"

    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        quant_dias = "30"
    else:
        quant_dias = "31"

    if mes > 12:
        print("Insira um valor correto para o mês.")
        mes = str(mes)
    elif ano_bissexto == "sim" and mes == 2 and dia > 29:
        print("Insira um valor correto para o dia (fevereiro em ano bissexto tem apenas 29 dias.")
    elif ano_bissexto == "nao" and mes == 2 and dia > 28:
        print("Insira um valor correto para o dia (fevereiro em anos normais tem apenas 28 dias.)")
    elif quant_dias == "30" and dia > 30:
        print("Insira um valor correto para o dia (o mes que escolheu tem apenas 30 dias.)")
    elif quant_dias == "31" and dia > 31:
        print("Insira um valor correto para o dia (o mes que escolheu tem apenas 31 dias.)")
    else:
        print(f"{ano}/{mes:02d}/{dia:02d}")

else:
    print("Formato Inválido, digite no formado correto (dd/mm/aaaa).")

#EXERCÍCIO 18 - CALCULADORA
expressao = input("Insira a expressão matématica para ser calculada: ")
print(f"O resultado é {eval(expressao)}")

#EXERCÍCIO 19 - DESAFIO
cpf = input("Insira o se CPF para ser realizado a verificação, na seguinte estrutura XXX.XXX.XXX-XX: ")

if len(cpf) < 14:
    print("CPF Inválido! O CPF não possui 11 dígitos.")
else:
    if cpf[3] != "." or cpf[7] != "." or cpf[11] != "-":
        print("CPF Inválido. Digite o CPF na estrutura correta, com os pontos e o traço.")
    else:
        digito01 = int(cpf[0]) * 10
        digito02 = int(cpf[1]) * 9 + digito01
        digito03 = int(cpf[2]) * 8 + digito02
        digito04 = int(cpf[4]) * 7 + digito03
        digito05 = int(cpf[5]) * 6 + digito04
        digito06 = int(cpf[6]) * 5 + digito05
        digito07 = int(cpf[8]) * 4 + digito06
        digito08 = int(cpf[9]) * 3 + digito07
        digito09 = int(cpf[10]) * 2 + digito08

        if digito09 % 11 < 2:
            digito_verificador_01 = 0
        else:
            digito_verificador_01 = 11 - (digito09 % 11)

        digito01 = int(cpf[0]) * 11
        digito02 = int(cpf[1]) * 10 + digito01
        digito03 = int(cpf[2]) * 9 + digito02
        digito04 = int(cpf[4]) * 8 + digito03
        digito05 = int(cpf[5]) * 7 + digito04
        digito06 = int(cpf[6]) * 6 + digito05
        digito07 = int(cpf[8]) * 5 + digito06
        digito08 = int(cpf[9]) * 4 + digito07
        digito09 = int(cpf[10]) * 3 + digito08
        digito10 = int(cpf[12]) * 2 + digito09

        if digito10 % 11 < 2:
            digito_verificador_02 = 0
        else:
            digito_verificador_02 = 11 - (digito10 % 11)

        if digito_verificador_01 == int(cpf[12]) and digito_verificador_02 == int(cpf[13]):
            print(f"CPF Válido! Os número verificadores são {digito_verificador_01} e {digito_verificador_02} respectivamente.")
        else:
            print(f"CPF Inválido!")