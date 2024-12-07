import unittest

from src.projeto import FuncionarioNotInProjectException, OcorrenciaDuplicadaException

from tests.tests_helper import TestsHelper
from src.ocorrencia import TipoInvalidoException, MaxOcorrenciasFuncException, PrioridadeInvalidaException, OcorrenciaJaFechadaException

class TestOcorrencia(unittest.TestCase):
    def setUp(self):
        self._empresa = TestsHelper().cria_empresa('padaria', 1)
        self._projeto = TestsHelper().cria_projeto(1, 'website', self._empresa)
        self._funcionario = TestsHelper().cria_funcionario(1, 'João')

        self._empresa.inclui_funcionario(self._funcionario)
        self._projeto.inclui_funcionario(self._funcionario)

    def test_cria_1_ocorrencia_prioridade_baixa_e_tarefa(self):
        ocorrencia = self._projeto.cria_ocorrencia(1, 'resumo', 'baixa', 'tarefa', self._funcionario)

        self.assertIn(ocorrencia, self._projeto.ocorrencias)
        self.assertEqual(ocorrencia.responsavel, self._funcionario)
        self.assertEqual('aberta', ocorrencia.estado)
        self.assertEqual('baixa', ocorrencia.prioridade)
        self.assertEqual('tarefa', ocorrencia.tipo)
        self.assertIn(ocorrencia, self._funcionario.ocorrencias)

    def test_cria_1_ocorrencia_prioridade_media_e_tarefa(self):
        ocorrencia = self._projeto.cria_ocorrencia(1, 'resumo', 'media', 'tarefa', self._funcionario)

        self.assertIn(ocorrencia, self._projeto.ocorrencias)
        self.assertEqual(ocorrencia.responsavel, self._funcionario)
        self.assertEqual('aberta', ocorrencia.estado)
        self.assertEqual('media', ocorrencia.prioridade)
        self.assertEqual('tarefa', ocorrencia.tipo)
        self.assertIn(ocorrencia, self._funcionario.ocorrencias)

    def test_cria_1_ocorrencia_prioridade_alta_e_tarefa(self):
        ocorrencia = self._projeto.cria_ocorrencia(1, 'resumo', 'alta', 'tarefa', self._funcionario)

        self.assertIn(ocorrencia, self._projeto.ocorrencias)
        self.assertEqual(ocorrencia.responsavel, self._funcionario)
        self.assertEqual('aberta', ocorrencia.estado)
        self.assertEqual('alta', ocorrencia.prioridade)
        self.assertEqual('tarefa', ocorrencia.tipo)
        self.assertIn(ocorrencia, self._funcionario.ocorrencias)

    def test_cria_1_ocorrencia_prioridade_baixa_e_bug(self):
        ocorrencia = self._projeto.cria_ocorrencia(1, 'resumo', 'baixa', 'bug', self._funcionario)

        self.assertIn(ocorrencia, self._projeto.ocorrencias)
        self.assertEqual(ocorrencia.responsavel, self._funcionario)
        self.assertEqual('aberta', ocorrencia.estado)
        self.assertEqual('baixa', ocorrencia.prioridade)
        self.assertEqual('bug', ocorrencia.tipo)
        self.assertIn(ocorrencia, self._funcionario.ocorrencias)

    def test_cria_1_ocorrencia_prioridade_media_e_bug(self):
        ocorrencia = self._projeto.cria_ocorrencia(1, 'resumo', 'media', 'bug', self._funcionario)

        self.assertIn(ocorrencia, self._projeto.ocorrencias)
        self.assertEqual(ocorrencia.responsavel, self._funcionario)
        self.assertEqual('aberta', ocorrencia.estado)
        self.assertEqual('media', ocorrencia.prioridade)
        self.assertEqual('bug', ocorrencia.tipo)
        self.assertIn(ocorrencia, self._funcionario.ocorrencias)

    def test_cria_1_ocorrencia_prioridade_alta_e_bug(self):
        ocorrencia = self._projeto.cria_ocorrencia(1, 'resumo', 'alta', 'bug', self._funcionario)

        self.assertIn(ocorrencia, self._projeto.ocorrencias)
        self.assertEqual(ocorrencia.responsavel, self._funcionario)
        self.assertEqual('aberta', ocorrencia.estado)
        self.assertEqual('alta', ocorrencia.prioridade)
        self.assertEqual('bug', ocorrencia.tipo)
        self.assertIn(ocorrencia, self._funcionario.ocorrencias)

    def test_cria_1_ocorrencia_prioridade_baixa_e_melhoria(self):
        ocorrencia = self._projeto.cria_ocorrencia(1, 'resumo', 'baixa', 'melhoria', self._funcionario)

        self.assertIn(ocorrencia, self._projeto.ocorrencias)
        self.assertEqual(ocorrencia.responsavel, self._funcionario)
        self.assertEqual('aberta', ocorrencia.estado)
        self.assertEqual('baixa', ocorrencia.prioridade)
        self.assertEqual('melhoria', ocorrencia.tipo)
        self.assertIn(ocorrencia, self._funcionario.ocorrencias)

    def test_cria_1_ocorrencia_prioridade_media_e_melhoria(self):
        ocorrencia = self._projeto.cria_ocorrencia(1, 'resumo', 'media', 'melhoria', self._funcionario)

        self.assertIn(ocorrencia, self._projeto.ocorrencias)
        self.assertEqual(ocorrencia.responsavel, self._funcionario)
        self.assertEqual('aberta', ocorrencia.estado)
        self.assertEqual('media', ocorrencia.prioridade)
        self.assertEqual('melhoria', ocorrencia.tipo)
        self.assertIn(ocorrencia, self._funcionario.ocorrencias)

    def test_cria_1_ocorrencia_prioridade_alta_e_melhoria(self):
        ocorrencia = self._projeto.cria_ocorrencia(1, 'resumo', 'alta', 'melhoria', self._funcionario)

        self.assertIn(ocorrencia, self._projeto.ocorrencias)
        self.assertEqual(ocorrencia.responsavel, self._funcionario)
        self.assertEqual('aberta', ocorrencia.estado)
        self.assertEqual('alta', ocorrencia.prioridade)
        self.assertEqual('melhoria', ocorrencia.tipo)
        self.assertIn(ocorrencia, self._funcionario.ocorrencias)

    def test_cria_1_ocorrencia_duplicada_lanca_excecao(self):
        self._projeto.cria_ocorrencia(1, 'resumo', 'alta', 'melhoria', self._funcionario)

        with self.assertRaises(OcorrenciaDuplicadaException):
            self._projeto.cria_ocorrencia(1, 'resumo', 'alta', 'melhoria', self._funcionario)

    def test_cria_1_ocorrencia_com_tipo_invalido_lanca_excecao(self):
        with self.assertRaises(TipoInvalidoException):
            self._projeto.cria_ocorrencia(1, 'resumo', 'alta', 'outro', self._funcionario)

    def test_cria_1_ocorrencia_com_prioridade_invalida_lanca_excecao(self):
        with self.assertRaises(PrioridadeInvalidaException):
            self._projeto.cria_ocorrencia(1, 'resumo', 'outra', 'melhoria', self._funcionario)

    def test_cria_1_ocorrencia_em_funcionario_com_10_ocorrencias_lanca_excecao(self):
        for i in range(10):
            self._projeto.cria_ocorrencia(i, 'resumo', 'alta', 'melhoria', self._funcionario)

        with self.assertRaises(MaxOcorrenciasFuncException):
            self._projeto.cria_ocorrencia(11, 'resumo', 'alta', 'melhoria', self._funcionario)

    def test_cria_ocorrencia_com_responsavel_que_nao_esta_no_projeto_lanca_excecao(self):
        joao = TestsHelper().cria_funcionario(2, 'João')

        with self.assertRaises(FuncionarioNotInProjectException):
            self._projeto.cria_ocorrencia(1, 'resumo', 'alta', 'melhoria', joao)

    def test_modificacao_de_responsavel_para_ocorrencia(self):
        joao = TestsHelper().cria_funcionario(2, 'João')
        self._empresa.inclui_funcionario(joao)
        self._projeto.inclui_funcionario(joao)

        ocorrencia = self._projeto.cria_ocorrencia(1, 'resumo', 'alta', 'melhoria', self._funcionario)
        
        self._projeto.modifica_responsavel(ocorrencia, joao)

        self.assertNotIn(ocorrencia, self._funcionario.ocorrencias)
        self.assertIn(ocorrencia, joao.ocorrencias)

    def test_modificacao_de_responsavel_para_responsavel_com_10_ocorrencias_lanca_excecao(self):
        joao = TestsHelper().cria_funcionario(2, 'João')
        self._empresa.inclui_funcionario(joao)
        self._projeto.inclui_funcionario(joao)

        for i in range(10):
            self._projeto.cria_ocorrencia(i, 'resumo', 'alta', 'melhoria', joao)

        ocorrencia = self._projeto.cria_ocorrencia(11, 'resumo', 'alta', 'melhoria', self._funcionario)

        with self.assertRaises(MaxOcorrenciasFuncException):
            self._projeto.modifica_responsavel(ocorrencia, joao)

    def test_modificacao_de_responsavel_para_ocorrencia_com_funcionario_que_nao_esta_no_projeto_lanca_excecao(self):
        joao = TestsHelper().cria_funcionario(2, 'João')

        ocorrencia = self._projeto.cria_ocorrencia(1, 'resumo', 'alta', 'melhoria', self._funcionario)

        with self.assertRaises(FuncionarioNotInProjectException):
            self._projeto.modifica_responsavel(ocorrencia, joao)

    def test_modifica_prioridade_da_ocorrencia(self):
        ocorrencia = self._projeto.cria_ocorrencia(1, 'resumo', 'alta', 'melhoria', self._funcionario)

        ocorrencia.prioridade = 'baixa'

        self.assertEqual('baixa', ocorrencia.prioridade)

    def test_modifica_prioridade_da_ocorrencia_para_prioridade_invalida_lanca_excecao(self):
        ocorrencia = self._projeto.cria_ocorrencia(1, 'resumo', 'alta', 'melhoria', self._funcionario)

        with self.assertRaises(PrioridadeInvalidaException):
            ocorrencia.prioridade = 'outra'

    def test_fechar_ocorrencia(self):
        ocorrencia = self._projeto.cria_ocorrencia(1, 'resumo', 'alta', 'melhoria', self._funcionario)

        ocorrencia.fechar_ocorrencia()

        self.assertEqual('fechada', ocorrencia.estado)
        self.assertNotIn(ocorrencia, self._funcionario.ocorrencias)

    def test_alterar_prioridade_de_ocorrencia_fechada_lanca_excecao(self):
        ocorrencia = self._projeto.cria_ocorrencia(1, 'resumo', 'alta', 'melhoria', self._funcionario)

        ocorrencia.fechar_ocorrencia()

        with self.assertRaises(OcorrenciaJaFechadaException):
            ocorrencia.prioridade = 'baixa'

    def test_alterar_responsavel_de_ocorrencia_fechada_lanca_excecao(self):
        joao = TestsHelper().cria_funcionario(2, 'João')
        self._empresa.inclui_funcionario(joao)
        self._projeto.inclui_funcionario(joao)

        ocorrencia = self._projeto.cria_ocorrencia(1, 'resumo', 'alta', 'melhoria', self._funcionario)

        ocorrencia.fechar_ocorrencia()

        with self.assertRaises(OcorrenciaJaFechadaException):
            self._projeto.modifica_responsavel(ocorrencia, joao)

if __name__ == '__main__':
    unittest.main()
