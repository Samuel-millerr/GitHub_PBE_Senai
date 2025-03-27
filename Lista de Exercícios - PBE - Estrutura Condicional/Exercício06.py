#EXERCÍCIO 06 - VERIFICAÇÃO DE NOTA
nota = float(input("Insira a nota do aluno: "))

if nota < 0 or nota > 10:
    print("Nota inválida!")
elif nota <= 2:
    print(f"Nota {nota} se classifica como: 'E'")
elif nota <= 4:
    print(f"Nota {nota} se classifica como: 'D'")
elif nota <= 6:
    print(f"Nota {nota} se classifica como: 'C'")
elif nota <= 8:
    print(f"Nota {nota} se classifica como: 'B'")
elif nota <= 10:
    print(f"Nota {nota} se classifica como: 'A'")