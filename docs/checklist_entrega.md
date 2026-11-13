# Checklist de entrega

Lista de controle do TCC, montada a partir de quatro fontes: as orientações de entrega do curso (apresentação "Projeto Final", Prof. Manoela Kohler), o modelo de README da PUC-Rio, a rubrica de avaliação da disciplina do orientador e o plano de trabalho da PoC. Cada item traz a fonte entre parênteses quando não vem do plano.

Legenda: `[x]` feito · `[ ]` a fazer · **(confirmar)** depende de resposta do orientador

---

## Calendário

Meta: tudo pronto até a primeira quinzena de novembro e defesa na segunda quinzena, em data escolhida pela aluna (orientação de 23/10; 20/11 é feriado nacional).

| Etapa | Período | Release |
|---|---|---|
| Fase 1 · Corpus e registro prévio | concluída | `v0.1-fase1` |
| Fase 2 · Primeiro contato técnico | concluída | `v0.2-fase2` |
| Fase 3 · Reconhecimento de fala e medição | concluída (09 a 13/10) | `v0.3-fase3` |
| Fase 4 · Eventos sonoros | concluída (19 a 23/10) | `v0.4-fase4` |
| Contato com o orientador (andamento e dúvidas) | feito (23/10) | |
| Fase 5 · Síntese e restrição | concluída (30/10 a 13/11) | `v0.5-fase5` |
| Fase 6 · Formalização | a partir de 14/11 | `v1.0-final` |
| Defesa com o orientador | segunda quinzena de novembro | |

---

## 1. Entrega formal

- [x] Tema definido e orientador aceito (Leonardo Alfredo Forero Mendoza)
- [ ] Marcar a data da defesa com o orientador. Em 23/10, ele deixou a data a critério da aluna, na segunda quinzena de novembro. A defesa consiste em mostrar o trabalho funcionando e na revisão do README nas condições exigidas pela PUC
- [x] Linha do modelo de README que cita a disciplina “Projetos de Sistemas Inteligentes de Apoio à Decisão”. Resposta do orientador (23/10): trocar pelo nome do curso
- [x] Repositório público no GitHub (PROJ), aberto em 23/10
- [ ] Tag da versão final `v1.0-final`
- [ ] Aprovação do orientador (PROJ)
- [ ] E-mail para secretaria@ica.ele.puc-rio.br com cópia para o orientador, informando nome completo, turma, matrícula, título do projeto e link do repositório, e dizendo que o orientador aprovou o trabalho (PROJ)
- [ ] Assinatura da ata e envio dos documentos que a secretaria pedir (PROJ)

## 2. README final (modelo PUC-Rio)

O README é o trabalho escrito. Não há monografia à parte.

- [ ] Título definitivo
- [ ] Aluna e orientador com link para o perfil no GitHub (verificar se o orientador tem perfil)
- [ ] Frase de apresentação ao curso Inteligência Artificial Generativa & Large Language Models, com link, no lugar do nome de disciplina do modelo
- [ ] Link para o código
- [ ] Linha da monografia removida
- [ ] Trabalhos relacionados (opcional)
- [ ] Resumo (Abstract opcional)
- [ ] 1. Introdução, com problema, pessoa usuária, tarefa e critério de sucesso declarados (rubrica, "valor do domínio")
- [ ] 2. Modelagem, com a arquitetura das quatro camadas, um diagrama e as decisões técnicas (soma dos canais, JSON por execução, prompt restritivo) (rubrica, "multimodalidade")
- [ ] 3. Resultados, com WER, termos críticos, eventos sonoros, divergências e dossiê (rubrica, "avaliação")
- [ ] 4. Conclusões, com os limites encontrados
- [ ] 5. Referências
- [ ] 6. Instalação e 7. Como executar, incluindo como pedir acesso ao corpus no Zenodo e o aviso de que o caderno de análise roda só com os JSON do repositório (rubrica, "engenharia")
- [ ] Política de dados, ou seja, onde estão os áudios, por que não estão no repositório e o que o repositório contém (rubrica, "segurança")
- [ ] Declaração do uso de IA no desenvolvimento, com onde e como foi usada (contrato da disciplina)
- [ ] Matrícula
- [ ] Todos os comentários de orientação do modelo removidos (modelo PUC)

## 3. Engenharia do repositório

