# Diário da fase 5 · Síntese e restrição

Trabalho iniciado em 30/10/2026, registrado nos cadernos [`fase5a_entradas.ipynb`](fase5a_entradas.ipynb) (montagem das entradas) e [`fase5b_dossies.ipynb`](fase5b_dossies.ipynb) (chamadas, dossiês e medidas). As entradas, os registros das chamadas, os dossiês e as tabelas das medidas estão em [`resultados/fase5/`](../../resultados/fase5/).

As leituras foram feitas pela pesquisadora com apoio do Claude (Anthropic), conforme declarado no projeto. A leitura dos dossiês e a escuta de conferência, registradas em [`02_leitura_e_escuta.md`](02_leitura_e_escuta.md), foram feitas por ela antes de ver as medidas automáticas.

## 1. Desenho experimental e decisões posteriores

O desenho experimental e as expectativas foram fechados em 02/11/2026 ([`01_desenho_experimental.md`](01_desenho_experimental.md)), antes de qualquer chamada ao LLM com dados do corpus. O modelo escolhido foi o `gemini-3.8-flash`, com temperatura e demais parâmetros no valor padrão e saída em JSON segundo um esquema. Cada faixa foi enviada três vezes, num total de quinze chamadas, além de uma chamada de teste com dados inventados.

As decisões tomadas depois do registro ficam listadas aqui, com data e motivo.

- **02/11, na montagem das entradas.** Três pontos que o desenho não detalhava foram fixados no caderno 5a. Cada arquivo de entrada passou a trazer uma legenda que descreve, sem interpretar, o que é cada campo e como os sinais foram calculados, para que o LLM soubesse o que estava lendo, e a pesquisadora leu a legenda antes da execução, sem alterações. Na divergência entre transcrições, contam as palavras da condição C cujo tempo tem algum trecho em comum com o intervalo do segmento. E os segmentos sem texto não recebem os sinais de repetição e de divergência, mas podem receber os outros dois.
- **02/11, na construção do caderno 5b.** O esquema da saída passou a limitar os motivos e os graus às listas da seção 5, de modo que a própria API só aceitasse esses valores. As medidas foram transcritas para o código com quatro leituras explícitas. O intervalo das fontes, na medida de invenção, vai do menor início ao maior fim das fontes citadas. A restrição procura palavras iniciadas pelos termos da lista (“tristeza” conta como “triste”). O grau esperado fica em branco quando as fontes formam uma combinação que a regra não prevê, como um segmento de fala sem sinal, e essa indicação sai do cálculo da coerência. E duas indicações de chamadas diferentes correspondem quando têm o mesmo motivo e algum tempo em comum.
- **02/11, na instalação.** A versão fixada da biblioteca `google-genai` (2.34.0) exige uma versão do `google-auth` diferente da que o próprio Colab usa, e o conflito poderia afetar a conexão com o Drive e com os Secrets. O caderno passou a usar a versão já instalada no Colab (2.12.1), que aceita o esquema da saída, e a versão fica gravada em cada chamada.
- **02/11, no teste de funcionamento.** As tentativas foram recusadas pelo servidor por sobrecarga (erros 503 e 504), e uma delas ficou mais de oito minutos sem resposta, porque a biblioteca, por padrão, não tem tempo limite. Cada tentativa passou a ter um limite de 5 minutos, registrado nos parâmetros de cada chamada. Isso não altera o que o modelo recebe nem como responde.
- **03/11, na camada de acesso.** As tentativas do teste esgotaram a cota da camada gratuita (erro 429), que, para este modelo, é de 20 chamadas por dia e por projeto, contadas também as recusadas por sobrecarga. Com esse limite, as dezesseis chamadas da fase caberiam num dia apenas se nenhuma falhasse. A pesquisadora passou à camada paga (nível 1, com crédito pré-pago), alternativa prevista na seção 2 do desenho, sem mudar modelo, parâmetros, instrução ou entradas. Na camada paga, o conteúdo enviado não é usado pelo Google para aprimorar seus produtos. O caderno passou a parar na hora diante de um erro de cota e a esperar 2 minutos, em vez de 1, entre as tentativas recusadas por sobrecarga.
- **03/11, antes da escuta de conferência.** Ficaram fora da conferência da seção 8 do desenho os três eventos que ocupam a faixa inteira (1.13 e 3.5, ruído de superfície ao longo da faixa, e 5.14, zumbido em toda a faixa). Com eles, toda indicação teria tempo em comum com algum evento, e a lista da escuta ficaria vazia de antemão. É o mesmo tratamento que a fase 4 deu às classes sempre presentes.
- **03/11, na ordem da leitura.** A seção 8 do caderno 5b, com as medidas, só foi executada depois da leitura dos dossiês, para que a leitura não fosse orientada pela conferência automática. O formulário seguiu a ordem escuta, leitura e nova escuta, porque o primeiro tempo da escuta só é cego se vier antes da leitura do dossiê.
- **12 e 13/11, durante a leitura.** Três critérios foram fixados no primeiro bloco em que se mostraram necessários e aplicados a todos os seguintes ([`02_leitura_e_escuta.md`](02_leitura_e_escuta.md), parte 2). A segunda escuta (parte 3) foi refeita em 13/11, porque a primeira versão foi feita, por engano, com a faixa 01.

