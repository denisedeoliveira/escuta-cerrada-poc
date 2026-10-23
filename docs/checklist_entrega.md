# Checklist de entrega

Lista de controle do TCC, montada a partir de quatro fontes: as orientações de entrega do curso (apresentação "Projeto Final", Prof. Manoela Kohler), o modelo de README da PUC-Rio, a rubrica de avaliação da disciplina do orientador e o plano de trabalho da PoC. Cada item traz a fonte entre parênteses quando não vem do plano.

Legenda: `[x]` feito · `[ ]` a fazer · **(confirmar)** depende de resposta do orientador

---

## Calendário

Meta: tudo pronto até 16/11, defesa entre 18 e 30/11 (a data depende da agenda do orientador; 20/11 é feriado nacional).

| Etapa | Período | Release |
|---|---|---|
| Fase 1 · Corpus e registro prévio | concluída | `v0.1-fase1` |
| Fase 2 · Primeiro contato técnico | concluída | `v0.2-fase2` |
| Fase 3 · Reconhecimento de fala e medição | concluída (09 a 13/10) | `v0.3-fase3` |
| Fase 4 · Eventos sonoros | concluída (19 a 23/10) | `v0.4-fase4` |
| Contato com o orientador (resultados das fases 3 e 4) | 1ª semana de novembro | |
| Fase 5 · Síntese, restrição e voz | 01/11 a 10/11 | `v0.5-fase5` |
| Fase 6 · Formalização | 11/11 a 16/11 | `v1.0-final` |
| Defesa com o orientador | 18/11 a 30/11 | |

---

## 1. Entrega formal

- [x] Tema definido e orientador aceito (Leonardo Alfredo Forero Mendoza)
- [ ] Marcar a data da defesa com o orientador
- [ ] **(confirmar)** A linha do modelo de README que cita a disciplina "Projetos de Sistemas Inteligentes de Apoio à Decisão" vale para este curso ou é resto de modelo de outro curso? Conferir no README da colega que já defendeu
- [ ] Repositório público no GitHub (PROJ)
- [ ] Tag da versão final `v1.0-final`
- [ ] Aprovação do orientador (PROJ)
- [ ] E-mail para secretaria@ica.ele.puc-rio.br com cópia para o orientador, informando nome completo, turma, matrícula, título do projeto e link do repositório, e dizendo que o orientador aprovou o trabalho (PROJ)
- [ ] Assinatura da ata e envio dos documentos que a secretaria pedir (PROJ)

## 2. README final (modelo PUC-Rio)

O README é o trabalho escrito. Não há monografia à parte.

- [ ] Título definitivo
- [ ] Aluna e orientador com link para o perfil no GitHub (verificar se o orientador tem perfil)
- [ ] Frase de apresentação ao curso Inteligência Artificial Generativa & Large Language Models, com link
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
- [x] Releases `v0.1-fase1`, `v0.2-fase2` e `v0.3-fase3`
- [x] Cadernos publicados sem saídas de áudio
- [x] `requirements.txt` com as versões das bibliotecas (fase 3)
- [x] Pasta para os cadernos e pasta para os resultados em JSON (fase 3)
- [ ] Mensagens de commit no formato `tipo(escopo): mudança`, por exemplo `feat(asr): transcreve as cinco faixas sem glossário` (rubrica)
- [ ] `.env.example` só com os nomes das variáveis (fase 5) (rubrica)
- [ ] Chave de API só nos Secrets do Colab, nunca no código, em captura de tela ou no histórico. **Item eliminatório** (rubrica)
- [x] `tests/` com os testes do WER e da normalização (fase 3)
- [ ] Teste da restrição do LLM, conferindo que toda indicação traz marcação temporal e grau de confiança (fase 5)

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
- [ ] Release `v0.4-fase4`
- [ ] Contato com o orientador, levando os resultados e as perguntas marcadas como **(confirmar)**

### Fase 5 · Síntese, restrição e voz

- [ ] Segundo caderno, que lê só os JSON e não toca no áudio
- [ ] Tabela de divergências
- [ ] Prompt de sistema restritivo, que proíbe inferir sentido, ironia, intenção e emoção e exige marcação temporal e grau de confiança
- [ ] Cada chamada ao LLM salva com modelo, parâmetros e saída
- [ ] **(confirmar)** Manter a síntese de voz, que não é exigência formal do TCC (decisão atual é manter, por acessibilidade e pela crítica ao visuocentrismo)
- [ ] Síntese de voz com voz genérica do catálogo, sem clonagem de nenhuma voz real, e com aviso falado no início de que a voz é gerada por IA (rubrica)
- [ ] Texto do dossiê reescrito para leitura em voz, sem tabelas e com os tempos por extenso
- [ ] Latência e custo das chamadas registrados (rubrica)
- [ ] Protocolo completo aplicado à faixa 05 e comparado com a escuta cega da fase 1
- [ ] Dossiê de escuta das cinco faixas
- [ ] Diário da fase e release `v0.5-fase5`

### Fase 6 · Formalização

- [ ] Protocolo de escuta redigido como documento transferível (`docs/protocolo.md`)
- [ ] README final (seção 2 desta lista)
- [ ] Teste de reprodução, abrindo o repositório como outra pessoa e rodando o caderno de análise do zero
- [ ] Revisão de segurança, sem chave no código nem no histórico
- [ ] Roteiro da demonstração para a defesa, incluindo um caso de falha (rubrica)
- [ ] Tag `v1.0-final` e repositório público
- [ ] Envio ao orientador para aprovação

---

## Mudanças em relação ao plano de trabalho

- A monografia saiu, porque o curso confirmou que o README é o trabalho escrito.
- O calendário passou de doze para cerca de dez semanas, com a defesa prevista para a segunda quinzena de novembro.
- Entraram itens de engenharia que o plano não listava, vindos da rubrica do orientador: `requirements.txt`, `tests/`, `.env.example`, declaração do uso de IA, registro de latência e custo, aviso de voz sintética e roteiro de demonstração.
