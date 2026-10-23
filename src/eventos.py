"""Funções da comparação da fase 4 (eventos de referência × rótulos dos detectores).

Cópia idêntica das funções definidas no caderno docs/fase4/fase4b_comparacao.ipynb, mantida
aqui para os testes automáticos de tests/test_eventos.py. As regras vêm de
docs/fase4/02_desenho_experimental.md e da decisão de 20/10/2026 registrada no diário da fase.
"""
import re

LIMIAR_APONTADO = 0.3     # PANNs, seção 4 do desenho
LIMIAR_INDICIO = 0.1      # PANNs, seção 4 do desenho
TOP_CLAP = 3              # CLAP, seção 4 do desenho
LIMIAR_SEM_CLASSE = 0.5   # PANNs, critério 2 da escuta dirigida (seção 9)
FOLGA_AGRUPAMENTO = 5     # segundos, decisão de 20/10/2026

# Classes presentes do começo ao fim, fora do critério 1 da escuta dirigida (seção 9)
SEMPRE_PRESENTES = {'ruído de disco': {1, 2, 3, 4, 5}, 'fala': {1, 2, 3}}

# Seção 6 do desenho experimental: rótulos do AudioSet (PANNs) por classe da referência.
# A classe "música" é completada pela função rotulos_musica.
PANNS_CLASSES = {
    'aplauso': ['Applause', 'Clapping'],
    'grito de plateia': ['Cheering', 'Crowd', 'Shout', 'Yell', 'Hubbub, speech noise, speech babble'],
    'tosse': ['Cough', 'Throat clearing'],
    'fala': ['Speech', 'Male speech, man speaking', 'Narration, monologue', 'Conversation'],
    'voz alterada': ['Distortion'],
    'ruído de disco': ['Hiss', 'Static', 'Crackle', 'Noise', 'White noise', 'Pink noise'],
    'estalos regulares': ['Clicking', 'Tick', 'Tick-tock', 'Crackle'],
    'papel': ['Crumpling, crinkling', 'Rustle', 'Tearing'],
    'surdo': ['Bass drum', 'Drum', 'Timpani'],
    'tamborim': ['Drum', 'Snare drum', 'Percussion'],
    'vento': ['Wind', 'Wind noise (microphone)'],
    'canto': ['Singing', 'Female singing', 'Choir', 'Chant', 'Vocal music'],
    'sino': ['Bell', 'Church bell', 'Chime', 'Tubular bells'],
    'passos': ['Walk, footsteps'],
    'zumbido': ['Hum', 'Mains hum', 'Buzz'],
}

# Descrições do CLAP por classe da referência
CLAP_CLASSES = {
    'aplauso': ['applause'],
    'grito de plateia': ['a crowd cheering and shouting'],
    'tosse': ['a man coughing'],
    'fala': ['a man giving a speech'],
    'voz alterada': ['a distorted voice'],
    'ruído de disco': ['the surface noise of an old record'],
    'estalos regulares': ['clicks of a scratched record'],
    'pulos': ['a skipping record'],
    'papel': ['a page of paper being turned'],
    'surdo': ['surdo', 'a surdo, a large Brazilian bass drum', 'a bass drum'],
    'tamborim': ['tamborim', 'a tamborim, a small Brazilian frame drum played with a stick', 'a snare drum'],
    'música': ['music'],
    'vento': ['wind'],
    'canto': ['women singing'],
    'sino': ['a church bell'],
    'passos': ['footsteps'],
    'zumbido': ['electrical hum'],
}

# Rótulos registrados à parte (seção 6)
A_PARTE_PANNS = {
    'Tambourine': 'tamborim (homônimo)', 'Silence': 'pausa', 'Door': 'passos (alternativa)',
    'Knock': 'passos (alternativa)', 'Ocean': 'surpresa da fase 1', 'Waves, surf': 'surpresa da fase 1',
}
A_PARTE_CLAP = {
    'a tambourine': 'tamborim (homônimo)', 'silence': 'pausa',
    'a door knocking': 'passos (alternativa)', 'ocean waves': 'surpresa da fase 1',
}


def rotulos_musica(rotulos_audioset):
    """Rótulos do ramo musical do AudioSet (índices 137 a 282), exceto os atribuídos a outras
    classes ou registrados à parte."""
    outros = {r for lista in PANNS_CLASSES.values() for r in lista} | set(A_PARTE_PANNS)
    return [r for r in rotulos_audioset[137:283] if r not in outros]


def mapa_inverso(classes):
    """{rótulo: {classes}} a partir de {classe: [rótulos]}."""
    inverso = {}
    for classe, rotulos in classes.items():
        for r in rotulos:
            inverso.setdefault(r, set()).add(classe)
    return inverso


def segundos(t):
    """'4:17,15' -> 257.15"""
    m, s = t.strip().split(':')
    return int(m) * 60 + float(s.replace(',', '.'))


def mmss(s):
    """257.15 -> '4:17,2'"""
    return f'{int(s // 60)}:{s % 60:04.1f}'.replace('.', ',')


def ler_referencia(texto):
    """Lê as tabelas de eventos do arquivo markdown. Devolve uma lista de dicionários."""
    eventos = []
    for linha in texto.splitlines():
        m = re.match(r'^\|\s*(\d+)\.(\d+)\s*\|', linha)
        if not m:
            continue
        cel = [c.strip() for c in linha.strip().strip('|').split('|')]
        eventos.append({
            'id': cel[0], 'faixa': int(m.group(1)), 'inicio': segundos(cel[1]), 'fim': segundos(cel[2]),
            'classe': cel[3], 'descricao': cel[4], 'fonte': cel[5],
            'componentes': [c.strip() for c in re.split(r',| e ', cel[3]) if c.strip()],
        })
    return eventos


