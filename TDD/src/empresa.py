from src.funcionario import Funcionario
from src.projeto import Projeto


class EmpresaDuplicadaException(Exception):
    def __init__(self):
        self.message = "Empresa com mesmo código já existe"
        super().__init__(self.message)

class FuncionarioJaIncluidoException(Exception):
    def __init__(self):
        self.message = 'Empresa já possui esse funcionário'
        super().__init__(self.message)

class ProjetoDuplicadoException(Exception):
    def __init__(self):
        self.message = 'Projeto ja existente'
        super().__init__(self.message)

class Empresa():
    def __init__(self, nome:str, id) -> None:
        self.__nome = nome
        self.__id = id
        self.__projetos = []
        self.__funcionarios = []

    @property
    def id(self):
        return self.__id
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def funcionarios(self):
        return self.__funcionarios

    def inclui_funcionario(self, funcionario: Funcionario):
        if funcionario in self.__funcionarios:
            raise FuncionarioJaIncluidoException()

        self.__funcionarios.append(funcionario)
        funcionario.empresas = self
    
    @property
    def projetos(self):
        return self.__projetos
    
    def cria_projeto(self, nome, id):
        projetos = [p.id for p in self.projetos]
        if id in projetos:
            raise ProjetoDuplicadoException()
        proj = Projeto(nome, id, self)
        self.__projetos.append(proj)
        return proj


class EmpresaManager():
    def __init__(self) -> None:
        self.__ids = []

    def ids(self) -> list:
        return self.__ids

    def create_empresa(self, nome:str, id:int) -> Empresa:
        if id in self.ids():
            raise EmpresaDuplicadaException()
        self.ids().append(id)
        return Empresa(nome, id)
