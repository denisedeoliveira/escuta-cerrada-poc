# Diário da fase 2 · Primeiro contato técnico

Trabalho realizado entre 06 e 08/10/2026, registrado no caderno [`fase2_primeiro_contato.ipynb`](fase2_primeiro_contato.ipynb), cujas figuras estão em [`figuras/`](figuras/). Nenhum modelo de reconhecimento de fala ou de detecção de eventos sonoros foi executado nesta fase.

As leituras foram feitas pela pesquisadora com apoio do Claude (Anthropic), conforme declarado no projeto. Toda interpretação que depende de escuta foi conferida por ela nos áudios. As hipóteses levantadas apenas a partir das imagens e depois revistas estão registradas na seção 8, porque o percurso das correções também é resultado.

## 1. Os arquivos como último elo de uma cadeia de transformações

- Os cinco arquivos estão em estéreo, embora os discos de acetato de origem fossem monofônicos.
- Nas faixas 01 a 04, os dois canais diferem bastante (correlação entre −0,53 e 0,37), o que é compatível com uma transferência feita com agulha estereofônica, capaz de ler separadamente as duas paredes do sulco. Na faixa 05, os canais são cópias do mesmo sinal (correlação de 1,0), de modo que essa cópia derivou de uma fonte monofônica e passou por uma cadeia de transformações distinta da das demais.
- Os formatos variam. As faixas 01 e 03 estão em MP3 a 320 kbps, as faixas 02 e 04 em WAV sem compressão (48 kHz, 24 bits), e a faixa 05 em MP4 com áudio HE-AAC a 52 kbps.
- Na faixa 05, o Windows declara taxa de amostragem de 22,05 kHz, e o ffprobe lê 44,1 kHz. A diferença decorre da variante HE-AAC, que codifica apenas parte das frequências e prevê a reconstrução estimada das demais na reprodução. O espectrograma, porém, não mostra nenhuma energia acima de cerca de 4,5 kHz, nem sequer o ruído de superfície presente em todas as outras faixas. O efeito da compressão dessa cópia foi a supressão dos agudos.
- Na faixa 04, uma linha fina e ondulada entre 17 e 19 kHz, inaudível, corresponde provavelmente a ruído eletrônico do equipamento de digitalização, já que a gravação de 1944 não registrava frequências tão altas.
- Na faixa 05, uma linha fraca entre 100 e 200 Hz atravessa a gravação inteira, inclusive antes da entrada da música, o que indica origem no equipamento de gravação ou de digitalização, e não no conteúdo encenado.

## 2. Decisão metodológica sobre a entrada dos modelos

Cada faixa foi decomposta na soma dos canais, que equivale à média usada pelos modelos ao converter o áudio para mono, e na diferença entre eles.

| Faixa | Energia da soma | Energia da diferença |
|---|---|---|
| 01 | −20,4 dB | −17,5 dB |
| 02 | −23,8 dB | −24,7 dB |
| 03 | −27,8 dB | −22,8 dB |
| 04 | −20,2 dB | −23,6 dB |
| 05 | −22,7 dB | −88,4 dB |

Nas faixas 01 e 03, a diferença tem mais energia que a soma. A escuta das quatro versões (canal esquerdo, canal direito, soma e diferença) mostrou que a voz, o grito de "muito bem!" e os aplausos estão na soma, enquanto a diferença contém sobretudo o giro e o chiado do disco. Os aplausos deixam algum resíduo na diferença, por serem sons fortes e de banda larga.

Os modelos receberão, portanto, a soma dos canais. Essa escolha tem uma consequência para o experimento das fases seguintes, já que a condição "sem filtro" exclui de antemão a parte do ruído de superfície que está na diferença. Antes de qualquer decisão consciente de tratar o áudio, o formato de entrada dos modelos já seleciona o que conta como sinal.

## 3. Limites de frequência

Os espectrogramas mostram dois tipos de limite superior, um da cadeia de gravação dos anos 1940 e outro da digitalização.

| Faixa | Limite da gravação (energia da voz e da música) | Limite da digitalização |
|---|---|---|
| 01 | cerca de 3 kHz | corte do codificador MP3 em cerca de 16 kHz |
| 02 | cerca de 1 a 1,5 kHz | nenhum (WAV) |
| 03 | cerca de 4 kHz | corte do codificador MP3 em cerca de 16 kHz |
| 04 | cerca de 2 a 4 kHz | nenhum (WAV) |
| 05 | cerca de 2,5 kHz, com fragmentos até 4,5 kHz | nada acima de cerca de 4,5 kHz (HE-AAC) |

