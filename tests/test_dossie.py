"""Testes das chamadas e das medidas da fase 5 (marcação temporal, fonte, grau de apoio, restrição).

Execução, a partir da raiz do repositório:  python -m pytest -q tests
"""
import json
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / 'src'))

from dossie import (ESQUEMA, GRAUS, INSTRUCAO, MOTIVOS, alcancado, dossie_md, estaveis, grau_esperado,
                    invencao, mapa_fontes, monta_pedido, problemas_conformidade, termos_na_frase)

ENTRADA = {
    'faixa': 9, 'duracao_s': 60.0, 'legenda': {}, 'resumo_panns': '',
    'fala': [{'id': 'F-001', 'inicio': 10.0, 'fim': 14.0, 'texto': 'teste', 'sinais': ['repetição']},
             {'id': 'F-002', 'inicio': 40.0, 'fim': 42.0, 'texto': 'outro', 'sinais': []}],
    'eventos_panns': [{'id': 'P-001', 'inicio': 11.0, 'fim': 13.0, 'rotulo': 'Applause', 'probabilidade_maxima': 0.4},
                      {'id': 'P-002', 'inicio': 30.0, 'fim': 32.0, 'rotulo': 'Owl', 'probabilidade_maxima': 0.6}],
    'descricoes_clap': [{'id': 'C-001', 'inicio': 50.0, 'fim': 52.0, 'descricao': 'wind'}],
}
FONTES = mapa_fontes(ENTRADA)


def ind(inicio, fim, fontes, motivo='evento sonoro apontado', grau='médio', frase='Verificar o trecho.'):
    return {'inicio': inicio, 'fim': fim, 'fontes': fontes, 'motivo': motivo, 'grau_de_apoio': grau, 'frase': frase}


def test_instrucao_e_o_texto_do_anexo_a():
    desenho = (RAIZ / 'docs' / 'fase5' / '01_desenho_experimental.md').read_text(encoding='utf-8')
    anexo = desenho.split('## Anexo A', 1)[1].split('\n', 1)[1].strip()
    assert INSTRUCAO == anexo


def test_esquema_limita_motivos_e_graus():
    props = ESQUEMA['properties']['indicacoes']['items']['properties']
    assert props['motivo']['enum'] == MOTIVOS and props['grau_de_apoio']['enum'] == GRAUS


def test_pedido_traz_regras_e_entrada_sem_titulo():
    pedido = monta_pedido(ENTRADA)
    assert all(m in pedido for m in MOTIVOS) and 'Entrada da faixa 9' in pedido
    assert json.loads(pedido.split('Entrada da faixa 9:\n', 1)[1]) == ENTRADA


def test_conformidade():
    assert problemas_conformidade(ind(10, 14, ['F-001'])) == []
    assert problemas_conformidade(ind(14, 10, [], motivo='ironia', grau='certo', frase=' ')) == [
        'início depois do fim', 'sem fonte', 'motivo fora da lista', 'grau fora da lista', 'sem frase']
    assert 'tempo ausente ou não numérico' in problemas_conformidade({**ind(1, 2, ['F-001']), 'inicio': '1'})


def test_invencao_identificador_e_tempo_com_tolerancia():
    assert invencao(ind(10, 14, ['F-001', 'P-099']), FONTES) == (['P-099'], False)
    assert invencao(ind(9.0, 15.0, ['F-001']), FONTES) == ([], False)   # dentro da tolerância de 1 s
    assert invencao(ind(8.9, 14, ['F-001']), FONTES) == ([], True)
    assert invencao(ind(10, 32, ['F-001', 'P-002']), FONTES) == ([], False)  # entre o menor início e o maior fim


def test_termos_interpretativos_por_inicio_de_palavra():
    assert termos_na_frase('Um tom irônico e certa tristeza; isso sugere que...') == ['irônico', 'triste' + 'za', 'sugere que']
    assert termos_na_frase('O detector registrou 0,60 para o rótulo Owl.') == []
    assert termos_na_frase('O texto representa') == ['representa']


def test_grau_esperado_segue_a_regra():
    assert grau_esperado(ind(10, 14, ['F-001', 'P-001']), FONTES) == 'alto'   # fontes diferentes coincidem
    assert grau_esperado(ind(30, 32, ['P-002']), FONTES) == 'alto'            # PANNs >= 0,5
    assert grau_esperado(ind(11, 13, ['P-001']), FONTES) == 'médio'
    assert grau_esperado(ind(10, 14, ['F-001']), FONTES) == 'médio'           # fala com sinal
    assert grau_esperado(ind(50, 52, ['C-001']), FONTES) == 'baixo'
    assert grau_esperado(ind(40, 42, ['F-002']), FONTES) is None             # fala sem sinal: não previsto
    assert grau_esperado(ind(10, 52, ['F-001', 'C-001']), FONTES) is None    # fontes diferentes sem coincidência
    assert grau_esperado(ind(10, 14, ['F-009']), FONTES) is None             # identificador inexistente


def test_estabilidade_exige_mesmo_motivo_e_sobreposicao():
    r1 = [ind(10, 14, ['F-001'], motivo='repetição na transcrição'), ind(30, 32, ['P-002'])]
    r2 = [ind(12, 16, ['F-001'], motivo='repetição na transcrição'), ind(30, 32, ['P-002'], motivo='rótulo isolado')]
    r3 = [ind(13, 13.5, ['F-001'], motivo='repetição na transcrição'), ind(31, 32, ['P-002'])]
    assert estaveis([r1, r2, r3]) == [[True, False], [True, False], [True, False]]


def test_cobertura_por_sobreposicao():
    assert alcancado({'inicio': 13, 'fim': 20}, [ind(10, 14, ['F-001'])])
    assert not alcancado({'inicio': 15, 'fim': 20}, [ind(10, 14, ['F-001'])])


def test_dossie_em_ordem_de_tempo_com_marca_de_estabilidade():
    texto = dossie_md(ENTRADA, [ind(30, 32, ['P-002']), ind(10, 14, ['F-001'])], [False, True], 'Cabeçalho')
    assert texto.index('0:10,0 a 0:14,0 · repete-se nas três chamadas') < texto.index('0:30,0 a 0:32,0')
    assert dossie_md(ENTRADA, [], [], 'x').count('nenhuma indicação') == 1