## 2. Ambiente e execução

- As chamadas foram feitas no Google Colab, em CPU, em 03/11/2026, com Python 3.13.18, pandas 2.2.3 e google-genai 2.12.1. A API informou a versão `gemini-3.8-flash` em todas as chamadas, e todas terminaram normalmente, sem nenhuma recusa. As seções de leitura dos registros e de medidas foram executadas de novo em 13/11, sem chamadas novas.
- Os pedidos enviados são idênticos, palavra por palavra, ao que o código produz a partir das entradas gravadas, e a instrução de sistema é idêntica ao anexo A do desenho, o que um teste automático confere.
- O tempo de resposta variou de 25 a 264 segundos, com média de 65. O tempo de raciocínio também variou muito para a mesma entrada. Na faixa 04, a primeira chamada usou 35.698 tokens de raciocínio e levou 264 segundos, perto do limite de 5 minutos, e a terceira usou 2.936 tokens e levou 25 segundos.
- As quinze chamadas somaram 142.233 tokens de entrada, 13.203 de saída e 118.189 de raciocínio, com custo equivalente de US$ 0,60. A maior parte do custo vem do raciocínio, que o modelo faz antes de responder e que não aparece na resposta.

## 3. A entrada do LLM

- Cada faixa foi enviada com três blocos, identificados apenas pelo número da faixa e pela duração. A fala trouxe os 196 segmentos da condição A, 74 deles com algum sinal. O PANNs trouxe 224 intervalos e o CLAP, 87, da faixa 01 à 05 respectivamente 41, 21, 27, 9 e 126 do PANNs e 2, 2, 3, 1 e 79 do CLAP.
- Nas faixas 01 a 04, os atratores do CLAP ocupam o alto da lista em quase todas as janelas, e restam de um a três itens por faixa. Nessas faixas, a entrada se compõe quase só da fala e do PANNs.
- A retirada dos rótulos onipresentes do PANNs vale rótulo por rótulo. Nas faixas em que “Speech” saiu, permanecem “Male speech, man speaking” e “Narration, monologue”, que somam 33 intervalos na faixa 05. A música chega fragmentada (18 intervalos de “Music” na faixa 02 e 29 na faixa 05), porque a probabilidade oscila em torno do limiar.
- O loop “A CIDADE NO BRASIL” da faixa 05 só se torna visível pelos sinais calculados. Os 15 segmentos do loop receberam o sinal de repetição, apenas um recebeu indicação de ausência de fala e nenhum recebeu baixa confiança, de modo que os indicadores do próprio Whisper mostram um modelo seguro do que escreveu.
- Os rótulos sem som correspondente na escuta dirigida da fase 4 (categoria 4), como “Owl”, “Cattle, bovinae” e “Gunshot, gunfire”, entraram sem nenhuma marca, já que o LLM não recebeu as escutas.