Na faixa 01, voz e aplausos são interrompidos no mesmo limite, embora palmas produzam, fora da gravação, energia em frequências muito mais altas. O limite pertence, assim, à cadeia de gravação, e não às fontes sonoras.

## 4. Como os sons aparecem no espectrograma

| Som | Aparência | Onde foi observado |
|---|---|---|
| Voz próxima do microfone | listras horizontais nítidas, regulares e empilhadas (vogais), interrompidas brevemente nas consoantes e por mais tempo nas pausas | Vargas (01), policial (03) |
| Vozes de multidão, distantes | arcos fracos e salpicados sobre fundo roxo | "muito bem!" (01) |
| Aplauso | mancha densa e uniforme, sem listras, como um traço de giz de cera; na forma de onda, contorno contínuo que cresce e decresce | 01 |
| Instrumento de percussão afinado | linha horizontal tracejada, um traço por batida | primeiro tamborim (04) |
| Percussão sem afinação nítida | energia espalhada numa faixa larga, com batidas cerradas | segundo tamborim (04) |
| Música | traços horizontais retos e sustentados, dispostos em degraus que acompanham a melodia | 05 |
| Sino | conjunto de traços horizontais simultâneos e prolongados | 05, a partir de 3:52 |
| Vento | nuvem difusa, sem traços, que cresce e diminui lentamente | 05 |
| Passos | riscos verticais regularmente espaçados | 05, 4:20 |
| Estalos do disco | linhas verticais finas que atravessam todas as frequências; picos isolados na forma de onda | todas as faixas |
| Ruído de superfície | névoa roxa contínua em toda a imagem | 01 a 04 |

## 5. Escuta e representação

- **Folheio (faixa 03).** A virada de página aparece como uma pausa da voz entre 4:14,9 e 4:17,15. Os dois ruídos de papel indicados pela escuta, em 4:15 e 4:16, coincidem com os dois traços de banda mais larga da pausa, por volta de 4:15,45 e 4:16,65, mas esses traços não se distinguem visualmente dos estalos do disco. A imagem localizou o papel apenas depois que a escuta indicou o que procurar.
- **Estalos (faixa 03).** Os picos mais altos da forma de onda são estalos de poucos milésimos de segundo, muito visíveis na imagem e quase imperceptíveis à escuta. A representação exagera o que o ouvido mal registra.
- **Tamborim (faixa 04).** A leitura da imagem atribuiu a linha tracejada ao surdo, e a escuta mostrou que se tratava do primeiro tamborim. A representação localiza padrões rítmicos, mas não identifica sozinha os instrumentos que os produzem.
- **Controle de intensidade (faixa 04).** Sempre que Almirante fala, o instrumento que soa ao fundo diminui de volume, o que a escuta percebe como recuo e a imagem registra como esmaecimento do tracejado. Trata-se de um gesto de produção da gravação.
- **Ruído e declamação (faixa 02).** Entre 1:30 e 2:16, a forma de onda se torna mais intensa. A escuta mostrou que o aumento corresponde ao ruído do disco, e não a uma mudança na declamação, com um pequeno pulo no meio do trecho.
- **Sino (faixa 05).** O som metálico começa em 3:52, exatamente o tempo registrado na escuta cega da fase 1. A escuta também separou o fim enfático de "triunfal", em 3:50, do início do sino, dois segundos que a imagem da faixa inteira não distingue.
- **Passos (faixa 05).** Os quatro riscos verticais regularmente espaçados em 4:20 favorecem a hipótese de passos, frente à de uma porta batendo, dúvida registrada na escuta cega. É o primeiro caso em que a representação contribui para resolver uma dúvida deixada em aberto pela escuta.
- **Zumbido (faixa 05).** A linha entre 100 e 200 Hz não consta da escuta cega e só passou a ser percebida depois de localizada no espectrograma. É o primeiro caso, no projeto, de uma representação computacional que dirige a atenção da escuta para algo antes não registrado. Como o espectrograma não é a saída de um modelo de classificação, o caso não se enquadra no critério de surpresa definido na fase 1, mas pertence ao mesmo tipo de fenômeno que o protocolo pretende examinar.

