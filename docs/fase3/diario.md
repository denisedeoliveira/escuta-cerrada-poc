# Diário da fase 3 · Reconhecimento de fala e medição

Trabalho realizado entre 09 e 13/10/2026, registrado nos cadernos [`fase3a_transcricao.ipynb`](fase3a_transcricao.ipynb) (transcrição) e [`fase3b_medicao.ipynb`](fase3b_medicao.ipynb) (medição). As saídas do modelo estão em [`resultados/fase3/`](../../resultados/fase3/), e as tabelas de medidas, em [`resultados/fase3/medidas/`](../../resultados/fase3/medidas/).

As leituras foram feitas pela pesquisadora com apoio do Claude (Anthropic), conforme declarado no projeto. Toda interpretação que depende de escuta foi conferida por ela nos áudios, na escuta dirigida registrada em [`02_escuta_dirigida.md`](02_escuta_dirigida.md).

## 1. Desenho experimental e decisões posteriores

O desenho experimental foi registrado em [`01_desenho_experimental.md`](01_desenho_experimental.md) e versionado em 09/10/2026, antes de qualquer execução. Quatro condições (A, sem glossário nem filtro; B, com glossário; C, com filtro; D, com ambos) foram aplicadas às cinco faixas, num total de vinte execuções do Whisper large-v3.

As decisões tomadas depois do registro ficam listadas aqui, com data e motivo.

- **09/10, antes do teste de determinismo.** O critério "saídas idênticas" foi interpretado como texto e tempos idênticos, já que o WER e os termos críticos dependem apenas do texto. Diferenças apenas nas casas decimais das probabilidades seriam registradas sem acionar as repetições previstas.
- **09/10, durante a construção do caderno de medição.** Dois ajustes de leitura da saída do modelo, que não alteram as regras do desenho. Os pronomes enclíticos que o Whisper devolve como peças separadas ("-se", "-nos") passaram a ser reunidos à palavra anterior, e a marcação `[...]` passou a ser retirada sem inserção de espaço, aplicação literal da regra "`[...]` é removido". O primeiro ajuste foi feito depois de constatada a diferença entre o texto completo e as palavras do JSON, e o segundo, depois de identificado o caso "prostitu[...]ção" (seção 7).
- **09/10, na leitura do WER.** A taxa global foi recalculada sem a faixa 05, como verificação exploratória não prevista no desenho (seção 6).
- **09/10, durante a escuta dirigida.** Dentro da categoria 2 (fala real deformada), a pesquisadora passou a distinguir nas observações os casos "sem relação" dos casos com "relação reconhecível" entre o texto da máquina e a fala.
- **13/10, depois da escuta dirigida.** A categoria de cinco trechos (7, 16, 17, 27 e 31) foi revista depois da conferência dos JSON, com a classificação original preservada nas observações de cada trecho.
- **13/10, escuta complementar.** Os três segmentos "Aplausos." da faixa 01 (condição A), que os critérios da escuta dirigida não selecionaram, foram escutados à parte (seção 4).

## 2. Ambiente e execução

- As execuções foram feitas no Google Colab, com GPU Tesla T4, Python 3.13.15, openai-whisper 20250625, noisereduce 3.0.3, librosa 0.11.0, numpy 2.1.3 e torch 2.11.0. A medição foi feita em CPU, com jiwer 4.0.0 e pandas 2.2.3. As versões de cada execução estão gravadas no próprio JSON.
- O Python do Colab passou de 3.13.16 (fase 2) para 3.13.15 (09/10) e voltou a 3.13.16 (13/10), sem aviso, o que justifica o registro das versões em cada saída. O relógio do Colab segue o horário UTC, três horas à frente do horário de Brasília.
- O teste de determinismo (condição A, faixa 04, duas execuções) produziu saídas idênticas até a última casa decimal das probabilidades. Pela regra do desenho, cada condição rodou uma vez. O teste cobriu apenas um caso, e a repetição nos trechos em que o modelo recorre ao sorteio depende da semente fixada, sem ter sido verificada diretamente.
- As vinte execuções levaram cerca de meia hora. A primeira execução da sessão levou 16 segundos, e a repetição idêntica, 9, diferença atribuída ao aquecimento da GPU. Os tempos de processamento variaram muito mais do que as durações dos áudios (a faixa 05 levou 31 segundos na condição A e 123 na condição C), porque dependem da quantidade de texto produzida e das novas tentativas com sorteio.

