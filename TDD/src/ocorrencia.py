class TipoInvalidoException(Exception):
    def __init__(self):
        self.message = "Tipo de ocorrência Inválido"
        super().__init__(self.message)

class PrioridadeInvalidaException(Exception):
    def __init__(self):
        self.message = "Prioridade inválida"
        super().__init__(self.message)

class MaxOcorrenciasFuncException(Exception):
    def __init__(self):
        self.message = "Funcinário já tem 10 ocorrências"
        super().__init__(self.message)

class OcorrenciaJaFechadaException(Exception):
    def __init__(self):
        self.message = "Ocorrência já fechada"
        super().__init__(self.message)

class Ocorrencia:
    _possiveis_tipos = ['tarefa', 'bug', 'melhoria']
    _possiveis_prioridades = ['baixa', 'media', 'alta']

    def __init__(self, id, resumo, tipo, prioridade, responsavel):
        if tipo not in self._possiveis_tipos:
            raise TipoInvalidoException()

        if prioridade not in self._possiveis_prioridades:
            raise PrioridadeInvalidaException()

        if len(responsavel.ocorrencias) >= 10:
            raise MaxOcorrenciasFuncException()

        self._id = id
        self._resumo = resumo
        self._tipo = tipo
        self._estado = 'aberta'
        self._prioridade = prioridade
        self._responsavel = responsavel

    @property
    def id(self):
        return self._id

    @property
    def estado(self):
        return self._estado

    @property
    def tipo(self):
        return self._tipo

    @property
    def prioridade(self):
        return self._prioridade

    @prioridade.setter
    def prioridade(self, nova_prioridade):
        if self._estado != 'aberta':
            raise OcorrenciaJaFechadaException()

        if nova_prioridade not in self._possiveis_prioridades:
            raise PrioridadeInvalidaException()

        self._prioridade = nova_prioridade

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, novo_responsavel):
        self._responsavel = novo_responsavel

    def fechar_ocorrencia(self):
        self._responsavel.remove_ocorrencia(self)
        self._estado = 'fechada'
