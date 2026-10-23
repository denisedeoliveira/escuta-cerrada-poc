# Escuta dirigida da fase 4

Este documento registra a escuta dos trechos selecionados pelos critérios da seção 9 do desenho experimental (`docs/fase4/02_desenho_experimental.md`), com a alteração decidida em 20/10/2026 e registrada no diário da fase. A lista foi gerada pelo caderno de comparação (caderno 4b, seção 10) e salva em `resultados/fase4/medidas/escuta_dirigida.csv`. O formulário preenchido está em [`original/Fase_4_caderno_escuta_dirigida.docx`](original/Fase_4_caderno_escuta_dirigida.docx).

**Data da escuta:** 21 e 22/10/2026

**Condições de escuta** (equipamento, número de vezes, pausas): fone de ouvido e computador (desktop). Cada trecho foi escutado duas vezes por tipo de escuta (duas antes de ver o que os detectores apontaram e duas depois) – isto em média. Em alguns trechos mais complexos, a escuta se prolongou por mais vezes para se confirmar.

## Como escutar

Cada trecho é tocado pela função `ouvir_trecho` do caderno 4a (seção 7), com três segundos de folga antes e depois, a partir do arquivo original (soma dos canais, sem reamostragem).

A escuta de cada trecho se faz em dois tempos, como na fase 3. Na primeira escuta, o trecho é ouvido sem ler os rótulos dos detectores, e anota-se o que soa. Por isso, em cada bloco, o espaço da primeira escuta vem antes dos rótulos. Na segunda, leem-se os rótulos e escuta-se de novo. Quando um rótulo aparece só na condição com filtro, vale ouvir também a versão filtrada, com `ouvir_trecho(n, filtro=True)`.

Os tempos indicam o começo da primeira janela e o fim da última janela do trecho. Cada janela tem 2 segundos, e o modelo não diz em que ponto dela o som ocorre. Os trechos 22 (faixa 04 quase inteira) e 29 (faixa 05, de 2:44 a 4:32) são longos e podem ser escutados em partes.

**Critério 1** · rótulo correspondente a uma classe da tabela de referência, apontado fora de qualquer evento dessa classe. A classe aparece entre parênteses.

**Critério 2** · rótulo sem correspondência com nenhuma classe da tabela, com probabilidade de pelo menos 0,5 (PANNs) ou em primeiro lugar com e sem filtro (CLAP).

No PANNs, o número é a probabilidade mais alta alcançada pelo rótulo no trecho, seguida do número de janelas em que foi apontado. No CLAP, a descrição ficou em primeiro lugar, entre as 28 do vocabulário, com e sem filtro.

## Categorias

Definidas antes da escuta. Um trecho pode receber mais de uma categoria, uma para cada rótulo, e nesse caso a classificação indica o rótulo (por exemplo, “Sheep: 3; Clicking: 4”).

1.  **Som presente e não registrado** · o rótulo aponta um som que soa no trecho e que não consta na tabela de referência.
2.  **Som registrado, fora dos tempos da tabela** · o rótulo aponta um som que já consta na tabela, mas que se estende para além dos tempos marcados.
3.  **Som presente, com outro nome** · há no trecho um som que a escuta reconhece, mas o rótulo o nomeia como outra coisa.
4.  **Nenhum som correspondente** · nada no trecho corresponde ao rótulo, além do que já está registrado.
5.  **Efeito do filtro** · o rótulo só aparece com filtro e corresponde a uma alteração do som produzida pela filtragem.
6.  **Outro** · descrever.

**Critério de surpresa da fase 1** · “a máquina apontar um evento, com marcação de tempo, que não consta na minha tabela da seção 2 nem na análise da dissertação, e que eu reconheço como presente no áudio ao reescutar o trecho indicado”. Em cada trecho, responder sim ou não.

## Glossário dos rótulos

Tradução aproximada, apenas para a leitura. Os rótulos do PANNs vêm da ontologia do AudioSet, e as descrições do CLAP, do vocabulário da seção 5 do desenho.

- **a crowd cheering and shouting** · uma multidão aclamando e gritando
- **a man coughing** · um homem tossindo
- **a man giving a speech** · um homem discursando
- **a skipping record** · um disco pulando
- **Applause** · aplauso
- **Bee, wasp, etc.** · abelha, vespa etc.
- **Boat, Water vehicle** · barco, veículo aquático
- **Cattle, bovinae** · gado, bovinos
- **Clicking** · cliques
- **Crunch** · som de algo sendo esmagado ou mastigado
- **Fly, housefly** · mosca
- **Gong** · gongo
- **Gunshot, gunfire** · tiro, disparo
- **Hoot** · pio (de coruja)
- **Insect** · inseto
- **Livestock, farm animals, working animals** · animais de criação
- **Male speech, man speaking** · fala masculina
- **Moo** · mugido
- **Music** · música
- **Musical instrument** · instrumento musical
- **Narration, monologue** · narração, monólogo
- **ocean waves** · ondas do mar
- **Owl** · coruja
- **Plop** · plop (som curto, como de gota ou rolha)
- **Sheep** · ovelha
- **silence** · silêncio
- **Speech** · fala
- **Speech synthesizer** · sintetizador de voz
- **surdo** · surdo (palavra sem descrição)
- **Tearing** · rasgo
- **Vehicle** · veículo
- **Wind chime** · sino de vento (mensageiro dos ventos)
- **women singing** · mulheres cantando
- **Wood block** · bloco de madeira (instrumento de percussão)

## Trechos

### Trecho 1 · faixa 01 · 0:00,0 a 0:06,0

