# Sistema de Inspeção Visual Automática — Classificação de Frutas

Pipeline clássico de visão computacional para classificar frutas **fresh vs rotten**.

## Estrutura

```
projetoVisaoComputacional/
├── data/                  # imagens organizadas por classe
│   ├── fresh/
│   └── rotten/
├── notebooks/
│   ├── 01_segmentacao.ipynb
│   ├── 02_features.ipynb
│   └── 03_classificacao.ipynb
├── outputs/               # figuras, métricas, X.csv, y.csv
├── requirements.txt
└── README.md
```

## Como executar

```bash
pip install -r requirements.txt
jupyter notebook
```

Execute os notebooks na ordem: `01` → `02` → `03`.

## Dataset

[Fruit Quality Detection — Kaggle](https://www.kaggle.com/datasets/shashwatwork/fruitnet-indian-fruits-dataset-with-quality)

Baixe e coloque as imagens em `data/fresh/` e `data/rotten/`, com ~100 imagens por classe.
