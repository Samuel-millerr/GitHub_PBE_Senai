# EXERCÍCIO 05 - VERIFICADOR DE IDADE

print(f"{"="*5} EXERCÍCIO 05 - CINEMA {"="*5}")
print("Bem vindo!! Para ver o filme é necessário verificar a idade dos clientes. O filme tem classificação de 18 anos.")
print("A princípio temos 3 clientes: ")

clientes = {
    "Lucas": 15,
    "Pedro": 20,
    "Maria": 15
}

print("   Nome    |  Idade   ")
for chave, valor in clientes.items():
    print(f"   {chave}   |   {valor}   ")

print("")
for chave, valor in clientes.items():
    if valor < 18:
        print(f"{chave} não pode entrar no filme!")
    else:
        print(f"{chave} pode entrar no filme!")