**Primeira escuta, antes de ler os rótulos:** aplausos

**O que os detectores apontaram** (ler só depois da primeira escuta)

- PANNs sem filtro · critério 1 (aplauso) · **Applause** · 0,64 · 5 janelas

**Segunda escuta, depois de ler:** aplausos

**Categoria:** 1

**Surpresa (critério da fase 1):** sim

**Observações:** Reescutando, percebi claramente os aplausos no início da gravação. Não sei se esqueci de anotar o que havia escutado ou se confundi com chiado quando transcrevi anteriormente.

### Trecho 2 · faixa 01 · 1:34,0 a 1:36,0

**Primeira escuta, antes de ler os rótulos:** aplausos

**O que os detectores apontaram** (ler só depois da primeira escuta)

- PANNs com filtro · critério 1 (estalos regulares) · **Clicking** · 0,35 · 1 janela

**Segunda escuta, depois de ler:** aplausos, mas algum deles parece estar próximo e soa como algo regular e mais forte.

**Categoria:** 3 e 5

**Surpresa (critério da fase 1):** não

**Observações:** O rótulo não aponta um evento novo, mas uma característica de um evento já registrado (aplauso 1.3). Na primeira escuta, soavam apenas aplausos. Depois da leitura de “Clicking”, foi possível distinguir entre eles um aplauso mais forte e mais regular que os demais, talvez por estar mais próximo do microfone. Na versão com filtro, esse aplauso passa a soar como um estalo nítido, de batida mais ou menos regular, enquanto o restante da plateia fica reduzido a um eco discreto por trás dele, o que explica o rótulo, que só aparece nessa condição. Ainda que decorra da alteração produzida pela filtragem, o rótulo dirigiu a escuta para uma qualidade do evento que não havia sido registrada.

### Trecho 3 · faixa 01 · 4:11,0 a 4:13,0

**Primeira escuta, antes de ler os rótulos:** aplausos

**O que os detectores apontaram** (ler só depois da primeira escuta)

- PANNs com filtro · critério 1 (estalos regulares) · **Clicking** · 0,44 · 1 janela

**Segunda escuta, depois de ler:** aplausos

**Categoria:** 4

**Surpresa (critério da fase 1):** não

**Observações:** O trecho está dentro de um aplauso já registrado (1.9). Na versão original e na versão com filtro, soam apenas aplausos, abafados na segunda, sem clique ou estalo reconhecível que corresponda ao rótulo “Clicking”, apontado só na condição com filtro. Ao contrário do trecho 2, em que o mesmo rótulo e a mesma condição levaram a escuta a um aplaudidor destacado, aqui nenhum traço do aplauso se distingue.

### Trecho 4 · faixa 01 · 4:30,0 a 4:32,0

**Primeira escuta, antes de ler os rótulos:** fala e barulho proeminente do disco girando

**O que os detectores apontaram** (ler só depois da primeira escuta)

- CLAP com e sem filtro · critério 1 (pulos) · **a skipping record** · 1º lugar · 1 janela

**Segunda escuta, depois de ler:** barulho proeminente do disco girando

**Categoria:** 3

**Surpresa (critério da fase 1):** não

**Observações:** Não há pulo da agulha no trecho. Soam a fala, com uma correção de Vargas registrada na transcrição de referência (“{fala: da industrial...} da produção”), e um ruído proeminente do disco girando, ainda mais perceptível na versão com filtro. O rótulo parece nomear como pulo o ruído do suporte, já registrado (1.13). Não é possível descartar que a interrupção e a retomada da fala, cuja estrutura se assemelha à de um pulo, tenham contribuído para a semelhança.

### Trecho 5 · faixa 01 · 4:54,0 a 4:58,0

**Primeira escuta, antes de ler os rótulos:** aplausos e tosse

**O que os detectores apontaram** (ler só depois da primeira escuta)

- PANNs com filtro · critério 1 (estalos regulares) · **Clicking** · 0,33 · 1 janela
- PANNs sem filtro · critério 2 · **Sheep** · 0,57 · 1 janela

**Segunda escuta, depois de ler:** aplausos e tosse

**Categoria:** Sheep: 3; Clicking: 4

**Surpresa (critério da fase 1):** não

**Observações:** O trecho reúne o fim do aplauso 1.10 e a tosse 1.11, ambos registrados. Na versão original, soam aplausos e a tosse, dividida em duas, e nenhum som que remeta a um animal. O rótulo “Sheep” (com “Bleat”, balido, logo abaixo) nomeia a tosse como vocalização animal. Nas janelas imediatamente anteriores, o PANNs já apontava “Animal”, “Crow” e “Caw” com valores baixos (caderno 4b, seção 6.1), embora a categoria “Cough” exista no AudioSet e não apareça em nenhuma janela. Na versão com filtro, restam ruídos dos aplausos, sem estalo que corresponda a “Clicking” e sem nada que remeta à tosse. A primeira escuta deste trecho não foi inteiramente cega, já que a associação entre a tosse e “Sheep” era conhecida desde a leitura do caderno 4b.

A primeira tosse começa pouco depois de 4:55, e a segunda, continuação dela, soa ao longo do segundo 4:56 e termina antes de 4:57. A janela de 4:56 a 4:58, em que “Sheep” alcança 0,57, contém, portanto, a segunda parte da tosse. A partir de 4:57 nada de diferente soa no trecho. O fim registrado na tabela de referência (4:56,0) indica o segundo em que a tosse ainda soa, e não o instante em que ela termina, e a tabela permanece como foi fechada.

### Trecho 6 · faixa 01 · 5:27,0 a 5:35,5