## 3. A entrada do modelo e o filtro

- Os modelos receberam a soma dos canais dividida por dois, conforme a decisão da fase 2, reamostrada para 16 kHz. A reamostragem descarta tudo acima de 8 kHz, o que nessas gravações atinge apenas o ruído da digitalização, mas constitui um segundo filtro implícito na entrada, ao lado da soma dos canais.
- Antes das execuções, a pesquisadora escutou o efeito do filtro no trecho da virada de página da faixa 03 (4:13 a 4:19). O chiado desapareceu, e os ruídos do papel continuaram presentes, mas atenuados e com timbre estranho, a ponto de não serem mais reconhecíveis como papel. O som de papel é de banda larga e sem altura definida, semelhante ao ruído de superfície, e o portão espectral corta as partes de seu espectro que se confundem com o ruído, deixando passar fragmentos metálicos, artefato conhecido como ruído musical (*musical noise*). O evento permanece como energia, mas perde a qualidade pela qual a escuta o reconhece.

## 4. As saídas do modelo

**Alucinação em loop.** Em cinco execuções, o modelo ficou preso numa frase e a repetiu ao longo de minutos.

- Faixa 05, condições A, B e D. "A CIDADE NO BRASIL", em maiúsculas, repetida 15 ou 16 vezes, a partir dos 25 segundos, durante a música de abertura, e se estende sobre o diálogo, que começa em 1:52, até 6:29 na condição A e até o fim da faixa nas condições B e D. Só a condição C escapou, com "E aí" repetido na parte musical e início da transcrição aos 111 segundos, coincidindo com a entrada da voz registrada na escuta cega (1:52).
- Faixa 01, condição B. O texto acompanha a fala até 1:29, passa por um trecho sem sentido que mistura português, inglês e caracteres árabes e, a partir daí, repete "Ação da Riqueza Nacional." oito vezes até o fim, frase derivada de "expansão da riqueza nacional".
- Faixa 02, condição C. "O fim do mar" repetido sete vezes.

O Whisper transcreve em trechos de 30 segundos e, por padrão, cada trecho recebe como contexto o texto do anterior, de modo que uma invenção num trecho difícil, como uma música sem fala, tende a se propagar pelos seguintes.

**Texto sem sentido.** Além dos loops, várias execuções produziram sequências que misturam português com espanhol, inglês, polonês, russo, árabe, hebraico, chinês e coreano, quase sempre sobre fala real (seção 9).

**Indicadores de confiança.** Nos segmentos "A CIDADE NO BRASIL", a probabilidade estimada de não haver fala é baixa e a confiança média é alta. Na faixa 02, condição A, ao contrário, o modelo transcreveu quase corretamente versos do poema ("Até o vento tem preguiça de ventar") em segmentos para os quais estimava mais de 60% de probabilidade de não haver fala. Os indicadores do próprio modelo erram nos dois sentidos.

**Instabilidade.** Os efeitos das variáveis não são fixos. Na faixa 05, o filtro sozinho evita o loop, mas filtro e glossário juntos não evitam. Na faixa 01, o glossário sozinho provoca o colapso, mas glossário e filtro juntos não provocam. As execuções são determinísticas, mas não estáveis, já que uma pequena diferença no ponto de partida leva a trajetórias inteiramente distintas.

