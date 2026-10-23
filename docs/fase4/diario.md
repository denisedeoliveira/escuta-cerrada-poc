# Diário da fase 4 · Eventos sonoros

Trabalho iniciado em 19/10/2026, registrado nos cadernos [`fase4a_deteccao.ipynb`](fase4a_deteccao.ipynb) (detecção) e [`fase4b_comparacao.ipynb`](fase4b_comparacao.ipynb) (comparação). As saídas dos modelos estão em [`resultados/fase4/`](../../resultados/fase4/), e as tabelas da comparação, em [`resultados/fase4/medidas/`](../../resultados/fase4/medidas/).

As leituras foram feitas pela pesquisadora com apoio do Claude (Anthropic), conforme declarado no projeto. Toda interpretação que depende de escuta foi conferida por ela nos áudios, na escuta dirigida registrada em [`03_escuta_dirigida.md`](03_escuta_dirigida.md).

## 1. Desenho experimental e decisões posteriores

A tabela de eventos de referência foi fechada em 19/10/2026 ([`01_eventos_referencia.md`](01_eventos_referencia.md)), e o desenho experimental, em 20/10/2026 ([`02_desenho_experimental.md`](02_desenho_experimental.md)), ambos antes de qualquer execução dos detectores. Dois modelos (PANNs e CLAP) foram aplicados às cinco faixas, sem e com filtro, num total de vinte execuções.

As decisões tomadas depois do registro ficam listadas aqui, com data e motivo.

- **20/10, na construção do caderno de comparação.** Três pontos de leitura do desenho, que não alteram suas regras, foram explicitados no código. O ramo musical do AudioSet, que a seção 6 faz corresponder à classe "música", ficou sem os rótulos atribuídos a outras classes, de modo que os rótulos de sino (Bell, Church bell, Chime, Tubular bells) e de canto (Vocal music) contam apenas para o sino e para o canto, e sem o rótulo registrado à parte (Tambourine). Um rótulo que corresponde a mais de uma classe (Drum, ao surdo e ao tamborim, ou Crackle, ao ruído de disco e aos estalos) só entra no critério 1 da escuta dirigida quando nenhuma dessas classes está presente na janela. E, no CLAP, a tabela de eventos nomeados registra a melhor posição alcançada pela classe também quando ela fica fora das três primeiras, para que a distância entre a descrição e o apontamento possa ser lida.
- **20/10, antes da escuta dirigida.** Os critérios da seção 9 foram alterados para o CLAP, e o agrupamento dos trechos foi ampliado. Com a regra registrada, que conta como apontadas as três descrições mais semelhantes de cada janela, a lista chegaria a 4.831 itens, cobrindo cerca de 23 minutos, praticamente o corpus inteiro. Mesmo restrita à descrição em primeiro lugar, a lista ainda cobriria cerca de 21 minutos. O CLAP não indica se um som está presente, apenas ordena as descrições do vocabulário pela semelhança com o trecho, e por isso aponta três delas em toda janela, haja ou não algo que corresponda. Na faixa 03 com filtro, por exemplo, a palavra "surdo" ficou em primeiro lugar em 207 das 362 janelas, numa gravação em que só se ouve o policial lendo. Os critérios do PANNs foram mantidos como registrados. No CLAP, passaram a entrar apenas as janelas em que a mesma descrição fica em primeiro lugar com e sem filtro, e que atendem ao critério 1 ou ao critério 2. Itens da mesma faixa separados por até 5 segundos passaram a formar um só trecho, já que o agrupamento apenas por sobreposição dividiria a faixa 02 em 28 trechos de poucos segundos. A lista resultante tem 34 trechos, cerca de 6 minutos e meio. O excesso de apontamentos do CLAP passou a ser tratado como resultado (caderno 4b, seção 8), e não como lista de escuta.
- **21/10, durante a escuta dirigida.** Duas regras de aplicação das categorias, que o caderno de escuta não explicitava, foram fixadas no primeiro trecho em que se mostraram necessárias e aplicadas a todos os seguintes. Quando um trecho reúne rótulos diferentes, cada rótulo recebe a sua categoria (por exemplo, "Sheep: 3; Clicking: 4"), e a categoria 5 combina-se com a 3 quando o som já está presente no original e a filtragem o altera ou realça. A surpresa, pelo critério da fase 1, só pode ser afirmada na categoria 1, porque o critério se refere a um evento que não consta na tabela nem na dissertação. Um rótulo que dirige a escuta para uma qualidade de um evento já registrado, como o aplaudidor destacado do trecho 2, não conta como surpresa e fica descrito nas observações.
- **21/10, na preparação da escuta.** As seções 1 e 2 do caderno de detecção foram executadas de novo, em CPU, para carregar os áudios e tocar os trechos, e a escuta foi feita no próprio caderno, com uma célula para cada trecho, na versão original e na versão com filtro. Essa nova execução substituiu a saída da seção 1.2, que registrava a GPU e as versões da execução de 20/10, e essa saída foi restaurada a partir do histórico de revisões do Colab, para corresponder à execução que produziu os JSON. Os tocadores de áudio foram retirados da versão publicada.
- **21/10, nos testes automáticos.** Os testes da fase 3 dependem da biblioteca jiwer, que o caderno de comparação não instalava, e a primeira execução da seção 12 parou com erro. A instalação do jiwer foi acrescentada à célula dos testes.