**Primeira escuta, antes de ler os rótulos:** aplausos e “muito bem”

**O que os detectores apontaram** (ler só depois da primeira escuta)

- CLAP com e sem filtro · critério 2 · **silence** · 1º lugar · 1 janela
- PANNs com filtro · critério 2 · **Crunch** · 0,61 · 3 janelas

**Segunda escuta, depois de ler:** aplausos e “muito bem”

**Categoria:** Crunch: 3 e 5; silence: 6

**Surpresa (critério da fase 1):** não

**Observações:** O trecho corresponde ao aplauso com “muito bem” do fim da faixa (1.12) e aos segundos finais, depois do corte abrupto. O rótulo “Crunch”, apontado só com filtro entre 5:27 e 5:31, corresponde aos aplausos, que na versão filtrada se reduzem a cliques constantes, parecidos com a palma proeminente do trecho 2, enquanto o “muito bem” passa a soar bem mais distante. O rótulo “silence” foi apontado apenas na última janela (5:33,5 a 5:35,5). Depois do fim da fala, soam cerca de 2 segundos de giro do disco e cerca de 3 segundos de silêncio completo, sem ruído de superfície. O rótulo corresponde, portanto, ao que soa, e o silêncio, que não vem do disco, decorre do corte já registrado na descrição do evento 1.12.

### Trecho 7 · faixa 02 · 0:02,0 a 0:19,0

**Primeira escuta, antes de ler os rótulos:** fala e chiado forte

**O que os detectores apontaram** (ler só depois da primeira escuta)

- PANNs com filtro · critério 2 · **Speech synthesizer** · 0,71 · 6 janelas

**Segunda escuta, depois de ler:** fala e chiado forte

**Categoria:** 5

**Surpresa (critério da fase 1):** não

**Observações:** Na versão original, soam a fala e um chiado forte, sem nada que remeta a voz sintetizada. Na versão com filtro, o chiado permanece, bem mais fraco, e surge ao fundo da voz um som metalizado e constante, ausente do original. O rótulo “Speech synthesizer”, apontado só nessa condição, corresponde a essa alteração produzida pela filtragem, conhecida como ruído musical, que confere à voz um timbre artificial.

### Trecho 8 · faixa 02 · 0:29,0 a 1:13,0

**Primeira escuta, antes de ler os rótulos:** fala e ruído de disco girando constante

**O que os detectores apontaram** (ler só depois da primeira escuta)

- PANNs com filtro · critério 2 · **Speech synthesizer** · 0,67 · 14 janelas
- PANNs sem filtro · critério 1 (música) · **Music** · 0,64 · 4 janelas

**Segunda escuta, depois de ler:** fala e ruído de disco girando constante

**Categoria:** Speech synthesizer: 5, como no trecho 7; Music: 3

**Surpresa (critério da fase 1):** não

**Observações:** O modelo, provavelmente, nomeou o giro do disco como música, já que ele é constante e está com marcação razoável no trecho.

### Trecho 9 · faixa 02 · 1:21,0 a 1:37,0

**Primeira escuta, antes de ler os rótulos:** fala e ruído de disco girando constante

**O que os detectores apontaram** (ler só depois da primeira escuta)

- PANNs com filtro · critério 2 · **Plop** · 0,65 · 1 janela
- PANNs com filtro · critério 2 · **Speech synthesizer** · 0,64 · 4 janelas
- PANNs sem filtro · critério 1 (música) · **Music** · 0,69 · 4 janelas

**Segunda escuta, depois de ler:** fala e ruído de disco girando constante

**Categoria:** Plop: 3; Speech synthesizer: 5, como no trecho 7; Music: 3

**Surpresa (critério da fase 1):** não

**Observações:** O modelo, provavelmente, nomeou o giro do disco como música, já que ele é constante e está com marcação razoável no trecho. O Plop também deve ter sido efeito do giro do disco, bem proeminente nos 3 segundos finais do trecho, tanto na versão original quanto filtrada.

### Trecho 10 · faixa 02 · 1:49,0 a 1:59,0

**Primeira escuta, antes de ler os rótulos:** fala e ruído de disco girando constante

**O que os detectores apontaram** (ler só depois da primeira escuta)

- PANNs sem filtro · critério 1 (música) · **Music** · 0,73 · 3 janelas

**Segunda escuta, depois de ler:** fala e ruído de disco girando constante

**Categoria:** 3

**Surpresa (critério da fase 1):** não

**Observações:** O modelo, provavelmente, nomeou o giro do disco como música, já que ele é constante e está bem marcado no trecho.

### Trecho 11 · faixa 02 · 2:07,0 a 2:35,0

**Primeira escuta, antes de ler os rótulos:** fala e ruído de disco girando constante

**O que os detectores apontaram** (ler só depois da primeira escuta)

- PANNs com filtro · critério 2 · **Speech synthesizer** · 0,62 · 5 janelas
- PANNs sem filtro · critério 1 (música) · **Music** · 0,70 · 8 janelas

**Segunda escuta, depois de ler:** fala e ruído de disco girando constante

**Categoria:** Speech synthesizer: 5, como no trecho 7; Music: 3

**Surpresa (critério da fase 1):** não

**Observações:** O modelo, provavelmente, nomeou o giro do disco como música, já que ele é constante e está bem marcado, como uma batida, principalmente nos primeiros segundos do trecho.

### Trecho 12 · faixa 02 · 2:43,0 a 2:45,0

**Primeira escuta, antes de ler os rótulos:** fala e ruído de disco girando constante

