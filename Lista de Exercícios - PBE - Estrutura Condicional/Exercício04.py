#EXERCÍCIO 04 - PODE VOTAR?
idade = int(input("Insira a idade para realizar a verificação de voto: "))

if idade < 0:
    print("IDADE INVÁLIDA!")
elif idade < 16:
    print(f"A idade de {idade} anos não tem obrigação de voto.")
elif idade < 18 or idade > 69:
    print("O VOTO É FACULTATIVO!")
else:
    print("O VOTO É OBRIGATÓRIO!")