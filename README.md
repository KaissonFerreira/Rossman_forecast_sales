![Screenshot](docs/capa.png)
---
# Previsão de vendas (Sales forecast)

> A Rossmann opera mais de 3.000 drogarias em 7 países europeus. Atualmente, os gerentes de loja da Rossmann têm a tarefa de prever suas vendas diárias com até seis semanas de antecedência. As vendas da loja são influenciadas por muitos fatores, incluindo promoções, competição, feriados escolares e estaduais, sazonalidade e localidade. Com milhares de gerentes individuais prevendo vendas com base em suas circunstâncias únicas, a precisão dos resultados pode ser bastante variada. Nesse sentido, o CFO pede a previsão de todas as lojas de forma antecipe a venda em até 6 semanas.

## 0.0 Questão de negócio
Qual é o valor das vendas de cada loja nas próximas 6 semanas?

## 1.0 Qual a motivação?
A previsão de vendas foi requisitada pelo CFO em uma reunião mensal sobre os resultados das lojas.

## 2.0 Qual a causa raiz do problema?
Dificuldade em determinar o valor do investimento para as reformas de cada loja.

## 3.0 Quem é o dono do problema?
Diretor financeiro (CFO) da Rossman.

## 4.0 Qual é o formato da solução?
* Granularidade: Previsão de vendas por dias e por loja os próximos 42 dias (6 Semanas)

* Tipo do problema: Previsão de vendas (Regressão)

* Potenciais métodos: Séries temporais e regressão com algumas modificações.

* Formato de entrega (3 itens):
    - O valor total das vendas no final das 6 semanas (Uma coluna com o código ID da loja e outra coluna com o valor de vendas).
    - A entrega será pelo celular (app).
    - Checagem diária.


# Project Organization

```
├── AUTHORS.md              <- List of developers and maintainers.
├── CHANGELOG.md            <- Changelog to keep track of new features and fixes.
├── CONTRIBUTING.md         <- Guidelines for contributing to this project.
├── LICENSE.txt             <- License as chosen on the command-line.
├── README.md               <- The top-level README for developers.
├── code                    
|     ├── configs                <- Directory for configurations of model & application.
|     ├── notebooks              <- Jupyter notebooks. Naming convention is a number (for
│     |                             ordering), the creator's initials and a description,
│     |                             e.g. `1.0-initial-data-exploration`.
|     ├── scripts                 <- Analysis and production scripts which import the
|     └──                              actual PYTHON_PKG, e.g. train_model.
├── data
│   ├── external            <- Data from third party sources.
│   ├── interim             <- Intermediate data that has been transformed.
│   ├── processed           <- The final, canonical data sets for modeling.
│   └── raw                 <- The original, immutable data dump.
├── docs                    <- Directory for documentation of the project in txt or docx.


```