**O que os detectores apontaram** (ler só depois da primeira escuta)

- PANNs sem filtro · critério 1 (música) · **Music** · 0,35 · 1 janela

**Segunda escuta, depois de ler:** fala e ruído de disco girando constante

**Categoria:** 3

**Surpresa (critério da fase 1):** não

**Observações:** O modelo, provavelmente, nomeou o giro do disco como música, já que ele é constante e está com marcação razoável no trecho.

### Trecho 13 · faixa 02 · 2:53,0 a 3:17,0

**Primeira escuta, antes de ler os rótulos:** fala e ruído de disco girando constante

**O que os detectores apontaram** (ler só depois da primeira escuta)

- PANNs com filtro · critério 2 · **Speech synthesizer** · 0,65 · 5 janelas
- PANNs sem filtro · critério 1 (música) · **Music** · 0,67 · 6 janelas

**Segunda escuta, depois de ler:** fala e ruído de disco girando constante

**Categoria:** Speech synthesizer: 5, como no trecho 7; Music: 3

**Surpresa (critério da fase 1):** não

**Observações:** O modelo, provavelmente, nomeou o giro do disco como música, já que ele é constante e está com marcação razoável no trecho.

### Trecho 14 · faixa 03 · 0:10,0 a 0:12,0

**Primeira escuta, antes de ler os rótulos:** fala e ruído de disco girando constante, mas mais discreto

**O que os detectores apontaram** (ler só depois da primeira escuta)

- PANNs com filtro · critério 2 · **Speech synthesizer** · 0,56 · 1 janela

**Segunda escuta, depois de ler:** fala e ruído de disco girando constante, mas mais discreto

**Categoria:** Speech synthesizer: 5, como no trecho 7

**Surpresa (critério da fase 1):** não

**Observações:** Como no trecho 7, o rótulo corresponde ao ruído musical produzido pela filtragem.

### Trecho 15 · faixa 03 · 2:12,0 a 2:14,0

**Primeira escuta, antes de ler os rótulos:** fala e ruído de disco girando constante, mas mais discreto

**O que os detectores apontaram** (ler só depois da primeira escuta)

- PANNs com filtro · critério 1 (estalos regulares) · **Clicking** · 0,30 · 1 janela

**Segunda escuta, depois de ler:** fala e ruído de disco girando constante, mas mais discreto

**Categoria:** 3

**Surpresa (critério da fase 1):** não

**Observações:** O clique está ligado ao giro do disco, proeminente no original e mais discreto na versão filtrada. Ainda assim, o rótulo só foi apontado na condição com filtro.

### Trecho 16 · faixa 03 · 3:01,0 a 3:03,0

**Primeira escuta, antes de ler os rótulos:** fala e ruído de disco girando constante, mas mais discreto

**O que os detectores apontaram** (ler só depois da primeira escuta)

- PANNs com filtro · critério 2 · **Speech synthesizer** · 0,58 · 1 janela

**Segunda escuta, depois de ler:** fala e ruído de disco girando constante, mas mais discreto

**Categoria:** Speech synthesizer: 5, como no trecho 7

**Surpresa (critério da fase 1):** não

**Observações:** Como no trecho 7, o rótulo corresponde ao ruído musical produzido pela filtragem.

### Trecho 17 · faixa 03 · 3:42,0 a 3:44,0

**Primeira escuta, antes de ler os rótulos:** fala e chiado

**O que os detectores apontaram** (ler só depois da primeira escuta)

- PANNs sem filtro · critério 2 · **Gunshot, gunfire** · 0,50 · 1 janela

**Segunda escuta, depois de ler:** fala e chiado

**Categoria:** 4

**Surpresa (critério da fase 1):** não

**Observações:** Na janela de 3:42 a 3:44 soam apenas a fala e o chiado, sem estalo ou impacto isolado que corresponda a “Gunshot, gunfire”, cuja probabilidade (0,50) está no limite do critério 2.

### Trecho 18 · faixa 03 · 4:45,0 a 4:48,0

**Primeira escuta, antes de ler os rótulos:** fala e chiado

**O que os detectores apontaram** (ler só depois da primeira escuta)

- PANNs com filtro · critério 2 · **Speech synthesizer** · 0,75 · 2 janelas

**Segunda escuta, depois de ler:** fala e chiado

**Categoria:** Speech synthesizer: 5, como no trecho 7

**Surpresa (critério da fase 1):** não

**Observações:** Como no trecho 7, o rótulo corresponde ao ruído musical produzido pela filtragem.

### Trecho 19 · faixa 03 · 5:38,0 a 5:40,0

**Primeira escuta, antes de ler os rótulos:** fala e chiado

**O que os detectores apontaram** (ler só depois da primeira escuta)

- PANNs com filtro · critério 2 · **Speech synthesizer** · 0,55 · 1 janela

**Segunda escuta, depois de ler:** fala e chiado

**Categoria:** Speech synthesizer: 5, como no trecho 7

**Surpresa (critério da fase 1):** não

**Observações:** Como no trecho 7, o rótulo corresponde ao ruído musical produzido pela filtragem.

### Trecho 20 · faixa 03 · 5:57,0 a 6:02,1

**Primeira escuta, antes de ler os rótulos:** fala com chiado

**O que os detectores apontaram** (ler só depois da primeira escuta)

- CLAP com e sem filtro · critério 2 · **silence** · 1º lugar · 1 janela
- PANNs com filtro · critério 2 · **Crunch** · 0,70 · 2 janelas

**Segunda escuta, depois de ler:** fala com chiado e dois segundos finais de silêncio

