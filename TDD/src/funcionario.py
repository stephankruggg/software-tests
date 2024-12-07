class FuncionarioAlreadyExistsException(Exception):
    def __init__(self) -> None:
        msg = 'Funcionário já existente'
        super().__init__(msg)

class FuncionarioManager:
    def __init__(self):
        self._funcionarios = []

    @property
    def funcionarios(self):
        return self._funcionarios

    def cria_funcionario(self, id, nome):
        for f in self._funcionarios:
            if id == f.id:
                raise FuncionarioAlreadyExistsException()

        funcionario = Funcionario(id, nome)
        self._funcionarios.append(funcionario)

        return funcionario

class Funcionario:
    def __init__(self, id, nome):
        self._id = id
        self._nome = nome
        self.__empresas = []
        self._ocorrencias = []

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome
    
    @property
    def empresas(self):
        return self.__empresas

    @empresas.setter
    def empresas(self, nova_empresa):
        self.__empresas.append(nova_empresa)

    @property
    def ocorrencias(self):
        return self._ocorrencias

    @ocorrencias.setter
    def ocorrencias(self, nova_ocorrencia):
        self._ocorrencias.append(nova_ocorrencia)

    def remove_ocorrencia(self, ocorrencia):
        self._ocorrencias.remove(ocorrencia)
