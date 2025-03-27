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