**Categoria:** Crunch: 3 e 5; silence: 1

**Surpresa (critério da fase 1):** não

**Observações:** Antes do silêncio final, o chiado se intensifica. No original, soa como um chuvisco mais forte. Na versão com filtro, como um estalo final mais proeminente, que chama mais atenção. O rótulo “Crunch”, apontado só com filtro entre 5:57 e 6:00, corresponde a esse ruído, já presente no original e realçado pela filtragem. O rótulo “silence”, apontado na última janela (6:00,1 a 6:02,1), corresponde aos cerca de 2 segundos finais de silêncio completo, sem ruído de superfície, que não constam na tabela de referência, cujo evento 3.4 termina em 6:00. Como no trecho 6, o silêncio decorre do fim do arquivo, e não do disco.

Soa a parte final da fala por volta de 5:54, no início do trecho tocado, embora o evento 3.4 registre o intervalo de 5:40 a 6:00 como sem fala.

### Trecho 21 · faixa 04 · 0:00,0 a 0:02,0

**Primeira escuta, antes de ler os rótulos:** fala e chiado forte

**O que os detectores apontaram** (ler só depois da primeira escuta)

- PANNs com filtro · critério 1 (papel) · **Tearing** · 0,37 · 1 janela

**Segunda escuta, depois de ler:** fala e estalos (de fato, parecem papel sendo rasgado, na versão filtrada)

**Categoria:** 3 e 5

**Surpresa (critério da fase 1):** não

**Observações:** No início da faixa, junto ao começo da fala (4.1), soam estalos do disco sobre um chiado forte. Na versão com filtro, esses estalos se destacam e passam de fato a soar como papel sendo rasgado, o que corresponde ao rótulo “Tearing”, apontado só nessa condição. É o único apontamento da classe papel em todo o corpus, enquanto as três viradas de página registradas na faixa 03 (3.1 a 3.3) não foram nomeadas por nenhum modelo, em nenhuma condição.

### Trecho 22 · faixa 04 · 0:11,0 a 1:04,9

**Primeira escuta, antes de ler os rótulos:** fala de Almirante, com o surdo, primeiro tamborim e depois segundo tamborim (e os outros que não sei quais são, porque na parte que ele nomeia, a gravação pula).

**O que os detectores apontaram** (ler só depois da primeira escuta)

- PANNs com filtro · critério 1 (música) · **Music** · 0,62 · 4 janelas
- PANNs com filtro · critério 1 (fala) · **Speech** · 0,74 · 18 janelas
- PANNs sem filtro · critério 1 (música) · **Music** · 0,90 · 35 janelas
- PANNs sem filtro · critério 1 (música) · **Musical instrument** · 0,54 · 10 janelas
- PANNs sem filtro · critério 1 (fala) · **Speech** · 0,57 · 5 janelas
- PANNs sem filtro · critério 1 (música) · **Wood block** · 0,39 · 2 janelas

**Segunda escuta, depois de ler:** fala de Almirante, com o surdo, primeiro tamborim e depois segundo tamborim (e os outros que não sei quais são, porque na parte que ele nomeia, a gravação pula). Na versão com filtro, os instrumentos continuam a soar e há um girar de disco mais discreto ao fundo.

**Categoria:** Music, Musical instrument e Wood block → 3; Speech sem filtro → 2; Speech com filtro → 4

**Surpresa (critério da fase 1):** não

**Observações:** Os rótulos não nomeiam os instrumentos que Almirante apresenta. O surdo e os tamborins, registrados nos eventos 4.2, 4.4 e 4.6, aparecem como “Music” e “Musical instrument”, no nível geral da música, e o primeiro tamborim, por duas janelas, como “Wood block” (bloco de madeira). “Speech” sem filtro aponta a fala de Almirante no fim do anúncio do segundo tamborim (0:44) e no trecho final com pulos (0:56 a 0:59), em que ele anuncia o instrumento seguinte, registrado na descrição do evento 4.7 mas não como fala. Com filtro, “Speech” se espalha pelos trechos instrumentais, que soam precisamente como instrumentos musicais. O nome dos instrumentos seguintes ao segundo tamborim não é audível, porque a gravação pula no momento em que Almirante os anuncia.

### Trecho 23 · faixa 05 · 0:18,0 a 0:21,0

**Primeira escuta, antes de ler os rótulos:** música religiosa

**O que os detectores apontaram** (ler só depois da primeira escuta)

- CLAP com e sem filtro · critério 1 (surdo) · **surdo** · 1º lugar · 2 janelas

**Segunda escuta, depois de ler:** música religiosa (versão original, porque com filtro mal dá para reconhecer que é música, parece algo arranhando e num tom bem agudo – quase insuportável de ouvir).

**Categoria:** 4

**Surpresa (critério da fase 1):** não

**Observações:** No trecho soa apenas a música religiosa do evento 5.2, sem percussão grave que corresponda a um surdo. A palavra “surdo”, sem descrição, ficou em primeiro lugar com e sem filtro, mas aparece entre as três primeiras na maior parte das janelas da faixa (caderno 4b, seção 8), o que indica uma proximidade genérica, e não a nomeação de um som. Na versão com filtro, mal se reconhece que é música, e o trecho soa como algo arranhando, num tom muito agudo, quase insuportável de ouvir.

### Trecho 24 · faixa 05 · 1:09,0 a 1:12,0

**Primeira escuta, antes de ler os rótulos:** vento ficando cada vez mais forte, com música ao fundo

**O que os detectores apontaram** (ler só depois da primeira escuta)

- PANNs sem filtro · critério 1 (música) · **Gong** · 0,45 · 2 janelas