## 6. Velocidade de rotação do disco das faixas 02 e 04

Entre 1:32 e 2:16 da faixa 02 ouvem-se estalos regulares, 26 em 20 segundos, produzidos por um defeito do disco que passa sob a agulha a cada volta. A autocorrelação dos impactos no mesmo trecho mede um período de 0,77 s, com picos também em 1,54 s e 2,31 s (duas e três voltas), o que corresponde a 78 rotações por minuto. A conclusão foi alcançada por dois caminhos independentes, a contagem de ouvido e o cálculo, e a escuta indicou onde procurar e qual era o fenômeno.

A digitalização reproduziu o disco das faixas 02 e 04 a 78 rpm, e a altura natural das vozes indica que essa era também a velocidade de gravação. As faixas 01 (5:35) e 05 (7:21) são longas demais para um lado de disco comum de 78 rpm, e a velocidade em que foram gravadas permanece em aberto.

## 7. Tempos citados na dissertação

- **Faixa 01.** O "muito bem!" de 2:19 ocorre exatamente nesse ponto do arquivo, de modo que o áudio usado na dissertação não sofreu recorte.
- **Faixa 02.** A parte "Meio-dia" começa por volta de 1:25, como registrado na dissertação.
- **Faixa 03.** A dissertação situa o folheio entre 0:18 e 0:19, e no arquivo completo ele ocorre entre 4:14 e 4:17. O áudio da dissertação era um recorte, e os tempos citados ali não valem para o arquivo de trabalho.

## 8. Hipóteses revistas

- A variante HE-AAC da faixa 05 levou à previsão de agudos reconstruídos pelo decodificador acima de 11 kHz. O espectrograma mostrou ausência total de energia acima de 4,5 kHz.
- O corte em cerca de 16 kHz da faixa 03 foi inicialmente lido como limite do disco. Trata-se do codificador MP3, e o limite da gravação está em cerca de 4 kHz.
- As variações regulares de intensidade na pausa da faixa 03, entre 4:15 e 4:17, foram atribuídas ao giro do disco. A escuta mostrou que coincidem com o manuseio do papel.
- A linha tracejada da faixa 04 foi atribuída ao surdo. A escuta mostrou que é o primeiro tamborim.
- Um deslocamento de cerca de 5 segundos foi suposto entre os tempos da dissertação e os do arquivo da faixa 01. O deslocamento resultava de comparar o centro das manchas de aplauso com o início do grito marcado na dissertação, e os tempos coincidem.
- A estimativa visual sugeria estalos regulares a cada 2 segundos na faixa 02. A contagem de ouvido e a autocorrelação deram 0,77 s.

## 9. Publicação do corpus

Os cinco arquivos de trabalho foram depositados no Zenodo, sem nenhuma alteração, com acesso restrito aos arquivos e registro público.

- DOI de todas as versões: [10.5281/zenodo.23240974](https://doi.org/10.5281/zenodo.23240974)
- DOI da versão 1.0: [10.5281/zenodo.23240975](https://doi.org/10.5281/zenodo.23240975)

O acesso é concedido mediante pedido, exclusivamente para fins de pesquisa. Os áudios continuam fora deste repositório, e o caderno da fase 2 foi enviado sem as saídas que continham tocadores de áudio. Quem tiver acesso aos arquivos pode executar o caderno e reproduzir todas as saídas.

## 10. Implicações para a fase 3

- Os modelos receberão a soma dos canais, e a condição "sem filtro" será declarada como já desprovida do ruído de superfície contido na diferença entre os canais.
- A faixa 05 não contém nenhuma informação acima de 4,5 kHz, o que deve pesar em qualquer comparação de desempenho entre as faixas, sobretudo nas consoantes sibilantes.
- Na faixa 02, a voz é a mais fraca em relação ao ruído e tem o limite de frequência mais baixo do corpus, o que deve ser considerado ao lado da aposta, registrada na fase 1, de que o pior desempenho ocorreria na faixa 04.
- Os pulos das faixas 02 e 04 e o recorte do áudio da dissertação na faixa 03 devem ser levados em conta no alinhamento entre transcrições de referência e saídas dos modelos, sempre pelos tempos do arquivo de trabalho.
