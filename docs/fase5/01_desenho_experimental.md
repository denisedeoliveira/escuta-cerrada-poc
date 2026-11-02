# Desenho experimental da fase 5

Registro fechado em 02/11/2026, antes de qualquer chamada ao LLM com dados do corpus. As escolhas abaixo valem para todas as chamadas e medições da fase. Qualquer alteração posterior será registrada no diário da fase, com data e motivo, sem apagar este texto.

## 1. Pergunta

Um LLM que recebe apenas as saídas dos modelos das fases 3 e 4, sem o áudio e sem as referências humanas, consegue produzir um dossiê de escuta que indique onde vale escutar, com marcação de tempo, fonte e grau de apoio, sem interpretar e sem inventar? E quanto do que a escuta registrou, e do que as escutas dirigidas das fases 3 e 4 classificaram como útil, esse dossiê alcança?

## 2. Modelo e parâmetros

- **Modelo.** `gemini-3.8-flash`, do Google, acessado pela API do Google AI Studio com a biblioteca `google-genai`, executada no Google Colab. O identificador exato e a versão da biblioteca ficam gravados em cada chamada.
- **Temperatura.** Valor padrão do modelo (1,0). A documentação do Google desaconselha valores menores nos modelos Gemini 3 e posteriores, por risco de repetição em laço e de piora das respostas. Como a temperatura padrão introduz variação, a estabilidade passa a ser medida por repetição (seção 6).
- **Demais parâmetros.** Valores padrão, com saída estruturada em JSON segundo o esquema da seção 5.
- **Chave de acesso.** Guardada apenas nos Secrets do Colab, com o nome `GEMINI_API_KEY`. O repositório recebe um `.env.example` com o nome da variável, sem valor.
- **Política de dados.** Na camada gratuita da API, o Google declara que pode usar o conteúdo enviado para aprimorar seus produtos. Por isso só são enviados dados que já estão publicados no repositório, ou seja, as saídas dos modelos em JSON, sem áudio, sem as transcrições de referência, sem a tabela de eventos e sem as escutas. A alternativa seria a camada paga, em que o conteúdo não é usado, com custo provavelmente inferior a um dólar para toda a fase.

## 3. Entrada

Para cada faixa, o caderno 5a monta um arquivo de entrada (`resultados/fase5/entradas/faixaNN.json`) com três blocos. Cada item recebe um identificador (por exemplo, `F-012` para fala, `P-003` para PANNs e `C-007` para CLAP), que o LLM deve citar.

**Fala.** Os segmentos do Whisper na condição A (sem glossário e sem filtro), com início, fim, texto e os indicadores do próprio modelo (`avg_logprob`, `no_speech_prob`, `compression_ratio`). A condição A é a que um acervo obteria ao aplicar a ferramenta tal como é distribuída, e inclui os loops que o dossiê precisa sinalizar. Cada segmento traz quatro sinais calculados pelo caderno.
- **Repetição.** O mesmo texto aparece em três ou mais segmentos da faixa.
- **Indicação de ausência de fala.** `no_speech_prob` acima de 0,6, critério já usado na fase 3.
- **Baixa confiança.** `avg_logprob` abaixo de −1,0.
- **Divergência entre transcrições.** Menos da metade das palavras do segmento aparece na transcrição da condição C (com filtro) no mesmo intervalo. A condição C foi escolhida como contraste por ter a menor taxa de erro global e por ser a única que escapou do loop da faixa 05.

**Eventos (PANNs).** Rótulos com probabilidade de pelo menos 0,3 na condição sem filtro, com as janelas consecutivas do mesmo rótulo reunidas num intervalo, e a probabilidade máxima. Os rótulos apontados em mais da metade das janelas da faixa (como “Speech” nas faixas de fala) não entram como itens e são informados numa linha de resumo. A condição com filtro fica de fora, porque produz rótulos que correspondem a alterações da própria filtragem (fase 4, categoria 5).

**Descrições (CLAP).** A descrição em primeiro lugar em cada janela, na condição sem filtro, com as janelas consecutivas reunidas num intervalo. Ficam de fora as descrições que entram entre as três primeiras em mais de um quarto das janelas da faixa, porque funcionam como atratores e não distinguem nada (fase 4, seção 8).

