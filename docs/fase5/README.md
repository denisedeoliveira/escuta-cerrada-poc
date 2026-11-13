# Fase 5 · Síntese e restrição

Material produzido entre 30/10 e 13/11/2026. O desenho experimental e as expectativas foram registrados em 02/11/2026, antes de qualquer chamada ao LLM com dados do corpus.

| Arquivo | Conteúdo |
|---|---|
| [`01_desenho_experimental.md`](01_desenho_experimental.md) | Pré-registro da fase, com modelo e parâmetros, entrada, instrução de sistema (anexo A), regra do grau de apoio, esquema da saída, execuções, medidas, leitura e escuta de conferência e expectativas da pesquisadora |
| [`fase5a_entradas.ipynb`](fase5a_entradas.ipynb) | Caderno do Google Colab que monta, para cada faixa, o arquivo que o LLM recebe, a partir dos JSON das fases 3 e 4, com os sinais da fala, os intervalos do PANNs e do CLAP e a retirada dos rótulos onipresentes e dos atratores, e executa os testes automáticos |
| [`fase5b_dossies.ipynb`](fase5b_dossies.ipynb) | Caderno do Google Colab que faz a chamada de teste e as quinze chamadas ao Gemini, registra cada uma, monta os dossiês, calcula as oito medidas do desenho e executa os testes automáticos |
| [`02_leitura_e_escuta.md`](02_leitura_e_escuta.md) | Leitura dos cinco dossiês pela pesquisadora, com a marcação de interpretação e de afirmação de presença em cada indicação, e escuta de conferência, em dois tempos, da indicação que nenhuma escuta anterior alcançava |
| [`diario.md`](diario.md) | Achados da fase, decisões posteriores ao desenho, confronto com as expectativas, limitações e implicações para a fase 6 |
| [`original/`](original/) | Desenho experimental e formulário de leitura e escuta preenchidos em Word |

Arquivos da fase em outras pastas do repositório:

| Pasta | Conteúdo |
|---|---|
| [`resultados/fase5/entradas/`](../../resultados/fase5/entradas/) | Os cinco arquivos enviados ao LLM, um por faixa |
| [`resultados/fase5/chamadas/`](../../resultados/fase5/chamadas/) | Os dezesseis registros de chamada (o teste e as quinze chamadas), com modelo, versão, parâmetros, instrução, esquema, pedido, resposta, tempo e tokens |
| [`resultados/fase5/dossies/`](../../resultados/fase5/dossies/) | O dossiê de escuta de cada faixa, montado pelo código a partir da primeira chamada |
| [`resultados/fase5/medidas/`](../../resultados/fase5/medidas/) | Tabela de todas as indicações com a conferência automática e tabelas das medidas de conformidade, invenção, restrição, grau de apoio, estabilidade, cobertura, faixa 05 e tempo e custo |
| [`src/entradas.py`](../../src/entradas.py) e [`src/dossie.py`](../../src/dossie.py) | Funções idênticas às dos cadernos 5a e 5b |
| [`tests/test_entradas.py`](../../tests/test_entradas.py) e [`tests/test_dossie.py`](../../tests/test_dossie.py) | Dezenove testes automáticos dos sinais da fala, da montagem das entradas, da identidade entre a instrução e o anexo A, do esquema e das medidas |

Nenhum dos dois cadernos usa os áudios ou a GPU. O caderno 5a pode ser executado a partir dos JSON das fases 3 e 4 publicados no repositório. O caderno 5b precisa de uma chave da API do Gemini, guardada nos Secrets do Colab com o nome `GEMINI_API_KEY` (ver [`.env.example`](../../.env.example)), apenas para as seções 4 e 5, que fazem as chamadas. As seções de dossiês e medidas leem os registros de `resultados/fase5/chamadas/` e podem ser executadas sem chave e sem nenhuma chamada nova. As chamadas foram feitas na camada paga da API, em que o conteúdo enviado não é usado pelo Google, e só enviaram dados já publicados no repositório.
