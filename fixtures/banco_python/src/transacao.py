from abc import ABC
from src.dinheiro import Dinheiro, ValorMonetario

class Transacao(ABC):

    def obter_valor_monetario(self):
        pass

    def contabilizar(self, saldo : ValorMonetario):
        pass


class TransacaoNaoRealizada(Transacao):

    def __init__(self, transacao : Transacao):
        self.__transacao = transacao

    def obter_valor_monetario(self):
        return self.__transacao.obter_valor_monetario()

    def contabilizar(self, saldo: ValorMonetario):
        return saldo



class Entrada(Transacao):

    def __init__(self, quantia : Dinheiro):
        self.__quantia = quantia

    def obter_valor_monetario(self):
        return self.__quantia.positivo()

    def contabilizar(self, saldo : ValorMonetario):
        return saldo.somar(self.__quantia)



class Saida(Transacao):

    def __init__(self, quantia : Dinheiro):
        self.__quantia = quantia

    def obter_valor_monetario(self):
        return self.__quantia.negativo()

    def contabilizar(self, saldo: ValorMonetario):
        return saldo.subtrair(self.__quantia)