## 2. Ambiente e execução

- A detecção foi feita no Google Colab, em 20/10/2026, com GPU Tesla T4, Python 3.13.15, panns-inference 0.1.1, torchlibrosa 0.1.0, transformers 5.20.1, noisereduce 3.0.3, librosa 0.11.0, numpy 2.1.3 e torch 2.11.0. A comparação foi feita em CPU, com pandas 2.2.3, e executada pela última vez em 23/10/2026, quando o Python do Colab já estava na versão 3.13.16. As versões de cada execução estão gravadas no próprio JSON.
- Os pesos do PANNs (`Cnn14_mAP=0.431.pth`) foram baixados do depósito dos autores no Zenodo. As versões recentes do PyTorch recusam por padrão o formato em que esses pesos foram salvos, e a leitura foi autorizada explicitamente no código, já que os pesos vêm da fonte oficial.
- O teste de determinismo (PANNs, faixa 04 sem filtro, duas execuções) produziu probabilidades idênticas, com diferença máxima igual a zero. Pela regra do desenho, cada execução rodou uma vez.
- Cada execução do PANNs levou menos de um segundo de processamento. As do CLAP levaram de 3,6 a 34,9 segundos, porque o modelo completa cada janela de 2 segundos até 10 segundos, repetindo o próprio trecho, antes de calcular a representação do áudio.

## 3. A entrada dos modelos

- Os modelos receberam a soma dos canais dividida por dois, como nas fases 2 e 3, reamostrada para 32 kHz (PANNs) e 48 kHz (CLAP). O filtro foi aplicado à faixa inteira, depois da reamostragem, e não a cada janela, de modo que a estimativa do ruído considera a gravação completa.
- As faixas foram divididas em 335, 201, 362, 64 e 441 janelas de 2 segundos, com passo de 1 segundo. A última janela de cada faixa foi ajustada para terminar no fim do arquivo, e a grade é a mesma nas quatro execuções de cada faixa (caderno 4b, seção 1.1), o que permite comparar os modelos janela a janela.

## 4. Eventos nomeados

A tabela evento a evento está em `resultados/fase4/medidas/eventos_nomeados.csv`, e a proporção por classe, em `nomeados_por_classe.csv`. A tabela de referência tem 44 eventos, que somam 53 componentes depois do desdobramento das classes compostas.

