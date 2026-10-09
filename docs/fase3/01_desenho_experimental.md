# Desenho experimental da fase 3

Registro fechado em 09/10/2026, antes de qualquer execução de modelo de reconhecimento de fala sobre o corpus. As escolhas abaixo valem para todas as execuções e medições da fase. Qualquer alteração posterior será registrada no diário da fase, com data e motivo, sem apagar este texto.

As transcrições de referência da fase 1 (`docs/fase1/transcricoes/`) não são alteradas. A normalização descrita na seção 5 atua sobre uma cópia, gerada pelo caderno de medição.

## 1. Pergunta

Quanto o reconhecimento automático de fala erra nas cinco faixas, quais termos críticos ele mantém, troca, omite ou inventa, e que efeito têm sobre isso um glossário de domínio e um filtro de ruído.

## 2. Condições

Duas variáveis, cada uma ligada ou desligada, combinadas em quatro condições aplicadas às cinco faixas, num total de 20 execuções.

| Condição | Glossário | Filtro |
|---|---|---|
| A (linha de base) | não | não |
| B | sim | não |
| C | não | sim |
| D | sim | sim |

A comparação entre B e A isola o efeito do glossário, e a comparação entre C e A isola o efeito do filtro. A condição D indica se os dois efeitos se somam.

## 3. Modelo, parâmetros e entrada

- Biblioteca `openai-whisper`, modelo `large-v3`, executado em GPU no Google Colab.
- Idioma fixado em português (`language="pt"`) e marcação de tempo por palavra (`word_timestamps=True`).
- Todos os demais parâmetros nos valores padrão da biblioteca, inclusive a sequência de temperaturas de recurso, porque a pergunta é o que a ferramenta faz tal como é distribuída.
- Semente aleatória fixada em 0 antes de cada execução.
- Entrada de cada faixa igual à soma dos canais dividida por dois, decisão registrada no diário da fase 2, reamostrada para 16 kHz, que é a taxa exigida pelo modelo. A reamostragem descarta tudo acima de 8 kHz, o que nessas gravações atinge apenas ruído da digitalização, mas constitui um segundo filtro implícito na entrada, ao lado da soma dos canais.
- O modelo e todos os parâmetros permanecem fixos nas quatro condições, de modo que apenas glossário e filtro variam.

**Teste de determinismo.** Antes das 20 execuções, a condição A será executada duas vezes sobre a faixa 04. Se as duas saídas forem idênticas, cada condição roda uma vez. Se diferirem, cada condição roda três vezes em cada faixa, e os resultados passam a ser relatados como média e amplitude.

## 4. Glossário de domínio

O glossário de cada faixa é a lista de termos críticos registrada na fase 1 (`docs/fase1/04_convencoes_e_termos_criticos.md`, fechada em 01/10/2026), sem acréscimos. Ele é passado ao modelo como prompt inicial, repetido em todos os trechos de 30 segundos da faixa (`carry_initial_prompt=True`). Os textos exatos são estes.

| Faixa | Prompt inicial |
|---|---|
| 01 | `Pacaembu, Dia do Trabalho, sindicalização.` |
| 02 | `Madrugada, Meio-dia, Tardezinha.` |
| 03 | `prostituição, mal necessário.` |
| 04 | `batucada, surdo, tamborim, primeiro tamborim, segundo tamborim.` |
| 05 | `Dom Aires Correia, batel, Portugal, Cabral, Vera Cruz.` |

Na faixa 04, a expressão "entre outros instrumentos" da lista da fase 1 não entra no glossário, por não nomear termos.

Os termos da faixa 01 e o termo "Vera Cruz" da faixa 05 não são pronunciados nas gravações. Eles vêm da descrição do evento, e não da fala. Para esses termos, a única medida possível é a de invenção, ou seja, se o glossário leva o modelo a escrevê-los onde ninguém os disse.

## 5. Normalização para o cálculo

Aplicada igualmente à referência e à saída do modelo.

- Conversão para minúsculas.
- Remoção da pontuação, inclusive dos travessões de início de linha da faixa 05. O hífen interno das palavras é mantido ("torna-se", "meio-dia").
- Acentos e grafia mantidos como estão.
- Números não são convertidos. Divergências apenas de grafia numérica (por exemplo "500" e "quinhentos") contam como erro e serão listadas à parte.
- `{som: …}` é removido.
- `{fala: …}` é removido do cálculo principal e usado na medida complementar da seção 6.
- `[...]` é removido.
- `[?]` é substituído por uma posição coringa, conforme a tabela abaixo. Em caso de dúvida, sai a palavra duvidosa junto com a marcação. Em caso de palavra perdida, só a marcação é substituída. A posição coringa aceita qualquer palavra do modelo, ou nenhuma, sem contar como erro, e não entra no total de palavras da referência.