- [x] `.gitignore` bloqueando áudio e `.env`
- [x] `docs/` com as decisões de cada fase
- [x] Releases `v0.1-fase1`, `v0.2-fase2`, `v0.3-fase3`, `v0.4-fase4` e `v0.5-fase5`
- [x] Cadernos publicados sem saídas de áudio
- [x] `requirements.txt` com as versões das bibliotecas (fases 3, 4 e 5)
- [x] Pasta para os cadernos e pasta para os resultados em JSON (fase 3)
- [ ] Mensagens de commit no formato `tipo(escopo): mudança`, por exemplo `feat(asr): transcreve as cinco faixas sem glossário` (rubrica)
- [x] `.env.example` só com os nomes das variáveis (fase 5) (rubrica)
- [x] Chave de API só nos Secrets do Colab, nunca no código, em captura de tela ou no histórico, conferido nos cadernos e nos registros da fase 5. Revisão final na fase 6. **Item eliminatório** (rubrica)
- [x] `tests/` com os testes do WER e da normalização (fase 3), da comparação de eventos (fase 4) e das entradas e medidas do LLM (fase 5)
- [x] Teste da restrição do LLM, conferindo que toda indicação traz marcação temporal, fonte e grau de apoio (fase 5)

## 4. Fases

### Fase 3 · Reconhecimento de fala e medição

- [x] Experimentos fixados antes de rodar (sem e com vocabulário de domínio × sem e com filtragem)
- [x] Whisper nas cinco faixas, com cada execução salva em JSON junto com modelo e parâmetros
- [x] WER calculado contra `ref_faixa01` a `ref_faixa05`
- [x] Termos críticos contados como mantidos, substituídos, omitidos ou inventados
- [x] Casos de falha documentados com marcação temporal
- [x] Tabela comparativa dos experimentos
- [x] Escuta dirigida dos trechos selecionados
- [x] Diário da fase
- [x] Release `v0.3-fase3`

### Fase 4 · Eventos sonoros

- [x] Tabela de eventos de referência e desenho experimental registrados antes das execuções
- [x] PANNs e CLAP nas mesmas faixas, com saídas em JSON
- [x] Cotejo entre os rótulos dos modelos e a taxonomia enunciada por Almirante
- [x] Comparação nas duas direções, entre o que os detectores apontaram e a escuta não registrou e o que a escuta registrou e nenhuma categoria nomeia
- [x] Escuta dirigida dos trechos apontados
- [x] `src/eventos.py` e `tests/test_eventos.py`
- [x] Diário da fase
- [x] Release `v0.4-fase4`
- [x] Contato com o orientador, levando o andamento e as perguntas marcadas como **(confirmar)** (23/10)

### Fase 5 · Síntese e restrição

- [x] Cadernos que leem só os JSON e não tocam no áudio (5a e 5b)
- [x] Divergências entre transcrições e entre modelos levadas à entrada do LLM como sinais (caderno 5a) e reunidas na tabela das indicações (`resultados/fase5/medidas/indicacoes.csv`)
- [x] Prompt de sistema restritivo, que proíbe inferir sentido, ironia, intenção e emoção e exige marcação temporal, fonte e grau de apoio (anexo A do desenho)
- [x] Cada chamada ao LLM salva com modelo, parâmetros e saída
- [x] Desenho experimental e expectativas registrados antes da primeira chamada ao LLM (02/11)
- [x] Latência e custo das chamadas registrados (rubrica)
- [x] Protocolo completo aplicado à faixa 05 e comparado com a escuta cega da fase 1
- [x] Dossiê de escuta das cinco faixas, com leitura e escuta de conferência pela pesquisadora
- [x] Diário da fase
- [ ] Release `v0.5-fase5`

### Fase 6 · Formalização

- [ ] Protocolo de escuta redigido como documento transferível (`docs/protocolo.md`)
- [ ] README final (seção 2 desta lista)
- [ ] Teste de reprodução, abrindo o repositório como outra pessoa e rodando o caderno de análise do zero
- [ ] Revisão de segurança, sem chave no código nem no histórico
- [ ] Roteiro da demonstração para a defesa, mostrando o trabalho funcionando e incluindo um caso de falha (rubrica e orientação de 23/10)
- [ ] Tag `v1.0-final`
- [ ] Envio ao orientador para aprovação

---

## Mudanças em relação ao plano de trabalho

- A monografia saiu, porque o curso confirmou que o README é o trabalho escrito.
- O calendário passou de doze para cerca de dez semanas, com a defesa prevista para a segunda quinzena de novembro.
- Entraram itens de engenharia que o plano não listava, vindos da rubrica do orientador: `requirements.txt`, `tests/`, `.env.example`, declaração do uso de IA, registro de latência e custo e roteiro de demonstração.
- Na fase 5, as chamadas ao LLM passaram da camada gratuita à camada paga da API em 03/11, por causa do limite diário de chamadas (custo total de US$ 0,60), conforme a alternativa prevista no desenho.
- A síntese de voz saiu da entrega em 23/10, por orientação do orientador, para quem a síntese em texto feita pelo LLM é suficiente e a voz não deve entrar nesta primeira entrega. Os argumentos que a motivavam (acessibilidade e crítica ao visuocentrismo) passam ao README, como desdobramento, e aos artigos.