| Classe | PANNs sem filtro | PANNs com filtro | CLAP sem filtro | CLAP com filtro |
|---|---|---|---|---|
| aplauso | 7/8 | 0/8 | 0/8 | 0/8 |
| grito de plateia | 0/4 | 0/4 | 0/4 | 0/4 |
| tosse | 0/1 | 0/1 | 0/1 | 0/1 |
| fala | 5/5 | 5/5 | 4/5 | 4/5 |
| voz alterada | 0/1 | 0/1 | 0/1 | 1/1 |
| ruído de disco | 1/8 | 0/8 | 7/8 | 5/8 |
| estalos regulares | 0/1 | 0/1 | 1/1 | 1/1 |
| pulos | sem correspondência | sem correspondência | 2/2 | 2/2 |
| papel | 0/3 | 0/3 | 0/3 | 0/3 |
| surdo | 0/1 | 0/1 | 0/1 | 1/1 |
| tamborim | 0/2 | 0/2 | 1/2 | 1/2 |
| música | 5/5 | 3/5 | 5/5 | 5/5 |
| vento | 0/5 | 0/5 | 5/5 | 5/5 |
| canto | 0/1 | 0/1 | 1/1 | 1/1 |
| sino | 1/1 | 0/1 | 0/1 | 0/1 |
| passos | 0/1 | 0/1 | 1/1 | 0/1 |
| zumbido | 0/1 | 0/1 | 1/1 | 1/1 |

A pausa e a mudança de intensidade não têm correspondência em nenhum dos modelos.

- **Os dois modelos nomeiam coisas diferentes.** O PANNs nomeia sete dos oito aplausos da faixa 01 e nenhuma das cinco passagens de vento. O CLAP nomeia as cinco passagens de vento e nenhum aplauso, com "applause" entre o 4º e o 22º lugar. Nos aplausos, as três primeiras posições do CLAP ficam quase sempre com as descrições do disco ("the surface noise of an old record", "clicks of a scratched record", "a skipping record").
- **Ruído de disco.** O PANNs quase não nomeia o ruído que atravessa todas as faixas (1/8), porque os rótulos de chiado do AudioSet (Static, Hiss) ficam baixos. O CLAP o nomeia em sete de oito eventos sem filtro, mas a descrição correspondente fica em primeiro lugar em quase todas as janelas das faixas 01 a 04 (seção 9), e o acerto não distingue o evento de nenhum outro momento.
- **O que nenhum modelo nomeia.** As três viradas de página da faixa 03, os quatro "muito bem!" da faixa 01 e a tosse não foram nomeados por nenhum modelo, em nenhuma condição. "A page of paper being turned" ficou entre o 13º e o 25º lugar.
- **O acerto do CLAP depende da especificidade.** Um evento conta como nomeado no CLAP quando uma descrição da classe fica entre as três primeiras, o que nada diz sobre o restante da gravação. Com filtro, "a distorted voice" ficou em primeiro lugar na voz alterada (1.2), mas entrou entre as três primeiras em 191 janelas da faixa 01, 182 delas fora do evento. Na faixa 05 sem filtro, "women singing" entrou entre as três primeiras em 87 janelas, 72 delas fora do canto. Esses acertos não indicam discriminação. "Music", na mesma faixa, aparece entre as três primeiras em 210 janelas, e só 22 delas ficam fora dos eventos de música.

## 5. Efeito do filtro

- **O filtro apaga os aplausos para o PANNs.** Com filtro, o rótulo "Applause" fica abaixo de 0,01 nos oito eventos, e o sino deixa de ser nomeado. Dos 19 componentes nomeados pelo PANNs sem filtro, 11 deixam de sê-lo com filtro, e nenhum passa a ser nomeado só com filtro. A música da faixa 05 cai de 0,78 para 0,15 nos eventos 5.5 e 5.11.
- **Para o CLAP, o efeito é misto.** Com filtro, passam a ser nomeados a voz alterada (1.2) e o surdo (4.2, por "a bass drum"), e deixam de sê-lo dois eventos de ruído de disco (2.4 e 5.1) e os passos (5.9).
- **A escuta mostra o mecanismo.** O aplauso é um som de banda larga, sem altura definida, como o chiado que o filtro aprende a retirar. No trecho 2 da escuta dirigida, a versão filtrada reduz a plateia a um eco discreto e deixa sobressair um único aplaudidor, mais próximo, cujas palmas passam a soar como estalos regulares, que o PANNs nomeia "Clicking". Nos trechos 6 e 20, o aplauso e o chiado final se convertem em cliques que o modelo nomeia "Crunch". Nas faixas 02 e 03, o ruído musical que a filtragem produz, um fundo metalizado e constante, faz o PANNs apontar "Speech synthesizer" sobre a voz dos locutores em nove trechos dessas faixas e num da faixa 05. Na faixa 05, a versão filtrada apaga o vento e a música e deixa as vozes sobre um fundo vazio, que o CLAP nomeia "silence" em 169 das 441 janelas e "ocean waves" em 135. A música religiosa do início da mesma faixa, depois da filtragem, mal se reconhece como música e soa, na escuta, como algo arranhando num tom muito agudo.
- **Nos trechos de percussão e de pulos da faixa 04, com filtro, os rótulos principais passam a ser de fala e de boca** ("Speech", "Biting", "Chewing, mastication"), o que se repete na tosse da faixa 01 ("Chewing", "Whispering"). O que o filtro não reconhece como voz e não remove como ruído chega aos detectores como restos que eles leem como boca.

