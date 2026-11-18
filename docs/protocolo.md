# Protocolo de escuta cerrada com mediação algorítmica

Este documento descreve o protocolo construído nas cinco fases deste repositório de modo que possa ser aplicado a outros registros sonoros de origem mecânica, por pesquisadoras e profissionais de acervo. Cada etapa remete à fase em que foi testada, onde estão os cadernos, os desenhos experimentais e os diários com os resultados e as decisões. As ferramentas usadas aqui (Whisper, PANNs, CLAP e Gemini) podem ser trocadas por outras do mesmo tipo, e o que o protocolo fixa é a ordem das etapas, os registros que cada uma exige e a divisão de papéis entre a máquina e quem escuta.

## Princípios

**A escuta é a base de comparação.** A escuta cerrada da pesquisadora não fornece rótulos para treinar ou corrigir a máquina. Ela é o termo contra o qual a máquina é comparada, e a decisão sobre o que soa cabe sempre a quem escuta.

**A divergência é um achado.** Quando a máquina e a escuta discordam, a discordância não é tratada como erro a eliminar, e sim como indicação do que cada representação seleciona como som. Os casos de divergência são descritos e classificados, e não apenas contados.

**Tudo o que pode orientar a leitura dos resultados é registrado antes.** As escutas de referência, as expectativas, o critério de surpresa e o desenho de cada experimento são fechados e datados antes de qualquer execução. As decisões tomadas depois entram num diário, com data e motivo, sem apagar o que foi registrado.

**A escuta dos resultados é feita em dois tempos.** Primeiro, o trecho é escutado sem a leitura do que a máquina indicou. Depois, com a leitura. O primeiro tempo só é cego se vier antes de qualquer contato com a indicação.

**A máquina indexa a atenção e não interpreta.** Os modelos indicam onde escutar, com tempo e fonte. A camada de linguagem recebe dados, e não áudio, e por isso não pode atribuir emoção, intenção ou sentido ao que não ouviu.

**Os dados ficam onde os direitos permitem.** Os áudios ficam fora do repositório, em depósito com acesso controlado. O repositório guarda as escutas, as referências, as saídas dos modelos e as medidas, de modo que as análises possam ser refeitas sem o áudio.

## Etapa 1 · Registro prévio

Antes de qualquer processamento, a pesquisadora registra a proveniência de cada arquivo (origem, suporte, digitalização, formato e restrições de uso) e escolhe ao menos uma gravação que ainda não conhece para uma escuta cega, anotada com os tempos de cada passagem e do que nela soa. Para as demais, prepara transcrições literais, com convenções explícitas para hesitações, trechos inaudíveis, marcas de som e números, e uma lista de termos críticos, como nomes próprios, palavras regionais e termos da época. Também monta uma tabela dos eventos sonoros que a escuta registra, com início, fim, classe e fonte, incluindo os de duração e intensidade, como pausas, viradas de página, pulos do disco e variações de volume.

Por fim, registra as expectativas sobre o comportamento dos modelos e um critério de surpresa, numa frase que diga, antes do fato, o que contaria como a máquina ter apontado algo que a escuta não registrou. Neste trabalho, o critério foi “a máquina apontar um evento, com marcação de tempo, que não consta na minha tabela nem na análise da dissertação, e que eu reconheço como presente no áudio ao reescutar o trecho indicado”. Todo esse material é versionado e datado antes da etapa seguinte ([fase 1](fase1/README.md)).

## Etapa 2 · Primeiro contato técnico

Antes de rodar os modelos, a pesquisadora examina os arquivos como último elo de uma cadeia de transformações. Confere taxa de amostragem, formato e compressão, compara os canais e observa espectrogramas e formas de onda, sempre ao lado da escuta. A decisão sobre o que os modelos vão receber é tomada aqui e declarada. Neste corpus, os discos eram monofônicos e a transferência pôs a voz na soma dos canais e boa parte do ruído do disco na diferença, de modo que a escolha da soma já excluiu parte do ruído antes de qualquer filtro. As hipóteses feitas a partir das imagens e depois corrigidas pela escuta também entram no diário, porque mostram o que cada representação faz ver ([fase 2](fase2/diario.md)).

## Etapa 3 · Reconhecimento de fala

O modelo de reconhecimento de fala é aplicado em condições fixadas antes da execução, que combinem ao menos a presença e a ausência de um glossário de termos de domínio e de um filtro de ruído. Cada execução é gravada em arquivo próprio, com modelo, parâmetros, versões e os indicadores de confiança de cada segmento, e um teste de determinismo verifica se a repetição produz a mesma saída.

A medição compara o texto da máquina com as transcrições de referência pela taxa de erro de palavra, decomposta em substituições, omissões e inserções, porque taxas parecidas podem resultar de silêncio indevido ou de invenção. Os termos críticos são contados como mantidos, substituídos, omitidos ou inventados. Os trechos em que a máquina escreveu algo sem correspondência na referência vão para uma escuta dirigida em dois tempos, com categorias definidas no desenho, como fala real ausente da referência, fala real deformada, repetição, texto sobre som não verbal e texto sobre silêncio ou ruído ([fase 3](fase3/README.md)).

Os indicadores de confiança do modelo não servem como garantia. Neste corpus, o Whisper repetiu uma mesma frase por minutos, sobre música e sobre diálogo, com alta confiança nos próprios segmentos, e transcreveu bem versos que estimava não conterem fala.

## Etapa 4 · Eventos sonoros

