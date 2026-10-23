# Fase 4 · Eventos sonoros

Material produzido entre 19 e 23/10/2026. A tabela de eventos de referência e o desenho experimental foram registrados antes de qualquer execução dos detectores de eventos sonoros.

| Arquivo | Conteúdo |
|---|---|
| [`01_eventos_referencia.md`](01_eventos_referencia.md) | Tabela dos sons registrados pela escuta nas fases anteriores, com tempos, classes e fontes, fechada antes das execuções |
| [`02_desenho_experimental.md`](02_desenho_experimental.md) | Pré-registro da fase, com modelos, condições, janelas, critérios de apontamento, vocabulário do CLAP, correspondência entre rótulos e classes, medidas e critérios da escuta dirigida |
| [`fase4a_deteccao.ipynb`](fase4a_deteccao.ipynb) | Caderno do Google Colab que aplica o PANNs e o CLAP às cinco faixas, sem e com filtro, e salva cada execução em JSON, com o teste de determinismo, a visão geral das saídas, as figuras e a função usada na escuta dirigida |
| [`fase4b_comparacao.ipynb`](fase4b_comparacao.ipynb) | Caderno do Google Colab que compara os rótulos com a tabela de referência, mede o efeito do filtro, examina a faixa 04, os aplausos e a tosse, os rótulos registrados à parte e o excesso de apontamentos do CLAP, confronta os resultados com as expectativas da fase 1, monta a lista da escuta dirigida e executa os testes automáticos |
| [`03_escuta_dirigida.md`](03_escuta_dirigida.md) | Escuta, pela pesquisadora, dos 34 trechos selecionados, em dois tempos, com classificação de cada rótulo e aplicação do critério de surpresa da fase 1 |
| [`diario.md`](diario.md) | Achados da fase, decisões posteriores ao desenho, confronto com as expectativas, observações sobre língua e categorias, limitações e implicações para a fase 5 |
| [`figuras/`](figuras/) | Espectrograma e rótulos do PANNs ao longo de cada faixa, na condição sem filtro |
| [`original/`](original/) | Tabela de eventos de referência e caderno da escuta dirigida preenchidos em Word |

Arquivos da fase em outras pastas do repositório:

| Pasta | Conteúdo |
|---|---|
| [`resultados/fase4/`](../../resultados/fase4/) | Os 21 JSON das execuções (vinte execuções e a repetição do teste de determinismo) |
| [`resultados/fase4/medidas/`](../../resultados/fase4/medidas/) | Tabelas produzidas pelo caderno de comparação (eventos nomeados, proporção por classe, termos de Almirante no CLAP, frequência das descrições do CLAP e lista da escuta dirigida) |
| [`src/eventos.py`](../../src/eventos.py) | Funções de leitura da referência, nomeação e seleção dos trechos, idênticas às do caderno de comparação |
| [`tests/test_eventos.py`](../../tests/test_eventos.py) | Nove testes automáticos da leitura da tabela, dos limiares e dos critérios da escuta dirigida |

O caderno de detecção foi publicado sem tocadores de áudio. Para executá-lo é preciso ter acesso aos arquivos de áudio, depositados com acesso restrito no Zenodo ([10.5281/zenodo.23240974](https://doi.org/10.5281/zenodo.23240974)), e uma GPU. O caderno de comparação não usa os áudios nem a GPU, e todas as comparações podem ser reproduzidas a partir dos JSON de `resultados/fase4/`, da tabela de referência e, na seção 6, dos JSON da fase 3.