## 6. Faixa 04 e a taxonomia de Almirante

- **PANNs.** Nenhum rótulo de tambor chega a 0,3 nos trechos instrumentais. No trecho do surdo (4.2) sem filtro, os rótulos de maior probabilidade média são fala, música, "Inside, small room", "Sizzle" e "Frying (food)", ou seja, o modelo aproxima o trecho de uma textura de fritura, e não da batida grave do instrumento. Com filtro, aparece "Heart sounds, heartbeat". Nos tamborins, o modelo nomeia "Music" e "Musical instrument", e o nome mais próximo que encontra para o primeiro tamborim é "Wood block" (0,39 em 0:31). "Drum" e "Percussion" chegam apenas a indício (0,15 e 0,26), e "Tambourine", o homônimo do AudioSet, fica abaixo de 0,01. No segundo tamborim aparecem "Guitar" e "Plucked string instrument", com valores baixos.
- **CLAP.** A palavra de Almirante sozinha fica sempre mais perto do trecho do que a mesma palavra acompanhada da descrição escrita pela pesquisadora. "Tamborim" tem posição mediana 5 no primeiro tamborim sem filtro e 1 com filtro, enquanto "a tamborim, a small Brazilian frame drum played with a stick" fica entre o 13º e o 28º lugar. O mesmo vale para a batucada. A única exceção é "a surdo, a large Brazilian bass drum" no trecho do surdo com filtro (mediana 5), no mesmo trecho em que "a bass drum" sobe para o 4º lugar. Os distratores de percussão ("a tambourine", "a snare drum") ficam, em posição mediana, entre o 10º e o 26º lugar.
- **Uma palavra crua não é uma palavra conhecida.** "Surdo" sozinho fica em 7º e 9º lugar no próprio trecho do surdo e, ao mesmo tempo, em primeiro lugar na maior parte da leitura do policial com filtro (seção 9). "Tamborim" tem sua melhor posição justamente no primeiro tamborim. As duas palavras se comportam de modo diferente, e os dados não permitem dizer que o modelo conheça uma ou outra. Permitem dizer que o conhecimento sobre o instrumento, traduzido para o inglês, afasta o modelo do som em vez de aproximá-lo.
- **A escuta (trecho 22) confirma o nível em que o modelo nomeia.** O surdo e os tamborins aparecem como música e instrumento musical, no nível geral, sem nenhum dos nomes que Almirante enuncia. A taxonomia da gravação, que apresenta um a um os instrumentos da batucada, não tem correspondência na ontologia do AudioSet, e o nome dos instrumentos seguintes ao segundo tamborim não é audível, porque a gravação pula no momento em que Almirante os anuncia.

## 7. Aplausos e tosse da faixa 01