Dois tipos de modelo são aplicados em janelas curtas e sobrepostas, sem e com filtro. Um detector de categorias fixas, como o PANNs, dá a probabilidade de cada categoria de uma ontologia, e um modelo que compara o áudio com descrições escritas, como o CLAP, ordena um vocabulário escolhido pela pesquisadora. Esse vocabulário inclui descrições dos eventos da tabela de referência, distratores e os termos com que a própria gravação nomeia seus sons, para testar se a máquina reconhece a taxonomia do acervo. Os critérios de apontamento e a correspondência entre rótulos e classes da tabela são registrados antes das execuções.

A comparação com a tabela de referência é feita nas duas direções, entre o que os detectores apontaram e a escuta não registrou e o que a escuta registrou e nenhum modelo nomeou. Os trechos apontados vão para uma escuta dirigida em dois tempos, rótulo por rótulo, com as categorias som presente e não registrado, som registrado fora dos tempos da tabela, som presente com outro nome, nenhum som correspondente, efeito do filtro e outro. A surpresa, pelo critério da etapa 1, só pode ser afirmada na primeira categoria ([fase 4](fase4/README.md)).

Um modelo que ordena descrições aponta sempre alguma coisa, e algumas descrições ficam no alto em quase toda a gravação. Essas descrições, os atratores, são identificadas pela frequência com que aparecem entre as primeiras e não podem ser lidas como detecção. O filtro de ruído é uma condição a examinar, e não um pré-processamento, porque altera ou apaga sons que têm sentido para a escuta, como aplausos, vento e papel.

## Etapa 5 · Síntese pelo LLM

**Entrada.** O LLM recebe apenas as saídas dos modelos, já publicadas, sem o áudio, sem o título ou a descrição das gravações e sem as referências humanas, para que não interprete a partir do contexto. Para cada gravação, um código monta um arquivo com três blocos (fala, eventos do detector e descrições do modelo de comparação), dá a cada item um identificador e acrescenta à fala sinais calculados, como repetição do mesmo texto, indicação de ausência de fala, baixa confiança e divergência entre duas transcrições feitas sob condições diferentes. Rótulos presentes em quase toda a gravação e atratores ficam de fora, com uma linha de resumo. Uma legenda descreve, sem interpretar, o que é cada campo.

**Instrução e saída.** A instrução de sistema pede que o modelo indique os momentos em que vale escutar, cite os identificadores que sustentam cada indicação, mantenha os tempos dentro dos tempos das fontes, descreva o que os modelos registraram e não o que soa, e não interprete sentido, intenção, ironia, emoção, gênero, tema ou contexto ([anexo A](fase5/01_desenho_experimental.md#anexo-a--instrução-de-sistema-texto-proposto)). A resposta segue um esquema estruturado com motivos e graus de apoio em listas fechadas. O grau de apoio mede quantas fontes coincidem e não deve ser chamado de confiança, porque não diz se o som existe.

**Dossiê.** O dossiê é montado pelo código a partir da resposta, em ordem de tempo, para que tempos e fontes não sejam reescritos. Cada gravação é enviada mais de uma vez com a mesma entrada, e o dossiê marca as indicações que se repetem.

**Conferência.** Um código confere, em todas as chamadas, a conformidade das indicações, a existência das fontes citadas, os tempos, o vocabulário interpretativo, a coerência do grau com a regra, a estabilidade entre chamadas e a cobertura dos eventos e das escutas anteriores. A pesquisadora lê os dossiês antes de ver essa conferência e marca as frases que interpretam ou que afirmam a presença de um som. As indicações que não coincidem com nenhum evento ou trecho já escutado vão para uma escuta de conferência em dois tempos, com o critério de surpresa. Cada chamada é gravada com modelo, versão, parâmetros, instrução, entrada, resposta, tempo e tokens ([fase 5](fase5/README.md)).

Neste corpus, o LLM cumpriu as regras sem nenhuma indicação inventada, mas não acrescentou nada que os modelos anteriores não tivessem registrado, e a medida de cobertura por sobreposição de tempo superestimou o alcance das indicações, que às vezes tratavam de outra coisa.

## Etapa 6 · Diário e confronto

Cada etapa termina com um diário que reúne os achados, as decisões posteriores ao desenho, o confronto item por item com as expectativas registradas, as limitações e as implicações para a etapa seguinte. Os casos em que uma representação computacional dirigiu a escuta para algo não registrado são descritos à parte, inclusive os que não cumprem o critério de surpresa, porque mostram tipos de contribuição que o critério não previa.

## Onde quem escuta decide

O protocolo reserva à escuta da pesquisadora as decisões que nenhuma etapa automática substitui. São dela a escolha do que entra na tabela de referência e nas transcrições, a classificação de cada trecho e de cada rótulo nas escutas dirigidas, a afirmação de uma surpresa, a leitura das frases do LLM e a decisão sobre o que soa em cada trecho indicado. Nas cinco fases deste trabalho, os sons de duração, de intensidade e de materialidade do suporte, como pausas, vento, viradas de página, pulos e variações de volume, ficaram inteiramente a cargo dessa escuta.

## Adaptação a outros acervos

O protocolo supõe acesso aos áudios em condições compatíveis com seus direitos de uso, um repositório versionado e tempo de escuta, que é a parte mais longa do trabalho. Para outro acervo, a língua das gravações, o glossário de domínio, o vocabulário do modelo de comparação e as categorias das escutas dirigidas precisam ser refeitos a partir do próprio material. Os serviços externos mudam sem aviso e têm limites de uso e custo, e por isso cada chamada deve ser gravada de modo que os dossiês e as medidas possam ser refeitos sem nova chamada. Neste trabalho, as quinze chamadas ao LLM custaram o equivalente a US$ 0,60 na camada paga da API, que também evita o uso do conteúdo enviado para aprimorar o serviço.
