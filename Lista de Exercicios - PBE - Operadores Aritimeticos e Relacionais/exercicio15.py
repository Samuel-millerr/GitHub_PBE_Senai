#EXERCICIO 15 - MÉDIA DE NOTAS
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))

print(f"As notas com seus respectivos pesos são: \n{nota1:.1f} com o peso de 2 \n{nota2:.1f} com peso de 3 \n"
      f"{nota3:.2} com peso de 5 \nA média das notas é {(nota1*2 + nota2*3 + nota3*5)/(2+3+5):.2f}")


