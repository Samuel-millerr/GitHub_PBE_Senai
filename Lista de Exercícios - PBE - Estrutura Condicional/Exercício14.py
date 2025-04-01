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