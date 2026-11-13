"""Funções das chamadas ao LLM e das medidas da fase 5.

Cópia idêntica das funções definidas no caderno docs/fase5/fase5b_dossies.ipynb, mantida
aqui para os testes automáticos de tests/test_dossie.py. As regras vêm das seções 4, 5 e 7 de
docs/fase5/01_desenho_experimental.md, e a instrução de sistema é o texto do anexo A.
"""
import json
import re
from itertools import combinations

INSTRUCAO = (
    'Você recebe as saídas de modelos automáticos aplicados a uma gravação sonora em disco. Você não '
    'tem acesso ao áudio. Sua tarefa é indicar a uma pesquisadora os momentos da gravação em que vale '
    'escutar com atenção, com base apenas nos itens da entrada.\n\n'
    '1. Cada indicação deve citar os identificadores dos itens da entrada que a sustentam. O início e o '
    'fim da indicação devem ficar dentro do intervalo desses itens.\n'
    '2. Descreva o que os modelos registraram, e não o que soa. Por exemplo, escreva “o modelo de fala '
    'escreveu o mesmo texto em seis segmentos seguidos” ou “o detector de eventos atribuiu 0,82 ao '
    'rótulo Applause”, e não “há aplausos” ou “o orador repete a frase”.\n'
    '3. Não interprete sentido, intenção, ironia, emoção, gênero, tema ou contexto da gravação, e não '
    'deduza o que ela representa.\n'
    '4. Use apenas os motivos da lista fornecida e atribua o grau de apoio segundo a regra fornecida.\n'
    '5. Se um trecho não tiver nada a indicar, não crie indicação para ele.\n'
    '6. A frase de cada indicação deve dizer o que a pesquisadora pode verificar na escuta, em uma ou '
    'duas frases, em português.'
)

MOTIVOS = [
    'repetição na transcrição',
    'texto com indicação de ausência de fala',
    'transcrição com baixa confiança',
    'divergência entre transcrições',
    'evento sonoro apontado',
    'coincidência entre fontes',
    'rótulo isolado',
]
GRAUS = ['alto', 'médio', 'baixo']

REGRAS_PEDIDO = (
    'Motivos possíveis: ' + '; '.join(MOTIVOS[:-1]) + '; rótulo isolado (rótulo ou descrição que '
    'aparece uma única vez na faixa).\n\n'
    'Regra do grau de apoio:\n'
    '- alto: dois ou mais itens de fontes diferentes (fala, PANNs, CLAP) coincidem no intervalo, ou um '
    'rótulo do PANNs tem probabilidade de pelo menos 0,5;\n'
    '- médio: um único item do PANNs com probabilidade entre 0,3 e 0,5, ou um único segmento de fala '
    'com algum dos quatro sinais;\n'
    '- baixo: apenas uma descrição do CLAP.'
)

ESQUEMA = {
    'type': 'object',
    'properties': {
        'indicacoes': {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {
                    'inicio': {'type': 'number', 'description': 'início da indicação, em segundos'},
                    'fim': {'type': 'number', 'description': 'fim da indicação, em segundos'},
                    'fontes': {'type': 'array', 'items': {'type': 'string'},
                               'description': 'identificadores dos itens da entrada que sustentam a indicação'},
                    'motivo': {'type': 'string', 'enum': MOTIVOS},
                    'grau_de_apoio': {'type': 'string', 'enum': GRAUS},
                    'frase': {'type': 'string', 'description': 'o que a pesquisadora pode verificar na escuta'},
                },
                'required': ['inicio', 'fim', 'fontes', 'motivo', 'grau_de_apoio', 'frase'],
            },
        },
    },
    'required': ['indicacoes'],
}

TERMOS_INTERPRETATIVOS = [
    'ironia', 'irônico', 'emoção', 'emocionado', 'sentimento', 'triste', 'alegre', 'entusiasmo',
    'intenção', 'pretende', 'quer dizer', 'significa', 'simboliza', 'representa', 'sugere que', 'revela',
]
TOLERANCIA = 1.0  # segundos, medida 2 (invenção)


def monta_pedido(entrada):
    """Texto enviado ao modelo, além da instrução de sistema: regras e entrada da faixa."""
    return (REGRAS_PEDIDO + f'\n\nEntrada da faixa {entrada["faixa"]}:\n'
            + json.dumps(entrada, ensure_ascii=False, indent=1))


def mapa_fontes(entrada):
    """{identificador: item} com os itens das três fontes."""
    return {i['id']: i for bloco in ['fala', 'eventos_panns', 'descricoes_clap'] for i in entrada[bloco]}


def sobrepoe(a, b):
    """Os intervalos a e b têm algum tempo em comum (contato num ponto conta)."""
    return a['inicio'] <= b['fim'] and b['inicio'] <= a['fim']


