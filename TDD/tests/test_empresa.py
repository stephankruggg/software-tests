import unittest
from src.empresa import Empresa, EmpresaManager, EmpresaDuplicadaException, FuncionarioJaIncluidoException

from tests.tests_helper import TestsHelper


class TestEmpresa(unittest.TestCase):
    def test_cria_empresa(self):
        nome = "Enterprise"
        empresa = Empresa(nome, 0)
        assert empresa.nome == nome
        assert empresa.id == 0
        
    def test_cria_2_empresas(self):
        manager = EmpresaManager()
        empresa1 = manager.create_empresa("Empresa1", 0)
        empresa2 = manager.create_empresa("Empresa2", 1)
        assert empresa1.nome == "Empresa1"
        assert empresa1.id == 0
        assert empresa2.nome == "Empresa2"
        assert empresa2.id == 1
    
    def test_cria_empresa_duplicada(self):
        manager = EmpresaManager()
        padaria1 = manager.create_empresa("Padaria1", 0)

        with self.assertRaises(EmpresaDuplicadaException):
            padaria2 = manager.create_empresa("Padaria2", 0)

    def test_inclui_jose_em_padaria(self):
        jose = TestsHelper().cria_funcionario(1, 'José')

        manager = EmpresaManager()
        padaria = manager.create_empresa('Padaria1', 0)

        padaria.inclui_funcionario(jose)

        self.assertIn(jose, padaria.funcionarios)

    def test_inclui_jose_e_joao_em_padaria(self):
        jose = TestsHelper().cria_funcionario(1, 'José')
        joao = TestsHelper().cria_funcionario(2, 'João')

        manager = EmpresaManager()
        padaria = manager.create_empresa('Padaria1', 0)

        padaria.inclui_funcionario(jose)
        padaria.inclui_funcionario(joao)

        self.assertIn(jose, padaria.funcionarios)
        self.assertIn(joao, padaria.funcionarios)

    def test_tenta_incluir_jose_2_vezes_retorna_erro(self):
        jose = TestsHelper().cria_funcionario(1, 'José')

        manager = EmpresaManager()
        padaria = manager.create_empresa('Padaria1', 0)

        padaria.inclui_funcionario(jose)
        self.assertIn(jose, padaria.funcionarios)

        with self.assertRaises(FuncionarioJaIncluidoException):
            padaria.inclui_funcionario(jose)

    def test_inclui_jose_em_padaria_e_borracharia(self):
        jose = TestsHelper().cria_funcionario(1, 'José')

        manager = EmpresaManager()
        padaria = manager.create_empresa('Padaria1', 0)
        borracharia = manager.create_empresa('Borracharia1', 1)

        padaria.inclui_funcionario(jose)
        borracharia.inclui_funcionario(jose)

        self.assertIn(jose, padaria.funcionarios)
        self.assertIn(jose, borracharia.funcionarios)

if __name__ == "__main__":
    unittest.main()