| # | Faixa | Trecho | Uso |
|---|---|---|---|
| 1 | 01 | passe-me [?] cerrar | palavra perdida |
| 2 | 01 | lei orgânica fugita [?] | dúvida |
| 3 | 01 | lavoura de [?] [...] cultura | palavra perdida |
| 4 | 01 | engregar [?] nas agremiações | dúvida |
| 5 | 02 | O gado invadindo [?] [...] | palavra perdida |
| 6 | 02 | para fugir [?] [...] derrama | palavra perdida |
| 7 | 02 | só um cavalo [?] [...] casco | palavra perdida |
| 8 | 02 | porque teve [?] [...] Debaixo | palavra perdida |
| 9 | 03 | o derece [?] mais preventivo | dúvida |
| 10 | 03 | explorando a alcocies[?] | dúvida |
| 11 | 03 | o bafom [?] carioca | dúvida |
| 12 | 03 | só aos cafitens[?] interessava | dúvida |
| 13 | 04 | depois do [?] [...] de som | palavra perdida |
| 14 | 05 | totinegras [?] do moinho | dúvida |
| 15 | 05 | apolas [?] do meu trigal | dúvida |
| 16 | 05 | moças loiras [?] | dúvida |
| 17 | 05 | iam a farrado [?] | dúvida |
| 18 | 05 | ele é [?]. | palavra perdida |
| 19 | 05 | as [?] no mar passam | palavra perdida |
| 20 | 05 | passam a vos [?]. | palavra perdida |

## 6. Medidas

**Taxa de erro de palavra (WER).** Calculada por faixa e por condição, com a biblioteca `jiwer`, e decomposta em substituições, omissões e inserções. Também é calculada uma taxa global por condição, com a soma dos erros dividida pela soma das palavras de referência. A faixa 04 tem poucas palavras de referência, e sua taxa será lida com essa ressalva.

**Termos críticos.** Cada ocorrência de termo crítico na referência é classificada como mantida, substituída ou omitida, a partir do alinhamento entre referência e saída. Termos de mais de uma palavra só contam como mantidos se todas as palavras forem mantidas. Conta como inventada toda ocorrência, na saída do modelo, de um termo crítico ou apostado que não corresponda a uma ocorrência do mesmo termo na referência. Os termos são procurados na forma exata em que constam na lista ou na referência, sem flexões.

**Palavras apostadas.** As palavras que as expectativas da fase 1 apostaram que seriam perdidas recebem a mesma classificação, fora do glossário: coxilha, cinamomos, guaipeca, cocoricoca e treval (faixa 02); Dom Aires Correia e batel (faixa 05).

**Hesitações apagadas.** Como medida complementar, as palavras marcadas com `{fala: …}` são reincluídas na referência, e conta-se quantas delas o modelo omitiu.

**Custo e tempo.** O tempo de processamento de cada execução é registrado.

## 7. Saídas

Cada execução gera um arquivo JSON em `resultados/fase3/`, nomeado por faixa e condição (por exemplo, `faixa01_A.json`), com o texto completo, os segmentos com início e fim, as palavras com marcação de tempo e probabilidade, os indicadores de confiança de cada segmento (`avg_logprob`, `no_speech_prob`, `compression_ratio`), o prompt usado, todos os parâmetros, a semente, as versões das bibliotecas, a GPU e a duração do processamento.

O cálculo das medidas usa apenas esses arquivos e as transcrições de referência, de modo que pode ser reproduzido sem acesso aos áudios.

## 8. Escuta dirigida

Depois das execuções, a pesquisadora escuta os trechos que atendam a pelo menos um destes critérios e registra o que ouve:

- sequência de três ou mais palavras inseridas pelo modelo onde a referência não tem fala;
- segmento com texto e `no_speech_prob` acima de 0,6;
- termo crítico ou apostado inventado.

## 9. Confronto com as expectativas

Os resultados serão confrontados, item por item, com as expectativas registradas em `docs/fase1/05_expectativas.md`, inclusive quando as contrariarem.
