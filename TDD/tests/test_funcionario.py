import unittest

from src.funcionario import FuncionarioManager, FuncionarioAlreadyExistsException

class TestFuncionario(unittest.TestCase):
    def setUp(self):
        self._funcionario_manager = FuncionarioManager()

    def test_cria_funcionario_jose(self):
        jose = self._funcionario_manager.cria_funcionario(1, 'José')

        self.assertIn(jose, self._funcionario_manager.funcionarios)
        self.assertEqual(1, jose.id)
        self.assertEqual('José', jose.nome)

    def test_cria_dois_funcionarios_jose_e_joao(self):
        jose = self._funcionario_manager.cria_funcionario(1, 'José')
        joao = self._funcionario_manager.cria_funcionario(2, 'João')

        self.assertIn(jose, self._funcionario_manager.funcionarios)
        self.assertEqual(1, jose.id)
        self.assertEqual('José', jose.nome)

        self.assertIn(joao, self._funcionario_manager.funcionarios)
        self.assertEqual(2, joao.id)
        self.assertEqual('João', joao.nome)

    def test_tenta_criar_funcionario_jose_duplicado_retorna_erro(self):
        jose = self._funcionario_manager.cria_funcionario(1, 'José')

        self.assertIn(jose, self._funcionario_manager.funcionarios)
        self.assertEqual(1, jose.id)
        self.assertEqual('José', jose.nome)

        with self.assertRaises(FuncionarioAlreadyExistsException):
            jose_duplicado = self._funcionario_manager.cria_funcionario(1, 'José com mesmo ID')

if __name__ == '__main__':
    unittest.main()
