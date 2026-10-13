"""Testes da medição da fase 3 (normalização, coringa e WER).

Execução, a partir da raiz do repositório:  python -m pytest -q tests
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'src'))

from medicao import CORINGA, alinhar, contar, limpar, preparar_maquina, preparar_referencia


def medir(ref, hip):
    return contar(*alinhar(ref, hip))


def test_substituicao_de_acento_conta_como_erro():
    r = medir(limpar('O samba é bom.'), limpar('o samba e bom'))
    assert (r['N'], r['S'], r['D'], r['I']) == (4, 1, 0, 0)
    assert r['WER'] == 0.25


def test_coringa_aceita_qualquer_palavra():
    r = medir(['o', CORINGA, 'é', 'bom'], limpar('o samba é bom'))
    assert r['N'] == 3
    assert r['WER'] == 0


def test_coringa_aceita_ausencia_de_palavra():
    r = medir(['o', CORINGA, 'é', 'bom'], limpar('o é bom'))
    assert r['N'] == 3
    assert r['WER'] == 0


def test_insercao_entra_no_numerador():
    r = medir(limpar('o samba é bom'), limpar('o samba é muito bom'))
    assert (r['S'], r['D'], r['I']) == (0, 0, 1)
    assert r['WER'] == 0.25


def test_interrogacao_de_palavra_perdida_preserva_a_anterior():
    palavras, _ = preparar_referencia('depois do [?] [...] de som.', 4)
    assert palavras == ['depois', 'do', CORINGA, 'de', 'som']


def test_interrogacao_de_duvida_retira_a_palavra_duvidosa():
    palavras, _ = preparar_referencia('explorando a alcocies[?]. Agir a polícia', 3)
    assert palavras == ['explorando', 'a', CORINGA, 'agir', 'a', 'polícia']


def test_marcacoes_de_som_saem_e_de_fala_sao_identificadas():
    palavras, de_fala = preparar_referencia(
        'empregadores. {fala: Torna...}{som: aplausos aparentemente inesperados} Torna-se inadiável', 1)
    assert palavras == ['empregadores', 'torna', 'torna-se', 'inadiável']
    assert de_fala == [False, True, False, False]


def test_pulo_no_meio_da_palavra_e_removido_sem_espaco():
    palavras, _ = preparar_referencia('A prostitu[...]ção, através', 3)
    assert palavras == ['a', 'prostitução', 'através']


def test_encliticos_separados_pelo_whisper_sao_reunidos():
    registro = {'segmentos': [{'words': [
        {'word': ' Torna', 'start': 0.0, 'end': 0.3},
        {'word': '-se', 'start': 0.3, 'end': 0.5},
        {'word': ' inadiável.', 'start': 0.5, 'end': 1.0},
    ]}]}
    palavras, tempos = preparar_maquina(registro)
    assert palavras == ['torna-se', 'inadiável']
    assert tempos == [(0.0, 0.5), (0.5, 1.0)]
