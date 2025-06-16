class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

carro_01 = Carro("Toyota", "Corolla")
carro_02 = Carro("Chevrolet", "Classic")
carro_03 = Carro("Fiat", "Mobi")

for carro in (carro_01, carro_02, carro_03):
    carro.exibir_informacoes()

from abc import ABC, abstractmethod
# class Gato:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#
#     def miar(self):
#         print(f"{self.nome} miau!")
#
#
# gato01 = Gato("Roberto", "16 anos")
# print(gato01.nome)
# print(gato01.idade)
#

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#
#     def apresentar(self):
#         print(f"\nOlá!\nMeu nome é {self.nome} e eu tenho {self.idade} anos")
#
#     def __str__(self):
#         return f"{self.nome}"
#
#     def __eq__(self, other): # Confere se é igual
#         if isinstance(other, Pessoa):
#             if self.nome ==  other.nome and self.idade == other.idade:
#                 return True
#         return False
#
#     def __ge__(self, other): # Confere se é maior ou igual
#         return
#     def __gt__(self, other):  # Confere se é maior
#         return
#     def __le__(self, other):  # Confere se é menor ou igual
#         return
#     def __lt__(self, other):  # Confere se é menor
#         return
#
#     def __len__(self):
#         return self.idade
#
#     def to_dict(self):
#         return  {
#             "nome": self.nome,
#             "idade": self.idade
#         }
#
# class Funcionario(Pessoa):
#     def __init__(self, nome, idade, cargo):
#         super().__init__(nome, idade)
#         self.cargo = cargo
#
#     def apresentar(self):
#         print(f"Olá sou o  {self.nome} e eu sou {self.cargo}")
#
# pessoas = []
# for i in range(3):
#     nome = input(f"Digite o nome da {i+1}° pessoa: ").strip()
#     idade = int(input(f"Digite o nome da {i+1}° pessoa: "))
#     if nome == "Samuel":
#         cargo = "Aprendiz"
#         pessoas.append(Funcionario(nome, idade, cargo))
#     pessoas.append(Pessoa(nome, idade))
#
# for pessoa in pessoas:
#     pessoa.apresentar()

# class ContaBancaria:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.__saldo = saldo
#
#     @property
#     def saldo(self):
#         return self.__saldo
#
#     @saldo.setter
#     def saldo(self, valor):
#         if valor < 0:
#             raise ValueError("Saldo não pode ser negativo!")
#         self.__saldo = valor

# def get_saldo(self):
    #     return self.__saldo
    #
    # def set_saldo(self, valor):
    #     if valor < 0:
    #         raise ValueError("Saldo não pode ser negativo!")
    #     self.__saldo = valor

# conta01 = ContaBancaria("Samuel", -878)
# conta01.saldo = -900
# print(conta01.saldo)

class Pagamento(ABC):

    @abstractmethod
    def autorizar(self, valor):
        pass

    @abstractmethod
    def estornar(self, valor):
        pass

class Pix(Pagamento):
    def autorizar(self, valor):
        print(f"Transferindo R$ {valor} via pix!")

    def estornar(self, valor):
        print(f"Estornando R$ {valor} via pix!")

Pix().autorizar(200)
Pix().estornar(290)