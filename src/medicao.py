"""Funções de normalização, alinhamento e contagem da fase 3.

Reproduzem, sem alteração, as funções definidas no caderno
`docs/fase3/fase3b_medicao.ipynb`, para que possam ser testadas em `tests/`.
"""
import re
import jiwer

CORINGA = '__coringa__'

# Uso de cada [?] por faixa, na ordem em que aparecem (desenho experimental, seção 5)
USOS_INTERROGACAO = {
    1: ['perdida', 'duvida', 'perdida', 'duvida'],
    2: ['perdida', 'perdida', 'perdida', 'perdida'],
    3: ['duvida', 'duvida', 'duvida', 'duvida'],
    4: ['perdida'],
    5: ['duvida', 'duvida', 'duvida', 'duvida', 'perdida', 'perdida', 'perdida'],
}

TERMOS_CRITICOS = {
    1: ['pacaembu', 'dia do trabalho', 'sindicalização'],
    2: ['madrugada', 'meio-dia', 'tardezinha'],
    3: ['prostituição', 'mal necessário'],
    4: ['batucada', 'surdo', 'tamborim'],
    5: ['dom aires correia', 'batel', 'portugal', 'cabral', 'vera cruz'],
}

PALAVRAS_APOSTADAS = {
    2: ['coxilha', 'cinamomos', 'guaipeca', 'cocoricoca', 'treval'],
    5: ['dom aires correia', 'batel'],
}


def limpar(texto):
    """Minúsculas, sem pontuação, hífen interno preservado. Devolve lista de palavras."""
    t = texto.lower()
    t = re.sub(r'[^\w\s-]', ' ', t)          # tudo o que não é letra, algarismo, espaço ou hífen
    t = re.sub(r'(?<!\w)-|-(?!\w)', ' ', t)  # hífen solto (travessão, hífen final de palavra cortada)
    return t.split()


def preparar_referencia(texto, faixa):
    """Aplica as regras da seção 5 do desenho experimental à transcrição de referência.

    Devolve a lista de palavras e, para cada uma, se veio de {fala: ...}.
    As marcações [?] viram a palavra coringa.
    """
    t = re.sub(r'\{som:[^}]*\}', ' ', texto)
    t = t.replace('[...]', '')

    # [?] na ordem em que aparecem
    usos = iter(USOS_INTERROGACAO.get(faixa, []))
    def trocar(m):
        uso = next(usos)
        if uso == 'duvida':
            return f' {CORINGA} '
        return f'{m.group(1)} {CORINGA} '
    t = re.sub(r'(\S*?)\s*\[\?\]', trocar, t)

    palavras, de_fala = [], []
    for parte in re.split(r'(\{fala:[^}]*\})', t):
        if parte.startswith('{fala:'):
            conteudo = parte[len('{fala:'):-1]
            for p in limpar(conteudo):
                palavras.append(p); de_fala.append(True)
        else:
            for p in limpar(parte):
                palavras.append(p); de_fala.append(False)
    return palavras, de_fala


def preparar_maquina(registro):
    """Palavras da saída do modelo, cada uma com início e fim em segundos."""
    # O Whisper às vezes devolve um pronome enclítico como peça separada ("-se", "-nos"),
    # sem espaço inicial. Essas peças são reunidas à palavra anterior ("torna-se").
    pecas = []
    for seg in registro['segmentos']:
        for w in seg.get('words', []):
            if pecas and not w['word'].startswith(' '):
                texto, inicio, _ = pecas[-1]
                pecas[-1] = (texto + w['word'], inicio, w['end'])
            else:
                pecas.append((w['word'], w['start'], w['end']))
    palavras, tempos = [], []
    for texto, inicio, fim in pecas:
        for p in limpar(texto):
            palavras.append(p)
            tempos.append((inicio, fim))
    return palavras, tempos


def alinhar(ref, hip):
    """Alinha referência e saída (jiwer) e devolve uma operação por posição.

    estado_ref[i]: 'acerto', 'substituicao', 'omissao' ou 'coringa'
    estado_hip[j]: 'acerto', 'substituicao', 'insercao' ou 'coringa'
    """
    saida = jiwer.process_words(' '.join(ref), ' '.join(hip))
    estado_ref = [None] * len(ref)
    estado_hip = [None] * len(hip)
    for b in saida.alignments[0]:
        if b.type == 'equal':
            for i in range(b.ref_start_idx, b.ref_end_idx):
                estado_ref[i] = 'acerto'
            for j in range(b.hyp_start_idx, b.hyp_end_idx):
                estado_hip[j] = 'acerto'
        elif b.type == 'substitute':
            for i, j in zip(range(b.ref_start_idx, b.ref_end_idx),
                            range(b.hyp_start_idx, b.hyp_end_idx)):
                op = 'coringa' if ref[i] == CORINGA else 'substituicao'
                estado_ref[i] = op
                estado_hip[j] = op
        elif b.type == 'delete':
            for i in range(b.ref_start_idx, b.ref_end_idx):
                estado_ref[i] = 'coringa' if ref[i] == CORINGA else 'omissao'
        elif b.type == 'insert':
            for j in range(b.hyp_start_idx, b.hyp_end_idx):
                estado_hip[j] = 'insercao'
    return estado_ref, estado_hip


def contar(estado_ref, estado_hip):
    n = sum(1 for e in estado_ref if e != 'coringa')
    s = estado_ref.count('substituicao')
    d = estado_ref.count('omissao')
    i = estado_hip.count('insercao')
    return {'N': n, 'acertos': estado_ref.count('acerto'), 'S': s, 'D': d, 'I': i,
            'WER': (s + d + i) / n if n else float('nan')}


def ocorrencias(palavras, termo):
    alvo = limpar(termo)
    k = len(alvo)
    return [list(range(i, i + k)) for i in range(len(palavras) - k + 1)
            if palavras[i:i + k] == alvo]


def classificar_termos(termos, ref, estado_ref, hip, estado_hip, tempos):
    linhas = []
    for termo in termos:
        for idx in ocorrencias(ref, termo):
            estados = [estado_ref[i] for i in idx]
            if all(e == 'acerto' for e in estados):
                classe = 'mantido'
            elif all(e == 'omissao' for e in estados):
                classe = 'omitido'
            else:
                classe = 'substituído'
            linhas.append({'termo': termo, 'classe': classe, 'inicio': None})
        for idx in ocorrencias(hip, termo):
            if not all(estado_hip[j] == 'acerto' for j in idx):
                linhas.append({'termo': termo, 'classe': 'inventado',
                               'inicio': tempos[idx[0]][0]})
    return linhas


def trechos_inseridos(hip, estado_hip, tempos, minimo=3):
    """Sequências de 'minimo' ou mais palavras inseridas pelo modelo."""
    trechos, atual = [], []
    for j, e in enumerate(estado_hip + [None]):
        if e == 'insercao':
            atual.append(j)
        else:
            if len(atual) >= minimo:
                trechos.append({'inicio': tempos[atual[0]][0], 'fim': tempos[atual[-1]][1],
                                'texto': ' '.join(hip[k] for k in atual)})
            atual = []
    return trechos