def sobrepoe(janela, inicio, fim):
    """A janela e o intervalo [inicio, fim] têm algum tempo em comum."""
    return janela['inicio'] < fim and janela['fim'] > inicio


def posicoes(janela):
    """CLAP: posição (1 = mais semelhante) de cada descrição na janela."""
    ordem = sorted(janela['semelhancas'], key=janela['semelhancas'].get, reverse=True)
    return {termo: k for k, termo in enumerate(ordem, start=1)}


def primeiro(janela):
    """CLAP: descrição mais semelhante da janela."""
    return max(janela['semelhancas'], key=janela['semelhancas'].get)


def nomeacao_panns(classe, janelas, classes_panns):
    """Situação de uma classe num conjunto de janelas (as que se sobrepõem a um evento).

    Devolve (situação, rótulo, probabilidade, início da janela). A situação é 'nomeado'
    (algum rótulo da classe com pelo menos 0,3), 'indício' (máximo entre 0,1 e 0,3),
    'não nomeado' ou 'sem correspondência' (classe sem rótulo no AudioSet).
    """
    rotulos = classes_panns.get(classe)
    if not rotulos:
        return 'sem correspondência', None, None, None
    melhor = (None, 0.0, None)
    for j in janelas:
        for r in rotulos:
            p = j['rotulos'].get(r, 0.0)
            if p > melhor[1]:
                melhor = (r, p, j['inicio'])
    if melhor[1] >= LIMIAR_APONTADO:
        situacao = 'nomeado'
    elif melhor[1] >= LIMIAR_INDICIO:
        situacao = 'indício'
    else:
        situacao = 'não nomeado'
    return situacao, melhor[0], round(melhor[1], 4) if melhor[0] else None, melhor[2]


def nomeacao_clap(classe, janelas, classes_clap, k=TOP_CLAP):
    """Como nomeacao_panns, para o CLAP. O valor é a melhor posição alcançada por alguma
    descrição da classe. 'nomeado' quando a posição é de 1 a k."""
    termos = classes_clap.get(classe)
    if not termos:
        return 'sem correspondência', None, None, None
    melhor = (None, 10 ** 6, None)
    for j in janelas:
        pos = posicoes(j)
        for t in termos:
            if pos[t] < melhor[1]:
                melhor = (t, pos[t], j['inicio'])
    situacao = 'nomeado' if melhor[1] <= k else 'não nomeado'
    return situacao, melhor[0], melhor[1], melhor[2]


def explicado(n, classe, janela, eventos):
    """A classe está presente na janela segundo a referência (ou fica fora do critério 1)."""
    if n in SEMPRE_PRESENTES.get(classe, set()):
        return True
    return any(e['faixa'] == n and classe in e['componentes'] and sobrepoe(janela, e['inicio'], e['fim'])
               for e in eventos)


def candidatos_panns(n, condicao, janelas, inverso, eventos):
    """Itens da escuta dirigida vindos do PANNs (seção 9 do desenho)."""
    itens = []
    for j in janelas:
        for r, p in j['rotulos'].items():
            if p < LIMIAR_APONTADO:
                continue
            if r in inverso:
                if not all(explicado(n, c, j, eventos) for c in inverso[r]):
                    itens.append(dict(faixa=n, inicio=j['inicio'], fim=j['fim'], modelo='PANNs',
                                      condicao=condicao, criterio=1, rotulo=r, valor=round(p, 2)))
            elif p >= LIMIAR_SEM_CLASSE:
                itens.append(dict(faixa=n, inicio=j['inicio'], fim=j['fim'], modelo='PANNs',
                                  condicao=condicao, criterio=2, rotulo=r, valor=round(p, 2)))
    return itens


def candidatos_clap(n, janelas_sem, janelas_com, inverso, eventos):
    """Itens da escuta dirigida vindos do CLAP (decisão de 20/10/2026). Só entram as janelas em
    que a mesma descrição fica em primeiro lugar com e sem filtro."""
    itens = []
    for a, b in zip(janelas_sem, janelas_com):
        t = primeiro(a)
        if t != primeiro(b):
            continue
        if t in inverso:
            if all(explicado(n, c, a, eventos) for c in inverso[t]):
                continue
            criterio = 1
        else:
            criterio = 2
        itens.append(dict(faixa=n, inicio=a['inicio'], fim=a['fim'], modelo='CLAP',
                          condicao='sem e com', criterio=criterio, rotulo=t, valor=1))
    return itens


def agrupar(itens, folga=FOLGA_AGRUPAMENTO):
    """Numera os trechos da escuta. Itens da mesma faixa que se sobrepõem ou que estão a até
    'folga' segundos um do outro formam um só trecho. Devolve os itens com a chave 'trecho'."""
    ordenados = sorted(itens, key=lambda x: (x['faixa'], x['inicio'], x['fim']))
    saida, trecho, faixa, fim = [], 0, None, None
    for x in ordenados:
        if x['faixa'] != faixa or x['inicio'] > fim + folga:
            trecho += 1
            faixa, fim = x['faixa'], x['fim']
        fim = max(fim, x['fim'])
        saida.append({**x, 'trecho': trecho})
    return saida