**Convenção de legendagem.** Na faixa 01, condição A, o modelo escreveu "Aplausos." três vezes, em segmentos isolados (4:12,2, 4:55,2 e 5:27,3), convenção aprendida nos dados de treino, em que legendas costumam anotar sons. Esses segmentos não entraram na lista da escuta dirigida, por terem uma palavra só, e foram escutados à parte pela pesquisadora em 13/10/2026. Nos três casos soam aplausos, que começam no tempo marcado pelo modelo (4:12,2 e cerca de 5:27,5) ou já estão em curso nele (4:55,2). A transcrição de referência marca sete passagens de aplauso na faixa. Dois dos "Aplausos." do modelo correspondem a passagens marcadas (4:11 e 4:50), e o terceiro (5:27,3) corresponde aos aplausos e ao "muito bem!" do fim da faixa, que a transcrição de referência não registra, mas que a pesquisadora ouviu na escuta dirigida (trecho 8) e na escuta de 13/10. O modelo de fala não escreveu nenhum aplauso onde não havia aplauso. *Correção de 13/10/2026: a primeira versão deste parágrafo afirmava que os três "Aplausos." correspondiam a passagens marcadas na referência.*

## 5. Normalização e coringa

As regras da seção 5 do desenho foram implementadas no caderno de medição e conferidas na seção 3.1 do caderno, que mostra o contexto de cada um dos vinte coringas. Nos casos de dúvida, a palavra duvidosa saiu com a marcação, e nos casos de palavra perdida, a palavra anterior foi preservada. As funções foram verificadas antes da medição com casos de resposta conhecida (seção 4.1 do caderno) e reproduzidas em `src/medicao.py`, onde nove testes automáticos (`tests/test_wer.py`) conferem cada regra.

Uma limitação do método ficou evidente. Quando a máquina escreve texto inventado no lugar de fala real, o alinhamento tende a contar cada palavra inventada como substituição, porque uma troca custa menos que uma omissão somada a uma inserção. O WER não distingue a palavra mal ouvida da palavra inventada, e por isso o loop da faixa 05 aparece como omissões e substituições, e não como inserções.

## 6. Taxa de erro de palavra

| Faixa | A | B | C | D |
|---|---|---|---|---|
| 01 | 26,0% | 66,8% | 17,6% | 20,7% |
| 02 | 48,9% | 25,8% | 56,3% | 46,8% |
| 03 | 8,9% | 20,9% | 5,8% | 19,2% |
| 04 | 22,4% | 22,4% | 25,9% | 24,1% |
| 05 | 78,5% | 95,7% | 25,1% | 95,7% |
| **Global** | **36,9%** | **49,8%** | **22,3%** | **43,3%** |

A taxa global soma os erros de todas as faixas e divide pela soma das palavras de referência (1.900, sem contar os coringas). A decomposição em substituições, omissões e inserções está em `resultados/fase3/medidas/wer_por_faixa.csv`.

- **A decomposição distingue fenômenos opostos.** Na faixa 05 (A, B e D), há de 325 a 409 omissões e nenhuma inserção, ou seja, a máquina deixou de escrever a fala. Na faixa 01 (B), 202 omissões correspondem ao colapso depois de 1:29. Nas faixas 01 e 02 (A), as 54 e 67 inserções correspondem a texto produzido a mais. Taxas semelhantes podem resultar de silêncio indevido ou de invenção.
- **Glossário (B contra A).** A taxa global piora de 36,9% para 49,8%. O efeito não é uniforme. Na faixa 02, a taxa cai de 48,9% para 25,8%, e as três palavras do prompt parecem ter mantido o modelo no registro do poema, enquanto na condição A ele derivava para texto sem sentido. Nas faixas 01, 03 e 05, a taxa piora.
- **Filtro (C contra A).** É a menor taxa global (22,3%), mas o ganho vem quase todo da faixa 05. Na verificação exploratória sem essa faixa, a condição A fica em 23,2% e a C em 21,3%. Na faixa 02, o filtro piora a taxa (de 48,9% para 56,3%).
- **Faixa 04.** Com 58 palavras de referência, cada erro vale quase dois pontos percentuais, e as diferenças entre condições (22% a 26%) correspondem a uma ou duas palavras.
- **O que os números não autorizam.** Os totais globais são dominados por poucos eventos catastróficos, que dependem do ponto de partida do modelo. Os dados não sustentam que o filtro funciona ou que o glossário atrapalha, e sim que, nesse material, as duas intervenções mudam o resultado de forma grande e pouco previsível.

## 7. Termos críticos e palavras apostadas

A tabela completa está em `resultados/fase3/medidas/termos.csv`.

