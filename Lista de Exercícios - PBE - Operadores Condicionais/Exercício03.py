#EXERCÍCIO 03 - VERIFICAÇÃO DE IDADE
idade = int(input("Insira a idade da pessoa: "))

if idade < 0:
    print("IDADE NÃO CORRESPONDENTE!")
elif idade < 18:
    print("MENOR DE IDADE!")
else:
    print("MAIOR DE IDADE!")
