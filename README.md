# Sistema de Inspeção Visual Automática — Classificação de Frutas

Pipeline clássico de visão computacional para classificar frutas como **fresh** (frescas) ou **rotten** (podres), cobrindo maçã, banana e laranja.

Projeto final da disciplina de **Visão Computacional** — Universidade Positivo  
**Equipe:** Luiz Lopes, Pedro Rossi, Luiz Athar

---

## Estrutura do repositório

```
Sistema_inspecao_visual/
├── data/
│   ├── fresh/             # imagens de frutas frescas
│   └── rotten/            # imagens de frutas podres
├── notebooks/
│   ├── 01_segmentacao.ipynb    # comparação HSV vs Otsu
│   ├── 02_features.ipynb       # extração e análise de features
│   └── 03_classificacao.ipynb  # KNN e Random Forest + métricas
├── outputs/               # figuras, matrizes de confusão, X.csv, y.csv
├── organizar_dataset.py   # script para organizar imagens do Kaggle
├── requirements.txt
└── README.md
```

---

## Como executar

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Preparar o dataset

Baixe o dataset [Fruits Fresh and Rotten for Classification](https://www.kaggle.com/datasets/sriramr/fruits-fresh-and-rotten-for-classification) do Kaggle e extraia dentro de `data/dataset/`. Depois rode:

```bash
python organizar_dataset.py
```

Isso cria `data/fresh/` e `data/rotten/` com 100 imagens por classe, balanceadas.

### 3. Rodar os notebooks

```bash
jupyter notebook
```

Execute na ordem: `01_segmentacao` → `02_features` → `03_classificacao`.

---

## Pipeline

```
Imagem RGB
    ↓
Segmentação (HSV com fallback Otsu)
    ↓
Extração de features manuais
    │ forma: área, perímetro, excentricidade, solidez, extensão, circularidade
    │ momentos de Hu (7, escala log)
    │ cor: média e desvio HSV (6 features)
    │ textura: GLCM — contraste, homogeneidade, energia, correlação
    ↓
Tabela X.csv + y.csv
    ↓
Classificação (KNN e Random Forest)
    ↓
Avaliação: acurácia, F1, matriz de confusão, curva ROC
```

---

## Resultados

| Modelo        | Acurácia | F1-score (weighted) |
|---------------|----------|----------------------|
| KNN           | 96,50%   | 96,69%               |
| Random Forest | 98,76%   | **98,62%**           |

**Modelo escolhido para produção: Random Forest** — melhor desempenho em todas as métricas, robusto a outliers e produz importância de features como subproduto.

---

## Dependências principais

- Python 3.9+
- opencv-python
- scikit-image
- scikit-learn
- pandas, numpy
- matplotlib, seaborn
- jupyter
