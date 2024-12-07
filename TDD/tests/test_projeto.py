import unittest
from src.empresa import EmpresaManager, ProjetoDuplicadoException
from src.projeto import FuncionarioDuplicadoException, FuncionarioNotInEmpresaException
from tests.tests_helper import TestsHelper

class TestProjeto(unittest.TestCase):
    def test_cria_1_projeto(self):
        manager = EmpresaManager()
        padaria = manager.create_empresa("Padaria", 0)
        padaria.cria_projeto("Pão", 0)

        assert len(padaria.projetos) == 1
        assert padaria.projetos[0].nome == "Pão"
    
    def test_cria_2_projetos(self):
        manager = EmpresaManager()
        padaria = manager.create_empresa("Padaria", 0)
        padaria.cria_projeto("Pão", 0)
        padaria.cria_projeto("Almoço", 1)

        assert len(padaria.projetos) == 2
        assert padaria.projetos[0].nome == "Pão"
        assert padaria.projetos[1].nome == "Almoço"
    
    def test_cria_2_projetos_iguais(self):
        manager = EmpresaManager()
        padaria = manager.create_empresa("Padaria", 0)
        padaria.cria_projeto("Pão", 0)
        with self.assertRaises(ProjetoDuplicadoException):
            padaria.cria_projeto("Pão", 0)
    
    def test_incluir_1_funcionario(self):
        empresa = TestsHelper().cria_empresa("padaria", 0)
        jose = TestsHelper().cria_funcionario(1, "jose")
        empresa.inclui_funcionario(jose)
        projeto = empresa.cria_projeto("Pão", 1)

        projeto.inclui_funcionario(jose)

        self.assertIn(jose, projeto.funcionarios)
    
    def test_incluir_2_funcionarios(self):
        empresa = TestsHelper().cria_empresa("padaria", 0)
        jose = TestsHelper().cria_funcionario(1, "jose")
        joao = TestsHelper().cria_funcionario(2, "joao")
        empresa.inclui_funcionario(jose)
        projeto = empresa.cria_projeto("Pão", 1)

        projeto.inclui_funcionario(jose)
        projeto.inclui_funcionario(joao)

        self.assertIn(jose, projeto.funcionarios)
        self.assertIn(joao, projeto.funcionarios)
    
    def test_incluir_1_funcionario_2_projetos(self):
        empresa = TestsHelper().cria_empresa("padaria", 0)
        jose = TestsHelper().cria_funcionario(1, "jose")
        empresa.inclui_funcionario(jose)
        projeto1 = empresa.cria_projeto("Pão", 1)
        projeto2 = empresa.cria_projeto("bebida", 2)

        projeto1.inclui_funcionario(jose)
        projeto2.inclui_funcionario(jose)

        self.assertIn(jose, projeto1.funcionarios)
        self.assertIn(jose, projeto2.funcionarios)
    
    def test_incluir_2_funcionarios(self):
        empresa = TestsHelper().cria_empresa("padaria", 0)
        jose = TestsHelper().cria_funcionario(1, "jose")
        empresa.inclui_funcionario(jose)
        projeto = empresa.cria_projeto("Pão", 1)

        projeto.inclui_funcionario(jose)

        with self.assertRaises(FuncionarioDuplicadoException):
            projeto.inclui_funcionario(jose)
    
    def test_inclui_func_outra_empresa(self):
        padaria = TestsHelper().cria_empresa("padaria", 0)
        joao = TestsHelper().cria_funcionario(1, 'joao')
        padaria.inclui_funcionario(joao)
        borracharia = TestsHelper().cria_empresa("Borracharia", 2)
        pneu = borracharia.cria_projeto("pneu", 1)

        with self.assertRaises(FuncionarioNotInEmpresaException):
            pneu.inclui_funcionario(joao)
    
if __name__=="__main__":
    unittest.main()