def problemas_conformidade(ind):
    """Lista do que falta ou é inválido numa indicação (lista vazia = conforme)."""
    p = []
    num = all(isinstance(ind.get(k), (int, float)) and not isinstance(ind.get(k), bool) for k in ['inicio', 'fim'])
    if not num:
        p.append('tempo ausente ou não numérico')
    elif not 0 <= ind['inicio'] <= ind['fim']:
        p.append('início depois do fim')
    f = ind.get('fontes')
    if not isinstance(f, list) or not f or not all(isinstance(x, str) and x for x in f):
        p.append('sem fonte')
    if ind.get('motivo') not in MOTIVOS:
        p.append('motivo fora da lista')
    if ind.get('grau_de_apoio') not in GRAUS:
        p.append('grau fora da lista')
    if not isinstance(ind.get('frase'), str) or not ind['frase'].strip():
        p.append('sem frase')
    return p


def invencao(ind, fontes):
    """(identificadores inexistentes, intervalo fora das fontes citadas com tolerância)."""
    citados = ind.get('fontes') or []
    inexistentes = [i for i in citados if i not in fontes]
    validos = [fontes[i] for i in citados if i in fontes]
    numericos = all(isinstance(ind.get(k), (int, float)) and not isinstance(ind.get(k), bool) for k in ['inicio', 'fim'])
    fora = False
    if validos and numericos:
        fora = (ind['inicio'] < min(v['inicio'] for v in validos) - TOLERANCIA
                or ind['fim'] > max(v['fim'] for v in validos) + TOLERANCIA)
    return inexistentes, fora


def termos_na_frase(frase):
    """Palavras da frase que começam por algum termo da lista (por exemplo, “tristeza” por “triste”)."""
    achados = []
    texto = (frase or '').lower()
    for termo in TERMOS_INTERPRETATIVOS:
        for m in re.finditer(r'(?<!\w)' + re.escape(termo) + r'\w*', texto):
            achados.append(m.group(0))
    return achados


def grau_esperado(ind, fontes):
    """Grau de apoio que a regra da seção 4 atribui às fontes citadas, ou None quando a regra não
    se aplica (identificador inexistente, ou combinação de fontes que a regra não prevê)."""
    citados = ind.get('fontes') or []
    if not citados or any(i not in fontes for i in citados):
        return None
    itens = [(i[0], fontes[i]) for i in citados]
    for (ta, a), (tb, b) in combinations(itens, 2):
        if ta != tb and sobrepoe(a, b):
            return 'alto'
    if any(t == 'P' and x['probabilidade_maxima'] >= 0.5 for t, x in itens):
        return 'alto'
    if len(itens) == 1:
        t, x = itens[0]
        if t == 'P':
            return 'médio'
        if t == 'F' and x['sinais']:
            return 'médio'
        if t == 'C':
            return 'baixo'
    return None


def correspondem(a, b):
    """Duas indicações de chamadas diferentes correspondem: mesmo motivo e sobreposição de tempo."""
    return a.get('motivo') == b.get('motivo') and sobrepoe(a, b)


def estaveis(rodadas):
    """Para cada rodada, lista de booleanos: a indicação tem correspondente em todas as outras."""
    return [[all(any(correspondem(ind, outra) for outra in rodadas[s]) for s in range(len(rodadas)) if s != r)
             for ind in rodadas[r]] for r in range(len(rodadas))]


def alcancado(intervalo, indicacoes):
    """Algum intervalo das indicações tem tempo em comum com o intervalo dado."""
    return any(sobrepoe(intervalo, ind) for ind in indicacoes)


def mmss(s):
    """257.15 -> '4:17,2'"""
    return f'{int(s // 60)}:{s % 60:04.1f}'.replace('.', ',')


def dossie_md(entrada, indicacoes, marcas, cabecalho):
    """Dossiê em Markdown, em ordem de tempo, montado a partir da saída do modelo."""
    linhas = [f'# Dossiê de escuta · faixa {entrada["faixa"]:02d}', '', cabecalho, '']
    ordem = sorted(range(len(indicacoes)), key=lambda k: (indicacoes[k]['inicio'], indicacoes[k]['fim']))
    if not ordem:
        linhas.append('O modelo não fez nenhuma indicação nesta chamada.')
    for n, k in enumerate(ordem, 1):
        ind = indicacoes[k]
        repete = ' · repete-se nas três chamadas' if marcas[k] else ''
        linhas += [f'## {n}. {mmss(ind["inicio"])} a {mmss(ind["fim"])}{repete}', '',
                   f'**Motivo** {ind["motivo"]} · **Grau de apoio** {ind["grau_de_apoio"]} · '
                   f'**Fontes** {", ".join(ind["fontes"])}', '', ind['frase'].strip(), '']
    return '\n'.join(linhas).rstrip() + '\n'
