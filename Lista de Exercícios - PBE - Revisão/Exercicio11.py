# EXERCÍCIO 11 - ESTUDO MATEMATÍCO

print(f"{"="*5} EXERCÍCIO 11 - FATORIAL {"="*5}")
print("Segue abaixo os fatoriais necessários para a realização do estudo: ")
numeros = (3, 7, 9, 25, 26)

for numero in numeros:
    fatorial = 1
    for i in range(1, numero+1):
        fatorial *= i
    print(f"{numero}! = {fatorial}")