**Segunda escuta, depois de ler:** vento ficando cada vez mais forte, com música ao fundo

**Categoria:** 2

**Surpresa (critério da fase 1):** não

**Observações:** O trecho está no evento 5.3 (vento), mas a música do evento 5.2 continua ao fundo, enquanto o vento se intensifica, para além do fim registrado na tabela (1:03). O rótulo “Gong”, que corresponde à classe música, aponta essa continuação, mas não se distingue na música nenhum som metálico ou ressonante que se aproxime de um gongo. O modelo nomeia a música pela categoria de um instrumento que não soa no trecho.

### Trecho 25 · faixa 05 · 1:24,0 a 1:26,0

**Primeira escuta, antes de ler os rótulos:** somente vento forte

**O que os detectores apontaram** (ler só depois da primeira escuta)

- PANNs sem filtro · critério 2 · **Vehicle** · 0,51 · 1 janela

**Segunda escuta, depois de ler:** somente vento (mas o início, de fato, parece um barulho de motor de carro)

**Categoria:** 3

**Surpresa (critério da fase 1):** não

**Observações:** Soa apenas o vento forte do fim do evento 5.3. O rótulo “Vehicle” nomeia esse vento como veículo, e, depois da leitura, o início do trecho de fato soa como o ruído de um motor de carro, semelhança que a primeira escuta não havia notado. O PANNs não nomeou como “Wind” nenhuma das passagens de vento da faixa (caderno 4b, seção 4).

### Trecho 26 · faixa 05 · 1:53,0 a 2:01,0

**Primeira escuta, antes de ler os rótulos:** fala com música sertaneja e vento ao fundo (música mais baixa que vento, que está mais baixo que as vozes)

**O que os detectores apontaram** (ler só depois da primeira escuta)

- CLAP com e sem filtro · critério 1 (surdo) · **surdo** · 1º lugar · 1 janela
- PANNs sem filtro · critério 2 · **Bee, wasp, etc.** · 0,84 · 3 janelas
- PANNs sem filtro · critério 2 · **Fly, housefly** · 0,56 · 1 janela
- PANNs sem filtro · critério 2 · **Insect** · 0,73 · 3 janelas

**Segunda escuta, depois de ler:** fala com música sertaneja e vento ao fundo (música mais baixa que vento, que está mais baixo que as vozes) (na versão com filtro, só sobram as vozes e um pouco do vento – a música desaparece).

**Categoria:** surdo: 4; Bee, Insect, Fly: 4

**Surpresa (critério da fase 1):** não

**Observações:** O trecho está no evento 5.5, com as vozes à frente, o vento ao fundo e, mais baixa, uma música sertaneja. A palavra “surdo” ficou em primeiro lugar com e sem filtro, mas não há no trecho percussão grave que lhe corresponda. Os rótulos “Bee, wasp, etc.”, “Insect” e “Fly”, com valores altos (até 0,84), não correspondem a nada que a escuta reconheça com segurança como zumbido. O instrumento e o vento soam baixos demais para dar essa impressão. Não se pode descartar que o modelo responda ao zumbido elétrico registrado na faixa inteira (5.14), pouco audível e identificado apenas no espectrograma. Na versão com filtro, restam apenas as vozes e um pouco do vento, e a música desaparece.

### Trecho 27 · faixa 05 · 2:08,0 a 2:13,0

**Primeira escuta, antes de ler os rótulos:** música sertaneja e vento oscilante em intensidade ao fundo, além da voz proeminente

**O que os detectores apontaram** (ler só depois da primeira escuta)

- CLAP com e sem filtro · critério 1 (tosse) · **a man coughing** · 1º lugar · 1 janela
- PANNs sem filtro · critério 2 · **Bee, wasp, etc.** · 0,82 · 2 janelas
- PANNs sem filtro · critério 2 · **Fly, housefly** · 0,56 · 1 janela
- PANNs sem filtro · critério 2 · **Insect** · 0,76 · 2 janelas

**Segunda escuta, depois de ler:** música sertaneja e vento oscilante em intensidade ao fundo, além da voz proeminente (na versão com filtro: música e vento desaparecem completamente).

**Categoria:** a man coughing: 4; Bee, Insect, Fly: 4

**Surpresa (critério da fase 1):** não

**Observações:** O trecho está no evento 5.5, com a voz à frente, a música sertaneja e o vento, de intensidade oscilante, ao fundo. A descrição “a man coughing”, em primeiro lugar com e sem filtro, não corresponde a nenhuma tosse, pigarro ou som áspero no trecho. Os rótulos de inseto repetem os do trecho 26, com valores próximos, e, como lá, não correspondem a nada que a escuta reconheça com segurança. Na versão com filtro, a música e o vento desaparecem completamente, e resta só a voz.

### Trecho 28 · faixa 05 · 2:25,0 a 2:29,0

**Primeira escuta, antes de ler os rótulos:** vento e vozes (com vento soando ao fundo de forma oscilante)

**O que os detectores apontaram** (ler só depois da primeira escuta)

- CLAP com e sem filtro · critério 2 · **silence** · 1º lugar · 1 janela
- PANNs sem filtro · critério 2 · **Insect** · 0,54 · 1 janela

**Segunda escuta, depois de ler:** vento e vozes (com vento soando ao fundo de forma oscilante) - na versão com filtro, só ficaram as vozes. E ficou tudo bem limpo, sem nenhum ruído ao fundo (diferente de outros registros/trechos, em que sempre se ouvia resquício de chiado)

**Categoria:** silence: 4 (sem filtro) e 5 (com filtro); Insect: 4

