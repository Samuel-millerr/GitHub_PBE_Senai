#EXERCÍCIO 15 - VALIDAÇÃO DE SENHA
import re

print("Critérios para criação de uma nova senha:")
print("• Pelo menos 8 caracteres.")
print("• Pelo menos uma letra maiúscula.")
print("• Pelo menos uma letra minúscula.")
print("• Pelo menos um número.")
print("• Pelo menos um caractere especial (@, #, $, %, &).")

senha = input("\nDigite a senha: ")
criterios = []

if len(senha) < 8:
    criterio_quant_caracter = bool(0)
    criterios.append("A senha não tem 8 ou mais caracteres.")
else:
    criterio_quant_caracter = bool(1)

if re.search(r"[a-z]", senha):
    criterio_minusculas = bool(1)
else:
    criterio_minusculas = bool(0)
    criterios.append("A senha não possui letras minusculas")

if re.search(r"[A-Z]", senha):
    criterio_maiusculas = bool(1)
else:
    criterio_maiusculas = bool(0)
    criterios.append("A senha não possui letras maiúsculas.")

if re.search(r"\d", senha):
    criterio_numero = bool(1)
else:
    criterio_numero = bool(0)
    criterios.append("A senha não possui nenhum número.")

if re.search("[@#$%&]", senha):
    criterio_especial = bool(1)
else:
    criterio_especial = bool(0)
    criterios.append("A senha não possui nenhum caractere especial.")

if len(criterios) == 0:
    print("Senha Válida! A senha segue todos os critérios estabelecidos.")
else:
    print("Senha Inválida! Os critérios abaixo não foram seguidos.")
    for criterio in criterios:
        print(criterio)