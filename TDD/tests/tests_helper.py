from src.empresa import EmpresaManager
from src.funcionario import FuncionarioManager

class TestsHelper:
    def cria_funcionario(self, id, nome):
        funcionario = FuncionarioManager().cria_funcionario(id, nome)
        
        return funcionario

    def cria_empresa(self, nome, id):
        return EmpresaManager().create_empresa(nome, id)

    def cria_projeto(self, id, nome, empresa):
        return empresa.cria_projeto(nome, id)
