#EXERCÍCIO 07 - TEM DESCONTO?
idade = int(input("Insira a idade para ser verificada: "))

if idade < 0:
    print("IDADE INVÁLIDA!")
elif idade <= 12 or idade >=60:
    print("Essa pessoa TEM direito ao desconto!")
else:
    print("Essa pessoa NÃO TEM direito ao desconto!")