## 4. O teste de funcionamento

A chamada com dados inventados respondeu no formato do esquema, com 5 indicações, todas com fontes existentes, tempos iguais aos das fontes e graus segundo a regra. O segmento sem sinal não foi indicado. Os três segmentos com o mesmo texto receberam três indicações separadas, cada uma com um motivo diferente (ausência de fala, repetição e baixa confiança), sem que nenhuma frase os tratasse como sequência. As frases já mostravam o padrão que se repetiria no corpus, com uma primeira parte que relata o registro (“O detector PANNs atribuiu probabilidade máxima de 0,72 ao rótulo Dog”) e uma segunda que traduz o rótulo num som a verificar (“latidos”).

## 5. Conformidade, invenção e restrição

As 98 indicações das quinze chamadas estão conformes, nenhuma cita identificador inexistente ou tem intervalo fora das fontes citadas, e nenhuma frase usa os termos da lista (caderno 5b, seções 8.1 a 8.3). A conformidade de motivo e de grau dependia pouco do modelo, porque o esquema só aceitava os valores das listas. O resultado de invenção, ao contrário, dependia inteiramente dele. A instrução pedia que o início e o fim de cada indicação ficassem dentro do intervalo das fontes, e o modelo copiou esses tempos em todas as indicações.

## 6. Grau de apoio

Os 97 graus que a regra permite avaliar seguem a regra (seção 8.4). A indicação fora da regra reúne onze segmentos de fala da faixa 01 (3:29 a 3:59, chamada 2), combinação que a regra não prevê, com grau médio.

A coerência mostra que o modelo aplicou a regra, e não que o som está presente. Na escuta dirigida da fase 4, a primeira chamada alcança 7 dos 13 trechos sem som correspondente (categoria 4) e 10 dos 17 em que o rótulo nomeava um som presente (categoria 3), proporções parecidas. “Owl”, a 0,60, recebeu grau alto, como manda a regra, num trecho em que a escuta não encontrou nenhuma coruja. A palavra “confiança” foi evitada no desenho por esse motivo, e o resultado confirma a necessidade da distinção.

## 7. Estabilidade

Das 98 indicações, 63 (64%) têm correspondente nas outras duas chamadas, com o mesmo motivo e algum tempo em comum (seção 8.5). A proporção vai de 45% na faixa 02 a 100% na faixa 03, cujas três chamadas produziram as mesmas quatro indicações. O número de indicações por chamada variou pouco (de 10 a 13 na faixa 01, de 3 a 4 na faixa 04), e a distribuição dos motivos também. A temperatura padrão não produziu dossiês muito diferentes entre si, ao contrário do que a expectativa 5 previa.

Os motivos mais usados foram “coincidência entre fontes” (32), “evento sonoro apontado” (24) e “rótulo isolado” (23). “Repetição na transcrição” aparece uma única vez nas quinze chamadas, na faixa 01, e nunca na faixa 05, em que o loop ocupa quinze segmentos.

## 8. Cobertura

Três dos 44 eventos de referência ocupam a faixa inteira e são alcançados por qualquer indicação. Sem eles, a primeira chamada alcança 23 de 41 eventos (56%), e as três chamadas juntas, 24 (seção 8.6).

Os eventos não alcançados formam um conjunto coerente. São as pausas e dois aplausos da faixa 01, as três viradas de página da faixa 03, o surdo, o tamborim, os dois anúncios e os pulos do disco na faixa 04 e, na faixa 05, as três passagens de vento, a música de suspense e o salto de intensidade no anúncio da terra avistada. São sons que nenhum detector rotulou com força, ou que só a escuta, atenta à duração, à intensidade e à materialidade do disco, registrou.

Nas escutas dirigidas, a primeira chamada alcança 9 dos 31 trechos da fase 3, entre eles 6 dos 22 de fala real deformada, e 17 dos 34 trechos da fase 4.