- **Termos contextuais.** "Pacaembu", "Dia do Trabalho", "sindicalização" e "Vera Cruz", ausentes da fala, não foram escritos em nenhuma condição, nem com o glossário sugerindo-os em todos os trechos. O risco de invenção por sugestão não se confirmou para esses termos.
- **Faixa 02.** "madrugada" foi mantida em todas as condições. "meio-dia" foi contada como substituída na condição A porque a máquina escreveu "Meio dia", sem hífen, e mantida com o glossário, que trazia a grafia hifenizada, de modo que o glossário corrigiu a grafia, e não o reconhecimento. "tardezinha" foi mantida em A e B e aparece uma vez inventada em D, dentro do loop "marinho o marinho tardezinha" (2:47). Das palavras apostadas, coxilha, cinamomos, guaipeca e treval foram trocadas na condição A, e só cocoricoca foi mantida. Na condição B, cinamomos, cocoricoca e guaipeca foram mantidas, embora nenhuma estivesse no glossário. "treval" foi trocada em todas as condições.
- **Faixa 03.** "mal necessário" (três ocorrências) e "prostituição" (quatro) foram mantidos em todas as condições. A ocorrência de "prostituição" classificada como inventada aos 3,8 segundos nas quatro condições decorre da marcação da referência ("prostitu[...]ção"), em que a retirada de `[...]` deixa a forma "prostitução", e a escuta dirigida confirmou o pulo no meio da palavra. A segunda ocorrência inventada da condição B (2:31) é real e resulta da repetição de uma frase.
- **Faixa 04.** "surdo" e "tamborim" foram mantidos em todas as condições. "batucada" se perdeu nas duas condições com filtro, primeiro caso em que o filtro custa um termo crítico.
- **Faixa 05.** Nas condições A, B e D, todos os termos falados (Dom Aires Correia, batel, Cabral e Portugal) foram omitidos, por causa do loop, embora as condições B e D trouxessem esses nomes no glossário. Na condição C, "Portugal" foi mantido nas duas ocorrências, e os demais foram trocados ("Vem doar-lhe as correias" no lugar de "Dom Aires Correia").

## 8. Medidas complementares

- **Hesitações.** As três marcações `{fala: …}` da faixa 01 foram apagadas pela máquina em todas as condições. A primeira é o rastro da interrupção da leitura pela plateia, quando Vargas começa "Torna...", é interrompido por aplausos inesperados e recomeça "Torna-se inadiável". A transcrição devolve o texto lido, e não a fala proferida, e apaga a marca da interação com a multidão. O acerto contado para "da" é um efeito do alinhamento, que atribuiu ao falso começo o "da" da frase corrigida.
- **Grafia numérica.** A única divergência com algarismos é "33" transcrito como "36" nas condições C e D, erro de reconhecimento, e não de notação. O modelo escreveu os números em algarismos, como a convenção da referência, e a regra de não converter números não produziu erros artificiais.

## 9. Escuta dirigida

Os critérios da seção 8 do desenho selecionaram 31 trechos, escutados pela pesquisadora em 09/10/2026, em dois tempos, primeiro sem e depois com a leitura do texto da máquina.

- **Nenhum trecho foi classificado na categoria 1** (fala real ausente da referência). Em nenhum momento o texto acrescentado pela máquina apontou para algo que a transcrição de referência tivesse deixado passar.
- **Vinte trechos receberam apenas a categoria 2** (fala real deformada), a maioria marcada como "sem relação" nas observações, ou seja, texto sem ligação reconhecível com a fala que soa no trecho. Dois outros receberam a categoria 2 combinada com outra, de forma hesitante (trechos 9 e 26).
- **Cinco trechos são repetições** (categoria 3) de frases ditas em outro momento ou duplicadas no mesmo ponto, e um sexto combina repetição e texto sobre música (trecho 31, "Silêncio" repetido sobre a música de 4:37 da faixa 05).
- **Um trecho é texto sobre som não verbal** (categoria 4), o início musical da faixa 05, onde a máquina escreveu "A CIDADE NO BRASIL" (A) e "E aí" (C).
- **Um trecho é texto sobre ruído de superfície** (categoria 5), o fim da faixa 03, onde soam apenas o chiado e o giro do disco.
- **Um trecho é efeito da marcação da referência** (categoria 6), o "prostitu[...]ção" da faixa 03.

