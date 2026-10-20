# Desenho experimental da fase 4

Registro fechado em 20/10/2026, antes de qualquer execução dos detectores de eventos sonoros sobre o corpus. As escolhas abaixo valem para todas as execuções e comparações da fase. Qualquer alteração posterior será registrada no diário da fase, com data e motivo, sem apagar este texto.

A referência humana é a tabela de eventos sonoros fechada em 19/10/2026 ([`01_eventos_referencia.md`](01_eventos_referencia.md)).

## 1. Pergunta

Quais sons não verbais registrados pela escuta os detectores de eventos nomeiam, com que categorias e em que momentos, o que eles apontam que a escuta não registrou, e o que a escuta registrou que nenhuma categoria disponível nomeia. Na faixa 04, a pergunta se estende ao confronto entre as categorias dos modelos e a taxonomia de instrumentos enunciada por Almirante.

## 2. Modelos

- **PANNs**, modelo Cnn14 (pacote `panns-inference`, pesos `Cnn14_mAP=0.431`, depositados no Zenodo pelos autores), treinado no AudioSet. Atribui a cada trecho uma probabilidade independente, de 0 a 1, para cada uma das 527 categorias do AudioSet. A ontologia é fechada.
- **CLAP**, modelo `laion/larger_clap_general` (biblioteca `transformers`), treinado com pares de áudio e descrições em inglês. Compara cada trecho com as descrições de um vocabulário escolhido pela pesquisadora (seção 5) e mede a semelhança entre eles. O vocabulário é aberto, mas os resultados dependem das descrições oferecidas.

Os dois modelos permanecem com os parâmetros padrão de suas bibliotecas.

## 3. Entrada e condições

- Entrada de cada faixa igual à soma dos canais dividida por dois, decisão registrada no diário da fase 2, reamostrada para a taxa de cada modelo, 32 kHz no PANNs e 48 kHz no CLAP.
- Duas condições. **Sem filtro** e **com filtro**, este igual ao da fase 3 (`noisereduce`, parâmetros padrão), aplicado à faixa inteira, depois da reamostragem.
- Cinco faixas × duas condições × dois modelos, num total de vinte execuções.
- **Teste de determinismo.** Antes das execuções, o PANNs será aplicado duas vezes à faixa 04 sem filtro. Se as probabilidades coincidirem até a quarta casa decimal, cada execução roda uma vez. Se diferirem, a diferença será registrada e cada execução rodará três vezes, com os resultados relatados como média.

## 4. Janelas e critérios de apontamento

- Os dois modelos analisam cada faixa em **janelas de 2 segundos, com passo de 1 segundo**, de modo que cada segundo da gravação aparece em duas janelas. A grade é a mesma para os dois modelos.
- **PANNs.** Um rótulo é considerado **apontado** numa janela quando sua probabilidade é de pelo menos 0,3, e registrado como **indício** quando fica entre 0,1 e 0,3.
- **CLAP.** O modelo não produz probabilidades absolutas. Uma descrição é considerada **apontada** numa janela quando está entre as três mais semelhantes ao trecho, dentro do vocabulário da seção 5.
- **Evento nomeado.** Um evento da tabela de referência é considerado nomeado por um modelo, numa condição, quando ao menos uma janela que se sobrepõe ao evento tem apontado um rótulo correspondente à sua classe (seção 6). As classes compostas da tabela ("aplauso e grito de plateia", "fala, música e vento" e outras) são desdobradas, e cada componente é avaliado separadamente.

## 5. Vocabulário do CLAP

Todas as descrições entram no molde "This is the sound of …", completado pelos termos abaixo.

| Grupo | Termos |
|---|---|
| Termos de Almirante, sem descrição | tamborim · surdo · batucada · samba |
| Termos de Almirante, descritos | a tamborim, a small Brazilian frame drum played with a stick · a surdo, a large Brazilian bass drum · a batucada, a Brazilian samba percussion group |
| Classes da tabela de referência | applause · a crowd cheering and shouting · a man coughing · a man giving a speech · a distorted voice · the surface noise of an old record · clicks of a scratched record · a skipping record · a page of paper being turned · music · wind · women singing · a church bell · footsteps · electrical hum |
| Alternativas e distratores | silence · a tambourine · a snare drum · a bass drum · a door knocking · ocean waves |

Os termos sem descrição testam a palavra de Almirante isoladamente. Os termos descritos testam a mesma palavra acompanhada do conhecimento da pesquisadora sobre o instrumento, de modo análogo ao glossário da fase 3. "A door knocking" corresponde à hipótese alternativa registrada na escuta cega para os passos da faixa 05, e "ocean waves", ao critério de surpresa da fase 1 para o trecho de 4:38 a 5:03 da mesma faixa.

## 6. Correspondência entre rótulos e classes da referência