## 9. Faixa 05 e a escuta cega

A medida da seção 8.7 conta como alcançada a passagem que tem algum tempo em comum com uma indicação, mesmo que a indicação trate de outra coisa, e a leitura do conteúdo muda o quadro.

- A música da abertura (0:04 a 1:03), a voz com música (1:52 a 2:49) e os gritos com música (5:04 a 7:21) são indicados, nas três chamadas, por coincidências entre a fala, o PANNs e o CLAP.
- O ruído da superfície do disco na abertura aparece numa das três chamadas, pela descrição do CLAP.
- O vento não é indicado em nenhuma das três passagens em que soa sozinho ou com música.
- As vozes femininas (2:50 a 3:14) só são alcançadas por uma indicação de “Owl” e “Hoot”, o som metálico com batidas (3:52 a 4:08) por uma indicação de “Cattle, bovinae” e “Moo”, e os passos (4:20 a 4:27) e o vento com ruído (4:28 a 4:37) por uma indicação de “ocean waves”, de 4:26 a 4:28.
- Dos 15 segmentos do loop, a primeira e a segunda chamadas citam dois, e a terceira, três, sempre dentro de uma “coincidência entre fontes”, em frases que registram a repetição ao lado de “Music”, de “a church bell” ou de “Bee, wasp, etc.”. Nenhuma frase trata a repetição como possível invenção da transcrição.

O modelo indica onde os detectores concordam, mas não alcança, pelo conteúdo, os sons que a escuta cega registrou e que os detectores nomearam de outro modo ou não nomearam.

## 10. Leitura dos dossiês

A pesquisadora leu as 32 indicações dos cinco dossiês ([`02_leitura_e_escuta.md`](02_leitura_e_escuta.md)). Nenhuma frase foi marcada como interpretação, e nenhuma afirma, por conta própria, a presença de um som. Sete ficaram como dúvida, por tomarem um som como dado ao pedir que se verifique outra coisa sobre ele (“a clareza da voz”, “as palavras efetivamente proferidas”, “o conteúdo musical”). Em quatro, a pesquisadora registrou o movimento contrário, de ceticismo em relação ao rótulo, como na frase da faixa 01 que pede para “verificar que características acústicas motivaram essas atribuições”, a propósito de “Sheep” e “Bleat”.

Parte do que poderia parecer interpretação do LLM vem das categorias dos modelos anteriores. O “canto” da faixa 01 (indicação 2) é a tradução de “women singing”, uma das descrições do CLAP escritas na fase 4, e o Gemini ainda abriu a alternativa “ou sobreposição de vozes”.

## 11. Escuta de conferência

Uma única indicação ficou fora de todas as escutas anteriores, a da faixa 03, de 5:27,0 a 5:28,7, por divergência entre as duas transcrições do Whisper. Na condição A, o modelo escreveu “por indirviço dos corpos,”, e na condição C, “por indivíduos do sexo”. No primeiro tempo, sem a indicação, a pesquisadora ouviu apenas fala com chiado ao fundo. No segundo, com a indicação, reconheceu que o locutor tropeça na leitura e diz algo como “por indivirço”, antes de seguir com “do sexo masculino”.

O tropeço não consta na transcrição de referência, em que a pesquisadora escreveu “indivíduos”, e é a primeira surpresa da fase, pelo critério da fase 1. A transcrição de referência foi mantida como estava, porque é a base das medidas publicadas na fase 3. A pesquisadora registrou que, ao transcrever, a atenção ao conteúdo e a busca de um texto coerente normalizaram o tropeço, que reforça a sua leitura das condições de gravação e de escuta, a de um locutor com dificuldade de leitura e de vocabulário diante de uma fala pública.

A surpresa não veio dos detectores de eventos, e sim do desacordo entre duas transcrições do mesmo modelo, que o caderno 5a transformou em sinal.

## 12. Confronto com as expectativas