**Surpresa (critério da fase 1):** não

**Observações:** O trecho está no evento 5.5, com vozes e o vento oscilante ao fundo. Na versão original não há silêncio em nenhum momento, e a descrição “silence”, em primeiro lugar também nessa condição, não corresponde ao que soa. Na versão com filtro, restam só as vozes, sobre um fundo inteiramente limpo, sem o resquício de chiado que permanece nos demais trechos filtrados. Nessa condição, o rótulo corresponde ao fundo silencioso produzido pela filtragem. O rótulo “Insect” (0,54) repete, com valor menor, os rótulos de inseto dos trechos 26 e 27, e, como lá, não corresponde a nada que a escuta reconheça.

### Trecho 29 · faixa 05 · 2:44,0 a 4:32,0

**Primeira escuta, antes de ler os rótulos:**

vozes (o tempo todo)

vento (ao fundo a partir de 0:38, com força por volta de 0:50-0:56, do tocador)

moças cantando (a partir de 0:09, até 0:33, do tocador)

sino (1:10-1:26)

passos (1:39-1:46)

disco girando nos segundos finais

**O que os detectores apontaram** (ler só depois da primeira escuta)

- CLAP com e sem filtro · critério 1 (grito de plateia) · **a crowd cheering and shouting** · 1º lugar · 1 janela
- CLAP com e sem filtro · critério 1 (fala) · **a man giving a speech** · 1º lugar · 11 janelas
- CLAP com e sem filtro · critério 1 (surdo) · **surdo** · 1º lugar · 1 janela
- CLAP com e sem filtro · critério 2 · **ocean waves** · 1º lugar · 1 janela
- CLAP com e sem filtro · critério 2 · **silence** · 1º lugar · 1 janela
- PANNs com filtro · critério 1 (fala) · **Speech** · 0,92 · 81 janelas
- PANNs com filtro · critério 2 · **Speech synthesizer** · 0,64 · 2 janelas
- PANNs sem filtro · critério 1 (fala) · **Male speech, man speaking** · 0,59 · 9 janelas
- PANNs sem filtro · critério 1 (música) · **Music** · 0,32 · 1 janela
- PANNs sem filtro · critério 1 (fala) · **Narration, monologue** · 0,58 · 6 janelas
- PANNs sem filtro · critério 1 (fala) · **Speech** · 0,91 · 88 janelas
- PANNs sem filtro · critério 1 (música) · **Wind chime** · 0,34 · 1 janela
- PANNs sem filtro · critério 2 · **Bee, wasp, etc.** · 0,85 · 4 janelas
- PANNs sem filtro · critério 2 · **Cattle, bovinae** · 0,69 · 1 janela
- PANNs sem filtro · critério 2 · **Fly, housefly** · 0,51 · 1 janela
- PANNs sem filtro · critério 2 · **Hoot** · 0,50 · 1 janela
- PANNs sem filtro · critério 2 · **Insect** · 0,74 · 2 janelas
- PANNs sem filtro · critério 2 · **Livestock, farm animals, working animals** · 0,61 · 1 janela
- PANNs sem filtro · critério 2 · **Moo** · 0,60 · 1 janela
- PANNs sem filtro · critério 2 · **Owl** · 0,60 · 1 janela

**Segunda escuta, depois de ler:**

vozes (o tempo todo)

vento (ao fundo a partir de 0:38, com força por volta de 0:50-0:56, do tocador)

moças cantando (a partir de 0:09, até 0:33, do tocador)

sino (1:10-1:26)

passos (1:39-1:46)

Com filtro: apaga muita coisa, sobram só as vozes principais, as moças cantando (cortadas, algumas partes desaparecidas). Vento aparece muito momentaneamente entre 0:50 e 0:55 (quando no original está bem forte). Sino fica ao fundo, mas menos intenso, assim como os passos. No lugar do disco girando nos segundos finais, há total silêncio.

**Categoria:**

**fala (Speech, Male speech, Narration, a man giving a speech): 2**

Speech synthesizer: 5

Bee e Insect (2:44 e 2:51): 3

Owl e Hoot: 4

Bee, Fly e Insect (3:39 a 3:42): 4

a crowd cheering and shouting: 3

Wind chime e Music: 3

Cattle, Livestock e Moo: 4

ocean waves: 4

surdo: 4

silence: 4 (sem filtro) e 5 (com filtro)

**Surpresa (critério da fase 1):** não

**Observações:** Correspondência com a tabela. Os tempos da escuta coincidem, quase ao segundo, com os eventos registrados: canto (5.6), vento (5.7), sino (5.8), passos (5.9) e giro do disco (5.10). As vozes soam o tempo todo, mas a tabela não registra fala entre 2:49 e 5:04. Os rótulos de fala apontam essa continuação da fala do evento 5.5, e por isso entram na categoria 2.

Canto. A entrada do canto se ouve já por volta de 2:44, ao fundo, antes do início registrado no 5.6 (2:50). “Bee” (2:44) e “Insect” (2:51) nomeiam esse começo do canto, que, na versão original, de fato pode ser confundido com um zumbido de inseto. Em 2:55, quando o canto se interrompe e entram as vozes masculinas, “Owl” e “Hoot” não correspondem a nada que lembre um pio.

Vento. No momento de maior força do vento (3:34), a descrição “a crowd cheering and shouting” nomeia o vento e as vozes como uma multidão. Logo depois (3:39 a 3:42), os rótulos de inseto não correspondem a nada de particular.

