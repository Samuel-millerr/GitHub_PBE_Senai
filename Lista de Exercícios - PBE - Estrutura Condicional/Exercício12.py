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