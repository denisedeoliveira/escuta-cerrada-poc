"""Testes da montagem das entradas da fase 5 (sinais da fala, PANNs, CLAP, identificadores).

Execução, a partir da raiz do repositório:  python -m pytest -q tests
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'src'))

from entradas import itens_clap, itens_panns, monta_entrada, normaliza, reune, sinais_fala


def seg(inicio, fim, texto, logprob=-0.2, sem_fala=0.1, compressao=1.0):
    return {'start': inicio, 'end': fim, 'text': texto, 'avg_logprob': logprob,
            'no_speech_prob': sem_fala, 'compression_ratio': compressao}


def pal(inicio, fim, texto):
    return {'word': texto, 'start': inicio, 'end': fim}


def janela_panns(i, **rotulos):
    return {'inicio': i, 'fim': i + 2, 'rotulos': rotulos}


def janela_clap(i, ordem):
    return {'inicio': i, 'fim': i + 2, 'semelhancas': {d: 1 - k / 10 for k, d in enumerate(ordem)}}


def test_normalizacao_ignora_caixa_e_pontuacao():
    assert normaliza(' A CIDADE no Brasil.') == 'a cidade no brasil'


def test_repeticao_exige_tres_segmentos_e_ignora_texto_vazio():
    segs = [seg(0, 1, 'Aplausos.'), seg(2, 3, 'aplausos'), seg(4, 5, ' '), seg(6, 7, ''), seg(8, 9, '')]
    assert ['repetição' in s for s in sinais_fala(segs, [])] == [False] * 5
    segs.append(seg(10, 11, 'APLAUSOS!'))
    assert ['repetição' in s for s in sinais_fala(segs, [])] == [True, True, False, False, False, True]


def test_limiares_de_ausencia_de_fala_e_confianca_sao_estritos():
    segs = [seg(0, 1, '', sem_fala=0.6, logprob=-1.0), seg(1, 2, '', sem_fala=0.61, logprob=-1.01)]
    assert sinais_fala(segs, []) == [[], ['indicação de ausência de fala', 'baixa confiança']]


def test_divergencia_compara_palavras_no_mesmo_intervalo():
    c = [pal(0, 1, ' a'), pal(1, 2, ' lei'), pal(2, 3, ' orgânica'), pal(10, 11, ' reforma')]
    segs = [seg(0, 3, 'A reforma da lei orgânica'), seg(0, 3, 'A reforma do escudário')]
    resultado = sinais_fala(segs, c)
    assert 'divergência entre transcrições' not in resultado[0]   # 3 de 5 palavras
    assert 'divergência entre transcrições' in resultado[1]       # 1 de 4 palavras


def test_reune_apenas_janelas_consecutivas():
    grupos = reune([(3, 3, 5, 0.4), (4, 4, 6, 0.7), (6, 6, 8, 0.3)])
    assert [(g['inicio'], g['fim'], g['maximo'], g['janelas']) for g in grupos] == [(3, 6, 0.7, 2), (6, 8, 0.3, 1)]


def test_panns_limiar_inclusivo_e_rotulos_onipresentes_fora():
    janelas = [janela_panns(i, Speech=0.9) for i in range(4)]
    janelas[1]['rotulos']['Applause'] = 0.3
    janelas[2]['rotulos']['Applause'] = 0.29
    itens, onipresentes = itens_panns(janelas)
    assert onipresentes == {'Speech': 1.0}
    assert itens == [{'inicio': 1, 'fim': 3, 'rotulo': 'Applause', 'probabilidade_maxima': 0.3}]


def test_panns_metade_exata_nao_e_onipresente():
    janelas = [janela_panns(0, Music=0.5), janela_panns(1, Music=0.1)]
    itens, onipresentes = itens_panns(janelas)
    assert onipresentes == {} and len(itens) == 1


def test_clap_retira_descricoes_atratoras():
    ordem_ruido = ['record noise', 'speech', 'music', 'wind', 'bell']
    janelas = [janela_clap(i, ordem_ruido) for i in range(6)]
    janelas += [janela_clap(6, ['wind', 'bell', 'speech', 'music', 'record noise']),
                janela_clap(7, ['wind', 'bell', 'speech', 'music', 'record noise'])]
    itens, atratores = itens_clap(janelas)
    assert set(atratores) == {'record noise', 'speech', 'music'}
    assert itens == [{'inicio': 6, 'fim': 9, 'descricao': 'wind'}]


def test_entrada_tem_identificadores_em_ordem_de_tempo_e_nada_alem_das_fontes():
    segs = [seg(5, 6, 'b'), seg(0, 1, 'a')]
    panns = [janela_panns(i, Speech=0.9) for i in range(4)]
    panns[2]['rotulos']['Bell'] = 0.6
    panns[0]['rotulos']['Wind'] = 0.4
    clap = [janela_clap(i, ['x', 'y', 'z', 'w']) for i in range(4)]
    entrada, _ = monta_entrada(5, 441.321, segs, [], panns, clap)
    assert set(entrada) == {'faixa', 'duracao_s', 'legenda', 'fala', 'eventos_panns', 'resumo_panns',
                            'descricoes_clap'}
    assert [(f['id'], f['texto']) for f in entrada['fala']] == [('F-001', 'a'), ('F-002', 'b')]
    assert [(p['id'], p['rotulo']) for p in entrada['eventos_panns']] == [('P-001', 'Wind'), ('P-002', 'Bell')]
    assert 'Speech (100% das janelas)' in entrada['resumo_panns']
    assert entrada['duracao_s'] == 441.32
