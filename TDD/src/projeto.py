from src.funcionario import Funcionario
from src.ocorrencia import Ocorrencia, OcorrenciaJaFechadaException, MaxOcorrenciasFuncException


class FuncionarioDuplicadoException(Exception):
    def __init__(self) -> None:
        msg = 'Funcionário duplicado'
        super().__init__(msg)

class FuncionarioNotInEmpresaException(Exception):
    def __init__(self) -> None:
        msg = 'Funcionário não pertence a mesma empresa que o projeto'
        super().__init__(msg)

class FuncionarioNotInProjectException(Exception):
    def __init__(self) -> None:
        msg = 'Funcionário não associado ao projeto'
        super().__init__(msg)

class OcorrenciaDuplicadaException(Exception):
    def __init__(self) -> None:
        msg = 'Ocorrência duplicada'
        super().__init__(msg)

class Projeto():
    def __init__(self, nome, id, empresa) -> None:
        self.__nome = nome
        self.__id = id
        self.__funcionarios = []
        self._ocorrencias = []
        self.__empresa = empresa
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def funcionarios(self) -> list:
        return self.__funcionarios

    @property
    def ocorrencias(self) -> list:
        return self._ocorrencias

    @property
    def empresa(self):
        return self.__empresa
    
    def inclui_funcionario(self, func:Funcionario):
        if func in self.funcionarios:
            raise FuncionarioDuplicadoException()
        if self.empresa not in func.empresas:
            raise FuncionarioNotInEmpresaException()
        self.__funcionarios.append(func)

    def cria_ocorrencia(self, id, resumo, prioridade, tipo, func: Funcionario):
        for o in self._ocorrencias:
            if id == o.id:
                raise OcorrenciaDuplicadaException()

        if func not in self.__funcionarios:
            raise FuncionarioNotInProjectException()

        ocorrencia = Ocorrencia(id, resumo, tipo, prioridade, func)
        self._ocorrencias.append(ocorrencia)
        func.ocorrencias = ocorrencia

        return ocorrencia

    def modifica_responsavel(self, ocorrencia, funcionario):
        if funcionario not in self.__funcionarios:
            raise FuncionarioNotInProjectException()

        if ocorrencia.estado != 'aberta':
            raise OcorrenciaJaFechadaException()

        if len(funcionario.ocorrencias) >= 10:
            raise MaxOcorrenciasFuncException()

        funcionario_atual = ocorrencia.responsavel

        funcionario_atual.remove_ocorrencia(ocorrencia)

        ocorrencia.responsavel = funcionario
        funcionario.ocorrencias = ocorrencia