O resultado contrasta com a fase 2, em que o espectrograma levou a escuta a perceber o zumbido da faixa 05, não registrado na escuta cega. No reconhecimento de fala, o texto acrescentado pela máquina não indexa nada que a escuta não tenha registrado, e funciona como ruído com forma de linguagem.

Os critérios da escuta dirigida não captam as invenções que o alinhamento contou como substituição, como a maior parte do loop "A CIDADE NO BRASIL", conforme a limitação registrada na seção 5. As marcações de tempo das palavras inventadas mostraram-se pouco confiáveis, e a escuta foi feita com três segundos de folga antes e depois de cada trecho.

## 10. Confronto com as expectativas

Confronto item por item com [`../fase1/05_expectativas.md`](../fase1/05_expectativas.md).

- **Pior desempenho na faixa 04.** Contrariada. As piores faixas na linha de base são a 05 (78,5%), pelo loop, e a 02 (48,9%), a de voz mais fraca em relação ao ruído e de limite de frequência mais baixo do corpus, como registrado no diário da fase 2. A faixa 04 fica em 22,4%. A aposta de que o modelo inventaria palavras nos trechos só de percussão encontra apoio parcial no final da faixa ("E assim o tamborim", repetição) e em "aqui aqui aqui" (condição D).
- **Melhor desempenho na faixa 03.** Confirmada (8,9% na condição A).
- **Troca de nomes próprios, sobretudo Dom Aires Correia.** Confirmada na única condição em que a faixa 05 foi transcrita (C), com "Vem doar-lhe as correias".
- **Texto inventado, principalmente na faixa 02.** Confirmada para a faixa 02, que concentra sequências sem sentido na condição A, mas as invenções mais extensas ocorreram nas faixas 05 e 01.
- **Perda das palavras regionais da faixa 02 e de "batel".** Confirmada na linha de base para coxilha, cinamomos, guaipeca e treval, contrariada para cocoricoca, e confirmada para batel.
- **O glossário não melhoraria a taxa de erro geral.** Confirmada de forma mais forte do que a aposta, já que a taxa global piorou, com a exceção da faixa 02.
- **O filtro retiraria ruídos que são sons com sentido.** Confirmada pela escuta do papel da faixa 03, e não mensurável pelo WER, que considera apenas palavras. Pelo WER, o filtro produziu a menor taxa global, sobretudo por ter evitado o loop da faixa 05.

## 11. Limitações

- Cada condição rodou uma vez, e a instabilidade observada indica que as diferenças entre condições podem refletir a trajetória de cada execução mais do que o efeito da variável.
- O WER não distingue invenção de erro de reconhecimento, e os critérios da escuta dirigida, baseados no alinhamento, não captam as invenções contadas como substituição.
- A faixa 04 tem poucas palavras de referência, e sua taxa é instável.
- Marcações da referência podem produzir divergências que não são erro da máquina, como no caso "prostitu[...]ção".
- As marcações de tempo das palavras inventadas não são confiáveis.

## 12. Implicações para as fases 4 e 5

- Os indicadores de confiança do Whisper não podem ser tratados como garantia pela camada de linguagem da fase 5, e o dossiê precisa sinalizar os loops e as sequências sem sentido como invenções, e não como transcrição.
- O texto acrescentado pelo reconhecimento de fala não serviu como indicação de onde escutar. A expectativa de que a máquina aponte para o que a escuta não registrou fica transferida para os detectores de eventos sonoros da fase 4.
- Os três "Aplausos." escritos pelo modelo de fala, confirmados pela escuta, serão comparados com as passagens de aplauso da referência e com os rótulos dos detectores da fase 4. O terceiro deles indicou um aplauso que a transcrição de referência não registra, caso a ser examinado à luz do critério de surpresa da fase 1.
- O início musical da faixa 05 (0:00 a 1:51), onde a transcrição inventou texto em três condições, é um ponto de comparação direto para os detectores de eventos.
- A escolha da transcrição que alimenta a fase 5, entre as quatro condições, precisa ser declarada e justificada.
