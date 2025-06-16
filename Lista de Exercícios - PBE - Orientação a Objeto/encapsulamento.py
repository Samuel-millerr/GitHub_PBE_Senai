""" Encapsulamento é a prática dentro de orientação a objeto serve para a proteção de dados específicos, dados
sensíveis por exemplo. Usado para controlar o acesso em determinados dados do sistema."""

class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo # "__saldo" os underlines no início da função os determinam como um atributo privado

    def depositar(self, valor):
        if not isinstance(valor, int):
            raise TypeError("Saldo deve ser um valor inteiro!")
        elif valor > 0:
            self.__saldo += valor
            print("Valor depositado!")
        else:
            raise ValueError("Valor inviável para um deposito bancário")

    def sacar(self, valor):
        if not isinstance(valor, int):
            raise TypeError("Saldo deve ser um valor inteiro!")
        elif valor > self.__saldo:
            raise ValueError("Não é possível sacar um valor maior doque o do saldo!")
        else:
            self.__saldo -= valor
            print(f"O valor de R${valor}, foi sacado")

    def ver_saldo(self):
        return f"{self.__saldo}"

contaSamuel = ContaBancaria(200)

print(contaSamuel.ver_saldo())
contaSamuel.depositar(15)
contaSamuel.sacar(50)
print(contaSamuel.ver_saldo())