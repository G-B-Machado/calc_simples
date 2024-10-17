from . import operacoes

class Calculadora:
    def adicionar(self, a, b):
        return operacoes.adicionar(a, b)

    def subtrair(self, a, b):
        return operacoes.subtrair(a, b)

    def multiplicar(self, a, b):
        return operacoes.multiplicar(a, b)

    def dividir(self, a, b):
        return operacoes.dividir(a, b)