- **Três registros que não se recobrem.** A tabela de referência tem oito aplausos. O PANNs aponta aplauso em sete, com mais confiança nos do meio da faixa (0,81 no 1.3 e 0,82 no 1.8). O Whisper, na fase 3, escreveu "Aplausos." só três vezes, no fim da faixa (1.9, 1.10 e 1.12) e só na condição A. No 1.10, o PANNs quase não vê aplauso (0,10), e o Whisper escreve a palavra. A palavra escrita pelo Whisper parece seguir a convenção de legendagem que o modelo aprendeu com os dados de treino, e não a mesma operação de detecção do PANNs.
- **O aplauso do início.** O PANNs aponta aplauso nos primeiros seis segundos da faixa 01, antes da primeira fala, momento que nem a transcrição de referência nem a tabela de eventos registram. A pesquisadora reconheceu os aplausos ao reescutar o trecho, sem saber dizer se havia deixado de anotá-los ou se os havia confundido com o chiado do início. É o único trecho em que o critério de surpresa da fase 1 se cumpre (seção 10).
- **A tosse vira animal.** Nas janelas que cobrem a tosse (4:54 a 4:58), o PANNs aponta "Animal", "Crow" e "Caw", com valores baixos, e depois "Sheep" (0,57) e "Bleat" (0,41) na janela de 4:56 a 4:58. A escuta confirmou que a segunda parte da tosse soa ao longo do segundo 4:56, dentro dessa janela, e que o fim registrado na tabela (4:56,0) indica o segundo em que a tosse ainda soa. A categoria "Cough" existe no AudioSet e não aparece em nenhuma janela. Com filtro, os animais desaparecem e entram "Chewing", "Clicking" e "Whispering". No CLAP, "a man coughing" fica no 11º lugar sem filtro e no 21º com filtro.

## 8. Rótulos registrados à parte

- **Tambourine.** Abaixo de 0,01 no PANNs, e entre o 7º e o 13º lugar no CLAP, nos dois tamborins. A coincidência de nome não produziu nenhum apontamento.
- **Silêncio.** O PANNs só se aproxima de "Silence" (0,26) na última janela das faixas 01 e 03, e fica em zero nas pausas da fala sem filtro. A escuta dos trechos 6 e 20 mostrou que, nesses dois finais, há de fato silêncio completo, sem o ruído do disco (cerca de 3 segundos na faixa 01, depois do corte abrupto, e cerca de 2 segundos na faixa 03). O silêncio não vem da gravação, e sim do arquivo, que continua depois que o som do disco acaba. A afirmação da seção 6 do desenho experimental de que "nenhum trecho do corpus é silêncio acústico" precisa, por isso, dessa ressalva, e o desenho permanece como foi fechado.
- **Passos ou batida na porta.** Os dois modelos ficam do lado da interpretação registrada na escuta cega. No CLAP sem filtro, "footsteps" fica em 3º lugar nos passos (5.9) e "a door knocking", em 5º. "Door" e "Knock" ficam abaixo de 0,05 no PANNs.
- **Mar.** O PANNs dá zero para "Ocean" e "Waves, surf" na música de suspense (5.11). Sem filtro, "ocean waves" entra entre as três primeiras do CLAP em 16 janelas da faixa 05, nenhuma entre 4:38 e 5:03, e todas nas passagens de vento (1:13 a 1:20, 1:47 a 1:53, 3:20 a 3:43 e 4:23 a 4:26). Com filtro, a descrição se espalha pela faixa inteira e pela leitura do policial (241 e 154 janelas). O modelo não ouve mar onde a escuta cogitou o mar, e sim onde há vento.

## 9. O excesso de apontamentos do CLAP

A tabela completa está em `resultados/fase4/medidas/clap_frequencias.csv`.

