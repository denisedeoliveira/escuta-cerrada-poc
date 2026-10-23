"""Testes da comparação da fase 4 (leitura da referência, nomeação, escuta dirigida).

Execução, a partir da raiz do repositório:  python -m pytest -q tests
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'src'))

from eventos import (CLAP_CLASSES, PANNS_CLASSES, agrupar, candidatos_clap, candidatos_panns,
                     ler_referencia, mapa_inverso, nomeacao_clap, nomeacao_panns, posicoes,
                     rotulos_musica, segundos, sobrepoe)

TABELA = """
| 1.5  | 2:18,2 | 2:26,7 | aplauso e grito de plateia | aplausos | REF | registrado |
| 5.5  | 1:52   | 2:49   | fala, música e vento       | vozes    | EC  | registrado |
| Fonte | não é linha de evento |
"""


def janela_panns(inicio, **rotulos):
    return {'inicio': inicio, 'fim': inicio + 2, 'rotulos': rotulos}


def janela_clap(inicio, ordem):
    """Semelhanças decrescentes na ordem dada; os demais termos ficam abaixo."""
    termos = list(ordem) + [t for ts in CLAP_CLASSES.values() for t in ts if t not in ordem]
    return {'inicio': inicio, 'fim': inicio + 2,
            'semelhancas': {t: 1 - k / 100 for k, t in enumerate(dict.fromkeys(termos))}}


def test_tempos_com_virgula_decimal():
    assert segundos('4:17,15') == 257.15
    assert segundos('0:00') == 0


def test_classes_compostas_sao_desdobradas():
    ev = ler_referencia(TABELA)
    assert [e['id'] for e in ev] == ['1.5', '5.5']
    assert ev[0]['componentes'] == ['aplauso', 'grito de plateia']
    assert ev[1]['componentes'] == ['fala', 'música', 'vento']
    assert ev[0]['inicio'] == 138.2 and ev[0]['fim'] == 146.7


def test_sobreposicao_exige_tempo_em_comum():
    j = {'inicio': 10, 'fim': 12}
    assert sobrepoe(j, 11.5, 13)
    assert not sobrepoe(j, 12, 14)   # só encostam


def test_limiares_do_panns():
    janelas = [janela_panns(0, Applause=0.29), janela_panns(1, Clapping=0.31)]
    assert nomeacao_panns('aplauso', janelas, PANNS_CLASSES)[:3] == ('nomeado', 'Clapping', 0.31)
    assert nomeacao_panns('aplauso', janelas[:1], PANNS_CLASSES)[0] == 'indício'
    assert nomeacao_panns('aplauso', [janela_panns(0, Applause=0.05)], PANNS_CLASSES)[0] == 'não nomeado'
    assert nomeacao_panns('pausa', janelas, PANNS_CLASSES)[0] == 'sem correspondência'


def test_clap_nomeia_ate_a_terceira_posicao():
    j3 = janela_clap(0, ['music', 'wind', 'applause'])
    j4 = janela_clap(0, ['music', 'wind', 'silence', 'applause'])
    assert posicoes(j3)['applause'] == 3
    assert nomeacao_clap('aplauso', [j3], CLAP_CLASSES)[:3] == ('nomeado', 'applause', 3)
    assert nomeacao_clap('aplauso', [j4], CLAP_CLASSES)[:3] == ('não nomeado', 'applause', 4)


def test_musica_exclui_percussao_e_rotulos_a_parte():
    nomes = [f'r{i}' for i in range(527)]
    nomes[137], nomes[150], nomes[160] = 'Music', 'Drum', 'Tambourine'
    musica = rotulos_musica(nomes)
    assert 'Music' in musica and 'Drum' not in musica and 'Tambourine' not in musica
    assert len(musica) == 146 - 2


def test_criterios_da_escuta_no_panns():
    ev = ler_referencia(TABELA)
    inv = mapa_inverso(PANNS_CLASSES)
    janelas = [
        janela_panns(140, Applause=0.8),              # dentro do evento 1.5: não entra
        janela_panns(200, Applause=0.4),              # fora de qualquer aplauso: critério 1
        janela_panns(201, Speech=0.9, Hiss=0.9),      # fala e ruído nas faixas 01 a 03: não entram
        janela_panns(202, Sheep=0.57, Bleat=0.45),    # sem classe: só o que passa de 0,5
    ]
    itens = candidatos_panns(1, 'sem', janelas, inv, ev)
    assert [(x['criterio'], x['rotulo']) for x in itens] == [(1, 'Applause'), (2, 'Sheep')]


def test_clap_exige_primeiro_lugar_nas_duas_condicoes():
    ev = ler_referencia(TABELA)
    inv = mapa_inverso(CLAP_CLASSES)
    sem = [janela_clap(0, ['surdo']), janela_clap(1, ['ocean waves']), janela_clap(130, ['music'])]
    com = [janela_clap(0, ['wind']), janela_clap(1, ['ocean waves']), janela_clap(130, ['music'])]
    itens = candidatos_clap(5, sem, com, inv, ev)
    assert [(x['inicio'], x['criterio'], x['rotulo']) for x in itens] == [(1, 2, 'ocean waves')]


def test_agrupamento_com_folga_de_cinco_segundos():
    itens = [dict(faixa=1, inicio=0, fim=2), dict(faixa=1, inicio=7, fim=9),
             dict(faixa=1, inicio=15, fim=17), dict(faixa=2, inicio=16, fim=18)]
    assert [x['trecho'] for x in agrupar(itens)] == [1, 1, 2, 3]