| Classe da referência | Rótulos do AudioSet (PANNs) | Descrições do CLAP |
|---|---|---|
| aplauso | Applause, Clapping | applause |
| grito de plateia | Cheering, Crowd, Shout, Yell, Hubbub, speech noise, speech babble | a crowd cheering and shouting |
| tosse | Cough, Throat clearing | a man coughing |
| fala | Speech, Male speech, man speaking, Narration, monologue, Conversation | a man giving a speech |
| voz alterada | Distortion | a distorted voice |
| pausa | nenhum | nenhuma |
| ruído de disco | Hiss, Static, Crackle, Noise, White noise, Pink noise | the surface noise of an old record |
| estalos regulares | Clicking, Tick, Tick-tock, Crackle | clicks of a scratched record |
| pulos | nenhum | a skipping record |
| papel | Crumpling, crinkling, Rustle, Tearing | a page of paper being turned |
| surdo | Bass drum, Drum, Timpani | surdo · a surdo, a large Brazilian bass drum · a bass drum |
| tamborim | Drum, Snare drum, Percussion | tamborim · a tamborim, a small Brazilian frame drum played with a stick · a snare drum |
| música | Music, Musical instrument e os rótulos de gênero e de clima musical do AudioSet (índices 137 a 282, exceto os de percussão já atribuídos acima) | music |
| vento | Wind, Wind noise (microphone) | wind |
| canto | Singing, Female singing, Choir, Chant, Vocal music | women singing |
| sino | Bell, Church bell, Chime, Tubular bells | a church bell |
| passos | Walk, footsteps | footsteps |
| zumbido | Hum, Mains hum, Buzz | electrical hum |
| mudança de intensidade | nenhum | nenhuma |

**Rótulos registrados à parte.** Alguns rótulos não correspondem a nenhuma classe, mas serão acompanhados por razões declaradas.

- "Tambourine" (PANNs) e "a tambourine" (CLAP). No AudioSet, o rótulo designa o pandeiro com platinelas, e não o tamborim. Sua ocorrência no trecho do tamborim será lida como coincidência de nome. A expectativa da fase 1 que o menciona será conferida separadamente.
- "Silence" (PANNs) e "silence" (CLAP). Nenhum trecho do corpus é silêncio acústico, já que o ruído do disco atravessa todas as faixas, e por isso a pausa da fala não recebe correspondência. A ocorrência desses rótulos nas pausas registradas será observada à parte.
- "Door" e "Knock" (PANNs) e "a door knocking" (CLAP), hipótese alternativa para os passos da faixa 05.
- "Ocean" e "Waves, surf" (PANNs) e "ocean waves" (CLAP), critério de surpresa da fase 1.

As classes "papel", com rótulos aproximados ("Crumpling", "Rustle"), e "voz alterada", com o rótulo genérico "Distortion", têm correspondência apenas aproximada, e isso será considerado na leitura.

## 7. Medidas

- **Eventos nomeados.** Para cada evento da tabela de referência, em cada modelo e condição, registra-se se foi nomeado, por qual rótulo e com que probabilidade ou posição.
- **Classes.** Para cada classe, a proporção de eventos nomeados, por modelo e condição.
- **Efeito do filtro.** A comparação entre as condições sem e com filtro, evento por evento.
- **Faixa 04.** Nos trechos do surdo e dos tamborins, os rótulos do PANNs mais prováveis e a posição de cada termo de Almirante no CLAP (tamborim, surdo, batucada e samba), comparando os termos sem descrição com os termos descritos. "Batucada" e "samba" não correspondem a uma classe da referência e são lidos como nomes do conjunto que se forma ao longo da faixa.
- **Aplausos e tosse da faixa 01.** O cruzamento entre os eventos da tabela, os três "Aplausos." escritos pelo Whisper na fase 3 e os rótulos dos detectores.
- **Rótulos registrados à parte**, conforme a seção 6.

## 8. Saídas

Cada execução gera um arquivo JSON em `resultados/fase4/`, nomeado por faixa, modelo e condição (por exemplo, `faixa01_panns_sem.json` e `faixa01_clap_com.json`), com a configuração, as versões das bibliotecas, a GPU, a data, a duração do processamento e, para cada janela, o início, o fim e os resultados. No PANNs, entram todos os rótulos com probabilidade de pelo menos 0,01. No CLAP, entram as semelhanças de todas as descrições do vocabulário.

As comparações usam apenas esses arquivos e a tabela de referência, e podem ser reproduzidas sem acesso aos áudios.

## 9. Escuta dirigida

Depois das comparações, a pesquisadora escuta os trechos que atendam a pelo menos um destes critérios, agrupados quando se sobrepõem.

1. Um rótulo correspondente a uma classe da referência, apontado numa janela que não se sobrepõe a nenhum evento dessa classe. A fala nas faixas 01 a 03 e o ruído de disco em todas as faixas ficam fora deste critério, por estarem presentes do começo ao fim.
2. Um rótulo sem correspondência com nenhuma classe, apontado com probabilidade de pelo menos 0,5 (PANNs) ou em primeiro lugar (CLAP).

A escuta será feita em dois tempos, como na fase 3, primeiro sem e depois com a leitura dos rótulos. O critério de surpresa da fase 1 ("a máquina apontar um evento, com marcação de tempo, que não consta na minha tabela da seção 2 nem na análise da dissertação, e que eu reconheço como presente no áudio ao reescutar o trecho indicado") será aplicado a cada trecho.

## 10. Confronto com as expectativas

Os resultados serão confrontados, item por item, com as expectativas sobre a detecção de eventos registradas em `docs/fase1/05_expectativas.md`, inclusive quando as contrariarem.