**O que o LLM não recebe.** O áudio, o título e a descrição das faixas, as transcrições de referência, a tabela de eventos, as escutas e os resultados das fases anteriores. Cada faixa é identificada apenas pelo número e pela duração. O título poderia levar o modelo a interpretar, como na coincidência entre “Boat, Water vehicle” e o tema das naus na faixa 05 (fase 4, trecho 34).

## 4. Instrução de sistema

O texto completo está no anexo A e será versionado no repositório antes da primeira chamada. Ele estabelece que o modelo deve indicar momentos para escuta com base apenas nos itens da entrada, citar os identificadores de cada indicação e descrever o que os modelos registraram, e não o que soa. Proíbe interpretar sentido, intenção, ironia, emoção, gênero, tema ou contexto histórico, e limita os motivos e os graus de apoio às listas fixadas.

**Grau de apoio.** Para evitar a palavra “confiança”, que sugeriria que o LLM sabe se o som existe, cada indicação recebe um grau de apoio nas fontes, segundo a regra abaixo.
- **Alto.** Dois ou mais itens de fontes diferentes (fala, PANNs, CLAP) coincidem no intervalo, ou um rótulo do PANNs tem probabilidade de pelo menos 0,5.
- **Médio.** Um único item do PANNs entre 0,3 e 0,5, ou um único segmento de fala com algum dos quatro sinais.
- **Baixo.** Apenas uma descrição do CLAP.

## 5. Saída

O modelo devolve um JSON com uma lista de indicações. Cada indicação tem início e fim (em segundos), os identificadores das fontes, um motivo, um grau de apoio e uma frase sobre o que verificar na escuta.

**Motivos possíveis.** Repetição na transcrição, texto com indicação de ausência de fala, transcrição com baixa confiança, divergência entre transcrições, evento sonoro apontado, coincidência entre fontes e rótulo isolado (que aparece uma única vez na faixa).

O dossiê de cada faixa (`resultados/fase5/dossies/faixaNN.md`) é montado pelo código a partir desse JSON, em ordem de tempo, e não redigido pelo LLM. Assim, os tempos e as fontes do dossiê são os mesmos da saída verificada.

## 6. Execuções

- **Teste de funcionamento.** Antes das execuções, uma chamada com uma entrada fictícia, de dados inventados e fora do corpus, confere a conexão, o esquema e o registro. Ela fica salva, mas não entra nas medidas.
- **Chamadas.** As cinco faixas, três vezes cada, num total de quinze chamadas, com a mesma entrada e os mesmos parâmetros.
- **Registro.** Cada chamada é salva em `resultados/fase5/chamadas/` com modelo, parâmetros, instrução, entrada, resposta, tempo de resposta e número de tokens de entrada e de saída.

## 7. Medidas

1. **Conformidade.** Proporção de indicações com início, fim, fonte, motivo e grau de apoio válidos, verificada por teste automático (`tests/test_dossie.py`).
2. **Invenção.** Indicações que citam identificadores inexistentes, ou cujo intervalo fica fora do intervalo das fontes citadas, com tolerância de 1 segundo.
3. **Restrição.** Ocorrência, nas frases das indicações, de vocabulário interpretativo de uma lista fixada (ironia, irônico, emoção, emocionado, sentimento, triste, alegre, entusiasmo, intenção, pretende, quer dizer, significa, simboliza, representa, sugere que, revela), verificada pelo teste automático e completada pela leitura da seção 8.
4. **Coerência do grau de apoio.** Proporção de indicações cujo grau corresponde à regra da seção 4, conferida pelo código a partir das fontes citadas.
5. **Estabilidade.** Proporção de indicações que se repetem nas três chamadas de cada faixa, com o mesmo motivo e sobreposição de tempo.
6. **Cobertura.** Proporção dos 44 eventos da tabela de referência da fase 4 alcançados por alguma indicação, e proporção dos trechos das escutas dirigidas das fases 3 e 4 alcançados, separada pela categoria que cada trecho recebeu (por exemplo, os trechos da fase 4 em que o rótulo correspondia a um som presente, nas categorias 1 a 3, e os trechos sem som correspondente, na categoria 4).
7. **Faixa 05.** Comparação das indicações com as doze passagens da escuta cega da fase 1.
8. **Tempo e custo.** Tempo de resposta e tokens de cada chamada, com o custo equivalente calculado pela tabela de preços da camada paga na data da execução.

## 8. Leitura e escuta de conferência