- **Sem filtro, o CLAP escuta primeiro o disco.** Nas faixas 01, 02 e 04, "the surface noise of an old record" fica em primeiro lugar em 241 das 335 janelas, 199 das 201 e 63 das 64. Na faixa 03, divide o primeiro lugar com a fala (151 e 203 das 362 janelas). Na leitura do policial, "music" entra entre as três primeiras em 209 janelas, numa gravação sem música.
- **Com filtro, as palavras de Almirante tomam o lugar do disco.** "Surdo", sem descrição, fica em primeiro lugar em 154 janelas da faixa 01 e em 207 da faixa 03, e entra entre as três primeiras em quase todas. Na faixa 05 sem filtro, entra entre as três primeiras em 329 das 441 janelas. "Batucada" faz o mesmo em escala menor (106 janelas do discurso de Vargas). As cinco indicações de "surdo" que chegaram à escuta dirigida foram classificadas na categoria 4.
- **Uma ordenação sempre escolhe alguma coisa.** O CLAP não tem como responder que nenhuma das descrições oferecidas corresponde ao trecho. A regra do desenho, que conta como apontadas as três primeiras, fazia o modelo apontar alguma coisa em toda janela, e foi essa a razão da decisão de 20/10 (seção 1). Com filtro, a faixa 02 vira "footsteps" (52 janelas em primeiro lugar), e a faixa 05, "silence" e "ocean waves".

## 10. Escuta dirigida

Os 34 trechos foram escutados pela pesquisadora em 21 e 22/10/2026, em dois tempos, primeiro sem e depois com a leitura dos rótulos, e ouvidos também na versão filtrada quando o rótulo só aparecia nessa condição. O registro está em [`03_escuta_dirigida.md`](03_escuta_dirigida.md). A classificação de cada trecho foi discutida com o Claude durante a escuta, a partir do que a pesquisadora descrevia, e a decisão final coube a ela. Contando em separado cada rótulo ou grupo de rótulos classificado (57 no total), e contando duas vezes os seis que receberam duas categorias, a distribuição é a seguinte.

| Categoria | Rótulos ou grupos |
|---|---|
| 1. Som presente e não registrado | 2 |
| 2. Som registrado, fora dos tempos da tabela | 3 |
| 3. Som presente, com outro nome | 20 |
| 4. Nenhum som correspondente | 21 |
| 5. Efeito do filtro | 16 |
| 6. Outro | 1 |

- **Categoria 1.** Os aplausos dos primeiros segundos da faixa 01 (trecho 1), único caso de surpresa pelo critério da fase 1, e o silêncio completo do fim da faixa 03 (trecho 20), que é um traço do arquivo e não um evento da gravação.
- **Categoria 2.** A fala da faixa 05 entre 2:49 e 5:04, que a tabela não registra, embora soe o tempo todo (trecho 29), a fala de Almirante nos pulos finais da faixa 04 (trecho 22) e a música da faixa 05, que continua por baixo do vento depois do fim registrado (trecho 24).
- **Categoria 3.** É a mais frequente entre as correspondências e reúne os casos em que o modelo nomeia por outro nome um som que a escuta reconhece. O giro do disco da faixa 02 vira "Music" em seis trechos, porque é constante e marcado como uma batida. O vento forte vira "Vehicle" (trecho 25), e o vento com as vozes, "a crowd cheering and shouting" (trecho 29). A tosse vira "Sheep", o sino vira "Wind chime", o início do canto das moças vira "Bee" e "Insect", os estalos do início da faixa 04 viram "Tearing" (papel rasgado), um "aliii" agudo e prolongado vira "women singing", e o ruído do disco vira "a skipping record".
- **Categoria 4.** Quase metade dos rótulos não corresponde a nada que a escuta reconheça, entre eles todas as indicações de "surdo", os insetos da faixa 05 (com a ressalva de que o modelo pode responder ao zumbido elétrico, pouco audível), "Gunshot, gunfire", "Boat, Water vehicle", "Owl", "Moo" e "silence" sobre música ou vento.
- **Categoria 5.** Todos os "Speech synthesizer" (dez trechos), os "Crunch" dos trechos 6 e 20, o "Clicking" do trecho 2 e o "Tearing" do trecho 21, que a filtragem produz ou realça a partir de aplausos e estalos, e o "silence" da faixa 05 filtrada (trechos 28 e 29).
- **A surpresa de qualidade.** No trecho 2, o rótulo não apontou um evento novo, e sim uma qualidade de um evento já registrado, um aplaudidor destacado e regular dentro do aplauso 1.3, que a pesquisadora passou a ouvir depois da leitura de "Clicking". O critério da fase 1 não previa esse tipo de contribuição, que dirige a escuta para dentro do evento, e não para fora da tabela.
- **Correspondência dos tempos.** No trecho 29, os tempos anotados pela escuta coincidem, quase ao segundo, com os eventos da tabela (canto, vento, sino, passos e giro do disco), o que confirma a tabela de referência como base da comparação.
- **Alcance da cegueira.** A primeira escuta foi feita sem ler os rótulos de cada trecho, mas não foi inteiramente cega, porque alguns resultados das seções 4 a 9 do caderno de comparação já eram conhecidos (o "Sheep" da tosse, a fala da faixa 05, o vento ouvido como ondas). O trecho 5 registra isso explicitamente.

