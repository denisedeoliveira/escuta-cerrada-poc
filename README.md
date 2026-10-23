# Close listening e mediação algorítmica

*Título provisório.*

Prova de conceito desenvolvida como trabalho de conclusão do curso de especialização em Inteligência Artificial Generativa & Large Language Models (PUC-Rio). O trabalho examina o que um pipeline de reconhecimento automático de fala e de detecção de eventos sonoros preserva e o que descarta quando aplicado a gravações fonográficas dos anos 1940 da Discoteca Pública do Distrito Federal, em contraste com a escuta cerrada de uma pesquisadora.

**Autora:** Denise S. de Oliveira

**Orientador:** Leonardo Alfredo Forero Mendoza

> Repositório em construção. Este README será substituído pelo modelo oficial do curso na entrega final.

## Corpus

Cinco gravações da primeira metade dos anos 1940, preservadas na Coleção da Discoteca Pública do Distrito Federal, sob guarda do Museu da Imagem e do Som do Rio de Janeiro (MIS-RJ). Os arquivos de áudio não integram este repositório. Estão depositados no Zenodo, sem alteração, com registro público e acesso aos arquivos restrito a fins de pesquisa, mediante pedido.

> de Oliveira, D. S. (2026). *Gravações dos anos 1940 da Discoteca Pública do Distrito Federal: corpus de áudio da prova de conceito "Close listening e mediação algorítmica"* [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.23240974

## Estrutura

- `docs/fase1/` · corpus, escuta prévia, referências humanas e expectativas, registrados antes de qualquer processamento (release `v0.1-fase1`).
- `docs/fase2/` · primeiro contato técnico com os áudios, com dados técnicos dos arquivos, espectrogramas, decisão sobre a entrada dos modelos e medição da velocidade de rotação (release `v0.2-fase2`).
- `docs/fase3/` · reconhecimento de fala com o Whisper em quatro condições, taxa de erro de palavra, termos críticos e escuta dirigida dos trechos em que a máquina escreveu algo sem correspondência na referência (release `v0.3-fase3`).
- `docs/fase4/` · detecção de eventos sonoros com o PANNs e o CLAP, sem e com filtro, comparação com a tabela de eventos registrada pela escuta, cotejo com a taxonomia de Almirante e escuta dirigida dos trechos apontados pelos detectores (release `v0.4-fase4`).
- `resultados/` · saídas dos modelos em JSON e tabelas de medidas, por fase.
- `src/` · funções reutilizadas pelos cadernos e testadas em `tests/`.
- `tests/` · testes automáticos (`python -m pytest -q tests`).
- `requirements.txt` · bibliotecas e versões usadas nos cadernos.