| Expectativa registrada em 02/11 | Resultado |
|---|---|
| 1. O LLM interpretaria, afirmaria a presença de sons, nomearia o que o som seria e atribuiria graus fora da regra | Não se confirmou. Nenhuma interpretação marcada na leitura, nenhum termo da lista, nenhuma afirmação de presença por conta própria e todos os graus avaliáveis segundo a regra. A tradução do rótulo num som a verificar foi considerada pela pesquisadora como não interpretativa. |
| 2. Criaria indicações sem fonte, com identificadores inexistentes e tempos fora das fontes | Não se confirmou. Nenhuma das 98 indicações. |
| 3. Não trataria o loop da faixa 05 como possível invenção da transcrição | Confirmou-se. Cada chamada cita dois ou três dos 15 segmentos do loop, sempre ao lado de outras fontes, e nunca como possível invenção. |
| 4. Na faixa 05, indicaria ruído de disco, música e sino, e não indicaria vento e passos | Em parte. Música sim, ruído numa das três chamadas, sino não (o tempo do som metálico só é alcançado por “Cattle” e “Moo”), vento não, passos só por coincidência de tempo com “ocean waves”. |
| 5. As três chamadas de cada faixa produziriam dossiês bem diferentes | Não se confirmou. 64% das indicações se repetem nas três chamadas, e na faixa 03 as três são idênticas. |
| 6. Surpresa genuína seria uma indicação com fonte válida de algo que nenhuma escuta registrou, ou o cumprimento integral da proibição sem indicações sem fonte | As duas condições ocorreram, o tropeço de leitura da faixa 03 e o cumprimento da proibição, sem nenhuma indicação sem fonte. |
| 7. Confirmação do esperado seria interpretação, indicações sem fonte, graus fora da regra, loop sem sinalização e, na faixa 05, acerto no genérico e falha no específico | Só em parte, no loop e na falha com os sons específicos da faixa 05. |

O modelo cumpriu quase integralmente as regras do protocolo, o que a pesquisadora não esperava. Cumprir as regras, porém, não o levou aos sons que só a escuta alcançou nas fases anteriores, e o grau de apoio, coerente com a regra, não distingue o som presente do rótulo sem correspondência.

## 13. Limitações

- Três chamadas por faixa, com um único modelo, numa única data. O Google pode mudar o modelo sem aviso, e a versão informada pela API fica registrada em cada chamada.
- O esquema da saída tornou a conformidade de motivo e de grau quase automática, e essa medida diz pouco sobre o modelo.
- As medidas de cobertura e de comparação com a escuta cega contam sobreposição de tempo, e não correspondência de conteúdo, o que a seção 9 mostra ser decisivo na faixa 05.
- A regra do grau de apoio não prevê combinações como vários segmentos de fala ou fontes diferentes sem coincidência no tempo.
- A leitura dos dossiês foi feita por uma única pessoa, e a escuta de conferência ficou restrita a uma indicação, porque as outras 31 tinham tempo em comum com escutas anteriores.
- Os preços usados no cálculo do custo vieram de uma fonte secundária, consultada em 02/11/2026.

## 14. Implicações para a fase 6

- O protocolo pode tratar o LLM como organizador das indicações dos modelos, e não como detector. Ele cita fontes, copia tempos e aplica regras explícitas com fidelidade, mas não acrescenta nada que os modelos anteriores não tenham registrado.
- A divergência entre transcrições do mesmo modelo, sob condições diferentes, mostrou-se um sinal útil para dirigir a escuta, e foi o único caminho para a surpresa desta fase.
- O dossiê deve declarar que grau de apoio não é presença, e que os sons de duração, intensidade e materialidade do disco (pausas, vento, viradas de página, pulos, saltos de intensidade) ficam, nesta configuração, inteiramente a cargo da escuta.
- A indisponibilidade do serviço e o limite da camada gratuita são parte das condições do protocolo. A demonstração da defesa deve contar com os registros das chamadas já gravados no repositório, que permitem refazer os dossiês e as medidas sem nenhuma chamada nova.
