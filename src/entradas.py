"""Funções da montagem das entradas do LLM na fase 5.

Cópia idêntica das funções definidas no caderno docs/fase5/fase5a_entradas.ipynb, mantida
aqui para os testes automáticos de tests/test_entradas.py. As regras vêm da seção 3 de
docs/fase5/01_desenho_experimental.md.
"""
import re
from collections import Counter

LIMIAR_REPETICAO = 3              # segmentos com o mesmo texto
LIMIAR_SEM_FALA = 0.6             # no_speech_prob, critério da fase 3
LIMIAR_LOGPROB = -1.0             # avg_logprob
LIMIAR_DIVERGENCIA = 0.5          # proporção de palavras encontradas na condição C
LIMIAR_PANNS = 0.3                # rótulo apontado, critério da fase 4
PROPORCAO_ONIPRESENTE_PANNS = 0.5 # rótulos acima disso ficam fora dos itens
TOP_CLAP = 3                      # posições consideradas para os atratores
PROPORCAO_ATRATOR_CLAP = 0.25     # descrições acima disso ficam fora dos itens

LEGENDA = {
    'fala': (
        'Segmentos produzidos pelo modelo de reconhecimento de fala Whisper (large-v3), sem filtro '
        'de ruído, com início e fim em segundos, o texto escrito pelo modelo e três indicadores do '
        'próprio modelo. avg_logprob é a média do logaritmo da probabilidade dos tokens do texto '
        '(valores mais baixos correspondem a menor confiança do modelo no texto). no_speech_prob é '
        'a probabilidade, estimada pelo modelo, de que o segmento não contenha fala. '
        'compression_ratio é a razão de compressão do texto (valores altos correspondem a texto '
        'repetitivo dentro do segmento). O campo sinais lista os sinais calculados a partir desses dados.'
    ),
    'sinais': {
        'repetição': 'o mesmo texto aparece em três ou mais segmentos da faixa',
        'indicação de ausência de fala': 'no_speech_prob acima de 0,6',
        'baixa confiança': 'avg_logprob abaixo de -1,0',
        'divergência entre transcrições': (
            'menos da metade das palavras do segmento aparece, no mesmo intervalo, numa segunda '
            'transcrição da mesma gravação feita pelo mesmo modelo depois de um filtro de redução de ruído'
        ),
    },
    'eventos_panns': (
        'Intervalos em que o detector de eventos sonoros PANNs (Cnn14, treinado com as 527 categorias '
        'do AudioSet) atribuiu probabilidade de pelo menos 0,3 a um rótulo, em janelas de 2 segundos '
        'com passo de 1 segundo. Janelas consecutivas com o mesmo rótulo foram reunidas num intervalo. '
        'probabilidade_maxima é o maior valor do rótulo no intervalo.'
    ),
    'descricoes_clap': (
        'Intervalos em que uma descrição textual, em inglês, ficou em primeiro lugar entre 28 na '
        'comparação feita pelo modelo CLAP entre o áudio e as descrições, em janelas de 2 segundos '
        'com passo de 1 segundo. Janelas consecutivas com a mesma descrição foram reunidas num '
        'intervalo. As descrições que ficaram entre as três primeiras em mais de um quarto das '
        'janelas da faixa foram retiradas.'
    ),
}


def palavras(texto):
    """Palavras em minúsculas, sem pontuação."""
    return re.sub(r'[^\w\s]', ' ', texto.lower()).split()


def normaliza(texto):
    """Texto em minúsculas, sem pontuação e com espaços simples."""
    return ' '.join(palavras(texto))


def sinais_fala(segmentos, palavras_c):
    """Lista de sinais de cada segmento da condição A.

    palavras_c: palavras da condição C, cada uma com 'word', 'start' e 'end'."""
    contagem = Counter(normaliza(s['text']) for s in segmentos)
    saida = []
    for s in segmentos:
        sinais = []
        texto = normaliza(s['text'])
        if texto and contagem[texto] >= LIMIAR_REPETICAO:
            sinais.append('repetição')
        if s['no_speech_prob'] > LIMIAR_SEM_FALA:
            sinais.append('indicação de ausência de fala')
        if s['avg_logprob'] < LIMIAR_LOGPROB:
            sinais.append('baixa confiança')
        ps = palavras(s['text'])
        if ps:
            em_c = {p for w in palavras_c if w['start'] < s['end'] and w['end'] > s['start']
                    for p in palavras(w['word'])}
            if sum(p in em_c for p in ps) / len(ps) < LIMIAR_DIVERGENCIA:
                sinais.append('divergência entre transcrições')
        saida.append(sinais)
    return saida