## 11. Confronto com as expectativas

Confronto item por item com [`../fase1/05_expectativas.md`](../fase1/05_expectativas.md).

- **Applause nos aplausos da faixa 01.** Confirmada sem filtro (7 de 8 eventos, máximo de 0,82), contrariada com filtro.
- **Drum, Percussion, Snare drum, Bass drum e Tambourine na faixa 04.** Contrariada. Drum e Percussion chegam apenas a indício (0,15 e 0,26, em 0:31), e Snare drum, Bass drum e Tambourine ficam abaixo de 0,01.
- **Na faixa 05, Hiss no início, Christian music, Wind nas três passagens de vento, Music of Latin America, Church bell, Walk, footsteps e Exciting music.** Contrariada em todos os rótulos. Nenhum passa de 0,03 no intervalo indicado. O modelo fica no nível genérico ("Music", com até 0,95) e nomeia o sino como "Chime" (0,31) e a música tradicional por instrumentos ("Guitar", 0,86, "Plucked string instrument", "Ukulele", "Strum"). Os rótulos de gênero existem no AudioSet e não foram usados neste material.
- **Fenômenos que nenhum modelo nomearia.** Confirmada para a virada de página e para o "muito bem!". Contrariada, com ressalva, para as mulheres cantando, que o CLAP põe em primeiro lugar no evento 5.6, embora a mesma descrição apareça em 72 janelas fora do canto. A variação de volume da faixa 05 não tem correspondência em nenhum modelo.
- **Surpresa genuína.** Os nomes das três partes do poema da faixa 02 estavam fora do alcance dos detectores, que não operam sobre palavras. O "mar" entre 4:38 e 5:03 não apareceu. O único caso de surpresa pelo critério declarado foi o aplauso do início da faixa 01.
- **Confirmação do esperado ("os rótulos acertarem o genérico e falharem no específico").** Confirmada em grande parte, com uma divisão entre os modelos. Fala e música são nomeadas pelos dois, o vento só pelo CLAP, e o tamborim (no PANNs), o folheio e o "muito bem!" falham.
- **O filtro retiraria ruídos que são sons com sentido** (expectativa sobre o reconhecimento de fala, retomada aqui). Confirmada de forma mais clara do que na fase 3. O filtro apaga os aplausos para o PANNs, apaga a música e o vento da faixa 05 e produz, a partir do que resta, sons que os modelos leem como voz sintetizada, cliques e silêncio.

## 12. Língua, ontologia e nomes

Observações reunidas para o artigo sobre as categorias dos modelos.

