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