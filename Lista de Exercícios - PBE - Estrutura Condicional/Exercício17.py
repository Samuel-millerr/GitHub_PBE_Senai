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