- **Dois tipos de falha.** Há sons que não têm nome na ontologia, como o surdo e o tamborim, que o modelo só pode aproximar de outra coisa ("Wood block", "Frying"). E há sons que têm nome e não o recebem, como a tosse, para a qual o AudioSet tem "Cough" e o modelo escolhe "Sheep", o papel, para o qual há "Rustle" e "Crumpling", e o aplauso no CLAP, cuja descrição está no vocabulário e perde para o ruído do disco.
- **O repertório dos nomes.** Diante de gravações de 1940, os modelos recorrem a um repertório de animais (ovelha, corvo, coruja, gado, abelha, mosca), de veículos (carro, barco), de guerra e de explosão ("Machine gun", "Gunshot", "Artillery fire", "Eruption", com valores entre 0,31 e 0,50, nas faixas 01 e 03) e de sons domésticos ("Frying", "Sizzle", "Rain on surface"). O ruído do suporte e a voz gravada nesse suporte são ouvidos por analogia com o que os dados de treino oferecem.
- **A fritura.** O chiado de fritura com que o PANNs descreve o trecho do surdo encontra um precedente na descrição do compositor Oscar Lorenzo Fernández, que em 1931 comparou os sons de uma máquina fonográfica com os de "uma cozinha frigindo ovos sincronizados" (Lorenzo Fernández, 1931). Os valores são baixos (0,05 e 0,04 em média), e a aproximação vale como achado sobre a forma de nomear, e não como apontamento do modelo.
- **A língua das descrições.** As descrições do CLAP estão em inglês, e o conhecimento da pesquisadora sobre os instrumentos, escrito em inglês, piora a posição dos termos (seção 6). As palavras portuguesas sem descrição se comportam como nomes vagos, que ficam perto de tudo ("surdo") ou de quase nada ("tamborim").
- **A música brasileira sem gênero.** A ontologia tem "Music of Latin America" e "Christian music", e o modelo não os usa. A música religiosa do início da faixa 05 recebe "Singing bowl" (0,35), e a música tradicional brasileira, "Guitar", "Ukulele" e "Strum".

**Referência citada nesta seção**

LORENZO FERNÁNDEZ, Oscar. Os discos e os músicos [entrevista]. *Correio da Manhã*, Coluna Música em Discos, Rio de Janeiro, 18 jan. 1931, p. 10. Disponível em: http://memoria.bn.gov.br/DocReader/089842_04/5538. Acesso em: 23 out. 2026.

## 13. Limitações

- Cada execução rodou uma vez, e o determinismo foi verificado apenas para o PANNs, numa faixa.
- As correspondências entre rótulos e classes (seção 6 do desenho) são aproximadas para a voz alterada ("Distortion") e para o papel ("Rustle", "Crumpling", "Tearing"), e a classe música foi ampliada ao ramo musical do AudioSet por uma regra declarada (seção 1).
- A posição do CLAP depende do vocabulário oferecido. Com outras descrições ou outro molde, as posições seriam outras, e o "nomeado" do CLAP mede proximidade relativa, e não presença.
- A janela de 2 segundos não localiza o som dentro dela, e um evento curto pode ser apontado numa janela vizinha à marcação da tabela, como no caso da tosse.
- A escuta dirigida não foi inteiramente cega (seção 10), e as categorias dos trechos longos (22 e 29) foram atribuídas rótulo a rótulo, com apoio nos tempos das janelas fornecidos durante a escuta.
- O zumbido elétrico da faixa 05 (5.14) é pouco audível, e a hipótese de que os rótulos de inseto respondam a ele não pôde ser verificada pela escuta.

## 14. Implicações para a fase 5

- A camada de linguagem não pode tratar a posição do CLAP como detecção. Um rótulo do CLAP só deve chegar ao dossiê quando for específico, ou seja, quando não aparecer também fora do evento, e as palavras de Almirante sem descrição devem ser tratadas como atratores.
- Os rótulos do PANNs sem filtro são a fonte mais confiável para aplausos, fala e música, e os rótulos de animais, veículos e armas, nesta faixa de valores, devem ser apresentados como nomes atribuídos pelo modelo, e não como sons presentes.
- A condição com filtro não deve alimentar o dossiê, porque produz rótulos que correspondem a alterações da própria filtragem (categoria 5).
- O dossiê deve manter separadas as três formas de indicação examinadas nesta fase, o evento novo (trecho 1), a qualidade de um evento conhecido (trecho 2) e o nome atribuído a um som presente (categoria 3).
- O início musical da faixa 05, ponto de comparação indicado na fase 3, recebeu do PANNs "Music" (até 0,89) e "Singing bowl". No CLAP sem filtro, as descrições em primeiro lugar nas 58 janelas da música religiosa (0:04 a 1:03) foram "surdo" (20), "music" (15) e "a church bell" (13). Nenhum dos detectores produziu ali o equivalente às invenções do Whisper, mas o CLAP também não deixa de nomear alguma coisa.
