#EXERCÍCIO 10 - VERIFICAÇÃO DE ANO BISSEXTO
ano = int(input("Insira o ano a ser verificado: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 100 == 0 and ano % 400 == 0:
    print("O ano é bissexto!")
else:
    print("O ano não é bissexto!")