- **Leitura.** A pesquisadora lê os dossiês das cinco faixas e marca as frases que interpretam, ainda que sem usar o vocabulário da lista, e as que afirmam a presença de um som em vez de relatar o que o modelo registrou.
- **Escuta.** As indicações que não se sobrepõem a nenhum evento da tabela de referência nem a nenhum trecho das escutas dirigidas anteriores são escutadas pela pesquisadora, em dois tempos, primeiro o intervalo sem ler a indicação e depois com a leitura. Aplica-se o critério de surpresa da fase 1.

## 9. Expectativas

Preenchidas pela pesquisadora em 02/11/2026, antes da primeira chamada, como na fase 1.

**O LLM vai respeitar a proibição de interpretar? Em que tipo de indicação você espera que ele falhe?**

Não irá respeitar a proibição de interpretar, apontando que um som está presente (“há aplausos”) em vez de relatar o que o modelo registrou, além de nomear o que o som seria (“sino de igreja”) ou atribuir sentido narrativo à gravação. Além de interpretar, estou pessimista quanto à capacidade de indicar grau de apoio, atribuindo graus que não seguem a regra.

**Ele vai criar indicações sem fonte?**

Sim, em grande parte dos casos, assinalando identificadores inexistentes e tempos fora do intervalo das fontes citadas.

**Ele vai sinalizar o loop “A CIDADE NO BRASIL” da faixa 05?**

Provavelmente, não. Mesmo com o sinal de repetição na entrada, ele não vai tratar o loop como possível invenção da transcrição.

**Na faixa 05, quais passagens da escuta cega você espera ver indicadas, e quais não?**

Indicadas: ruído de disco girando, música, som de sino. Trata-se de sons que entendo serem mais fáceis de captar, por suas características mais genéricas.

Não indicadas: vento, som de passos. Trata-se de sons que entendo serem mais difíceis de captar, por suas características mais específicas, mais facilmente confundíveis.

**As três chamadas de cada faixa vão produzir indicações parecidas?**

Espero que sejam bem diferentes entre si, a ponto de cada chamada produzir um dossiê distinto.

**O que você consideraria uma surpresa genuína?**

O dossiê indicar, com fonte válida, um momento que nenhuma das escutas anteriores registrou e que eu reconheça como presente ao escutar o trecho indicado. Também seria surpresa o LLM cumprir integralmente a proibição de interpretar e não criar nenhuma indicação sem fonte.

**O que você consideraria confirmação do esperado?**

O dossiê interpretar o que os modelos registraram, afirmando a presença de sons ou atribuindo sentido à gravação, criar indicações sem fonte, atribuir graus de apoio que, preponderantemente, não seguem a regra e não sinalizar o loop da faixa 05. Na faixa 05, acertar o genérico (música, ruído de disco, sino) e falhar no específico (vento, passos).

## 10. Saídas

- `resultados/fase5/entradas/` · um arquivo de entrada por faixa.
- `resultados/fase5/chamadas/` · um JSON por chamada, mais o teste de funcionamento.
- `resultados/fase5/dossies/` · o dossiê de cada faixa, em Markdown, montado a partir da primeira chamada, com as indicações que se repetem nas três chamadas marcadas.
- `resultados/fase5/medidas/` · tabelas das medidas da seção 7.

## Anexo A · Instrução de sistema (texto proposto)

Você recebe as saídas de modelos automáticos aplicados a uma gravação sonora em disco. Você não tem acesso ao áudio. Sua tarefa é indicar a uma pesquisadora os momentos da gravação em que vale escutar com atenção, com base apenas nos itens da entrada.

1. Cada indicação deve citar os identificadores dos itens da entrada que a sustentam. O início e o fim da indicação devem ficar dentro do intervalo desses itens.
2. Descreva o que os modelos registraram, e não o que soa. Por exemplo, escreva “o modelo de fala escreveu o mesmo texto em seis segmentos seguidos” ou “o detector de eventos atribuiu 0,82 ao rótulo Applause”, e não “há aplausos” ou “o orador repete a frase”.
3. Não interprete sentido, intenção, ironia, emoção, gênero, tema ou contexto da gravação, e não deduza o que ela representa.
4. Use apenas os motivos da lista fornecida e atribua o grau de apoio segundo a regra fornecida.
5. Se um trecho não tiver nada a indicar, não crie indicação para ele.
6. A frase de cada indicação deve dizer o que a pesquisadora pode verificar na escuta, em uma ou duas frases, em português.