def reune(marcadas):
    """Reúne janelas consecutivas. marcadas: lista de (índice, início, fim, valor) em ordem.
    Devolve intervalos com início, fim, valor máximo e número de janelas."""
    grupos = []
    for i, inicio, fim, valor in marcadas:
        if grupos and grupos[-1]['ultima'] == i - 1:
            g = grupos[-1]
            g['fim'], g['ultima'], g['maximo'], g['janelas'] = fim, i, max(g['maximo'], valor), g['janelas'] + 1
        else:
            grupos.append({'inicio': inicio, 'fim': fim, 'ultima': i, 'maximo': valor, 'janelas': 1})
    return grupos


def itens_panns(janelas):
    """Itens do PANNs e rótulos onipresentes ({rótulo: proporção de janelas})."""
    por_rotulo = {}
    for i, j in enumerate(janelas):
        for rotulo, p in j['rotulos'].items():
            if p >= LIMIAR_PANNS:
                por_rotulo.setdefault(rotulo, []).append((i, j['inicio'], j['fim'], p))
    onipresentes = {r: len(v) / len(janelas) for r, v in por_rotulo.items()
                    if len(v) / len(janelas) > PROPORCAO_ONIPRESENTE_PANNS}
    itens = [{'inicio': g['inicio'], 'fim': g['fim'], 'rotulo': r, 'probabilidade_maxima': round(g['maximo'], 2)}
             for r, v in por_rotulo.items() if r not in onipresentes for g in reune(v)]
    return itens, onipresentes


def itens_clap(janelas):
    """Itens do CLAP e descrições atratoras ({descrição: proporção de janelas no top-3})."""
    ordens = [sorted(j['semelhancas'], key=j['semelhancas'].get, reverse=True) for j in janelas]
    top = Counter(d for o in ordens for d in o[:TOP_CLAP])
    atratores = {d: c / len(janelas) for d, c in top.items() if c / len(janelas) > PROPORCAO_ATRATOR_CLAP}
    por_descricao = {}
    for i, (j, o) in enumerate(zip(janelas, ordens)):
        if o[0] not in atratores:
            por_descricao.setdefault(o[0], []).append((i, j['inicio'], j['fim'], 0))
    itens = [{'inicio': g['inicio'], 'fim': g['fim'], 'descricao': d}
             for d, v in por_descricao.items() for g in reune(v)]
    return itens, atratores


def identifica(itens, prefixo):
    """Ordena por tempo e acrescenta identificadores (F-001, P-001, C-001)."""
    ordenados = sorted(itens, key=lambda x: (x['inicio'], x['fim']))
    return [{'id': f'{prefixo}-{k:03d}', **x} for k, x in enumerate(ordenados, 1)]


def monta_entrada(faixa, duracao, segmentos_a, palavras_c, janelas_panns, janelas_clap):
    """Arquivo de entrada de uma faixa (seção 3 do desenho)."""
    sinais = sinais_fala(segmentos_a, palavras_c)
    fala = [{'inicio': round(s['start'], 2), 'fim': round(s['end'], 2), 'texto': s['text'].strip(),
             'avg_logprob': round(s['avg_logprob'], 2), 'no_speech_prob': round(s['no_speech_prob'], 2),
             'compression_ratio': round(s['compression_ratio'], 2), 'sinais': si}
            for s, si in zip(segmentos_a, sinais)]
    panns, onipresentes = itens_panns(janelas_panns)
    clap, atratores = itens_clap(janelas_clap)
    if onipresentes:
        lista = ', '.join(f'{r} ({p:.0%} das janelas)' for r, p in sorted(onipresentes.items()))
        resumo = f'Rótulos apontados em mais da metade das janelas da faixa, que não entram como itens: {lista}.'
    else:
        resumo = 'Nenhum rótulo foi apontado em mais da metade das janelas da faixa.'
    entrada = {
        'faixa': faixa,
        'duracao_s': round(duracao, 2),
        'legenda': LEGENDA,
        'fala': identifica(fala, 'F'),
        'eventos_panns': identifica(panns, 'P'),
        'resumo_panns': resumo,
        'descricoes_clap': identifica(clap, 'C'),
    }
    return entrada, atratores