Sino. “Wind chime” e “Music” (3:55 a 3:57) nomeiam o sino de modo aproximado, como sino de vento. Em 4:06, quando a voz diz “astrolábio”, os rótulos “Cattle”, “Livestock” e “Moo” não correspondem a nada que se distinga no trecho.

Passos e fim. “ocean waves” (4:26) e “surdo” (4:28) não correspondem a nada semelhante. “silence” (4:30) aponta o giro do disco na versão original e corresponde, na versão com filtro, ao silêncio total que ocupa o lugar desse giro.

Versão com filtro. Apaga quase tudo, e restam as vozes principais e o canto das moças, com partes cortadas. O vento aparece apenas por um instante (3:31 a 3:36), justamente quando é mais forte no original, e o sino e os passos ficam ao fundo, menos intensos.

### Trecho 30 · faixa 05 · 4:44,0 a 4:46,0

**Primeira escuta, antes de ler os rótulos:** nota constante, e aguda, da música

**O que os detectores apontaram** (ler só depois da primeira escuta)

- CLAP com e sem filtro · critério 2 · **silence** · 1º lugar · 1 janela

**Segunda escuta, depois de ler:** nota constante, e aguda, da música (no filtro, ficou distorcido, mas sempre soando alguma coisa, nunca silêncio)

**Categoria:** 4

**Surpresa (critério da fase 1):** não

**Observações:** O trecho está no evento 5.11 (música de suspense), em que soa uma nota aguda e constante. A descrição “silence”, em primeiro lugar com e sem filtro, não corresponde ao que soa. Na versão com filtro, a nota fica distorcida, mas algo soa o tempo todo, sem silêncio. É possível que a constância da nota, sem ataques nem variações, tenha aproximado o trecho da descrição de silêncio.

### Trecho 31 · faixa 05 · 5:13,0 a 5:15,0

**Primeira escuta, antes de ler os rótulos:** fala apenas (final com início da música)

**O que os detectores apontaram** (ler só depois da primeira escuta)

- CLAP com e sem filtro · critério 1 (canto) · **women singing** · 1º lugar · 1 janela

**Segunda escuta, depois de ler:** fala apenas (final com início da música) – com filtro, somente fala

**Categoria:** 3

**Surpresa (critério da fase 1):** não

**Observações:** O trecho está no evento 5.13, e soa fala, com a música bem baixa ao fundo. Por volta de 5:14 soa um “aliiii” agudo e prolongado, que a escuta não reconhece como canto, mas que é o único som do trecho a que a descrição “women singing”, em primeiro lugar com e sem filtro, pode corresponder. Uma vogal aguda e sustentada se aproxima, para o modelo, de uma nota cantada. Na versão com filtro, resta somente a fala.

### Trecho 32 · faixa 05 · 6:16,0 a 6:18,0

**Primeira escuta, antes de ler os rótulos:** música aguda ao final (principalmente nos primeiros segundos) e fala

**O que os detectores apontaram** (ler só depois da primeira escuta)

- CLAP com e sem filtro · critério 1 (surdo) · **surdo** · 1º lugar · 1 janela

**Segunda escuta, depois de ler:** música aguda ao final (principalmente nos primeiros segundos) e fala (versão com filtro: somente vozes)

**Categoria:** 4

**Surpresa (critério da fase 1):** não

**Observações:** O trecho está no evento 5.13, com fala e uma música aguda, mais presente nos primeiros segundos. A palavra “surdo”, em primeiro lugar com e sem filtro, não corresponde a nenhuma percussão grave, o que repete o comportamento dos trechos 23 e 26 e a proximidade genérica dessa palavra com a maior parte das janelas da faixa (caderno 4b, seção 8). Na versão com filtro, restam somente as vozes.

### Trecho 33 · faixa 05 · 6:31,0 a 6:33,0

**Primeira escuta, antes de ler os rótulos:** música ao fundo com as vozes - com um "aliii" no 0:05 (do tocador)

**O que os detectores apontaram** (ler só depois da primeira escuta)

- CLAP com e sem filtro · critério 1 (surdo) · **surdo** · 1º lugar · 1 janela

**Segunda escuta, depois de ler:** música ao fundo (notas agudas em 0:02) com as vozes - com um "aliii" no 0:05 (do tocador); na versão com filtro, dá para ouvir as notas agudas da música.

**Categoria:** 4

**Surpresa (critério da fase 1):** não

**Observações:** O trecho está no evento 5.13, com vozes e música ao fundo, que tem notas agudas por volta de 6:30, e um “aliii” em 6:33. Como no trecho 32, a palavra “surdo”, em primeiro lugar com e sem filtro, não corresponde a nenhuma percussão grave. Na versão com filtro, ao contrário de outros trechos da faixa, as notas agudas da música continuam audíveis.

### Trecho 34 · faixa 05 · 7:15,0 a 7:17,0

**Primeira escuta, antes de ler os rótulos:** música ao fundo, voz e disco girando nos 2 segundos finais

**O que os detectores apontaram** (ler só depois da primeira escuta)

- PANNs sem filtro · critério 2 · **Boat, Water vehicle** · 0,51 · 1 janela

**Segunda escuta, depois de ler:** música ao fundo, voz e disco girando nos 2 segundos finais

**Categoria:** 4

**Surpresa (critério da fase 1):** não

**Observações:** O trecho está no fim do evento 5.13, com música ao fundo, a voz e o giro do disco nos últimos segundos. O rótulo “Boat, Water vehicle” não corresponde a nenhum som de água ou de embarcação. A coincidência com o tema da faixa, a chegada das naus, é apenas do ouvinte, já que o modelo opera só sobre o som.
