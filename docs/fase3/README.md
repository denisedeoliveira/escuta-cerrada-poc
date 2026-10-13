# Fase 3 · Reconhecimento de fala e medição

Material produzido entre 09 e 13/10/2026. O desenho experimental foi registrado antes de qualquer execução do modelo de reconhecimento de fala.

| Arquivo | Conteúdo |
|---|---|
| [`01_desenho_experimental.md`](01_desenho_experimental.md) | Pré-registro da fase, com condições, modelo, glossário, filtro, regras de normalização, medidas e critérios da escuta dirigida |
| [`fase3a_transcricao.ipynb`](fase3a_transcricao.ipynb) | Caderno do Google Colab que executa o Whisper large-v3 nas cinco faixas e nas quatro condições e salva cada execução em JSON, com o teste de determinismo, a visão geral das saídas e a função usada na escuta dirigida |
| [`fase3b_medicao.ipynb`](fase3b_medicao.ipynb) | Caderno do Google Colab que calcula a taxa de erro de palavra, classifica os termos críticos e as palavras apostadas, produz as medidas complementares e a lista de trechos para a escuta dirigida, e executa os testes automáticos |
| [`02_escuta_dirigida.md`](02_escuta_dirigida.md) | Escuta, pela pesquisadora, dos 31 trechos selecionados, com transcrição do que soa, texto da máquina e classificação |
| [`diario.md`](diario.md) | Achados da fase, decisões posteriores ao desenho, confronto com as expectativas da fase 1, limitações e implicações para as fases 4 e 5 |
| [`original/`](original/) | Caderno da escuta dirigida preenchido em Word |

Arquivos da fase em outras pastas do repositório:

| Pasta | Conteúdo |
|---|---|
| [`resultados/fase3/`](../../resultados/fase3/) | Os 21 JSON das execuções (vinte condições e a repetição do teste de determinismo) |
| [`resultados/fase3/medidas/`](../../resultados/fase3/medidas/) | Tabelas produzidas pelo caderno de medição (WER por faixa, WER global, termos e lista da escuta dirigida) |
| [`src/medicao.py`](../../src/medicao.py) | Funções de normalização, alinhamento e contagem, idênticas às do caderno de medição |
| [`tests/test_wer.py`](../../tests/test_wer.py) | Nove testes automáticos das regras de normalização e de contagem |

O caderno de transcrição foi enviado sem as saídas que continham tocadores de áudio. Para executá-lo é preciso ter acesso aos arquivos de áudio, depositados com acesso restrito no Zenodo ([10.5281/zenodo.23240974](https://doi.org/10.5281/zenodo.23240974)), e uma GPU. O caderno de medição não usa os áudios, e todas as medidas podem ser reproduzidas a partir dos JSON e das transcrições de referência de `docs/fase1/transcricoes/`.
