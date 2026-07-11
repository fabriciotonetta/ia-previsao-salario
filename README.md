# 💰 IA Previsão Salário

Sistema de previsão de salário para profissionais de TI, construído com base em dados reais da Stack Overflow Developer Survey 2024. O projeto cobre o fluxo completo de um produto de dados: coleta e limpeza de dados, comparação de modelos de Machine Learning, API REST documentada, testes automatizados e integração contínua.

---

## 📌 Sobre o projeto

Este projeto responde a uma pergunta prática: **dado o perfil de um profissional de TI (país, experiência, cargo, formação, modelo de trabalho), qual salário anual esperar?**

Mais do que treinar um modelo, o objetivo foi construir algo que se pareça com um produto real — com API funcional, testes automatizados, pipeline de CI, e documentação completa das decisões técnicas tomadas ao longo do caminho.

---

## 🏗️ Arquitetura

Dados brutos (Stack Overflow Survey 2024)
│
▼
Limpeza e tratamento (pandas)
│
▼
Treino e comparação de modelos (scikit-learn)
│
▼
Modelo serializado (joblib)
│
▼
API REST (FastAPI) — endpoints /health e /predict
│
▼
Containerização (Docker)

---

## 🛠️ Tecnologias

- **Python 3.13**
- **Pandas / NumPy** — manipulação e limpeza de dados
- **Scikit-learn** — modelagem (Regressão Linear, Random Forest, Gradient Boosting)
- **FastAPI** — API REST com documentação automática (Swagger)
- **Pydantic** — validação de dados de entrada
- **Docker** — containerização da aplicação
- **Pytest** — testes automatizados
- **GitHub Actions** — integração contínua (CI)

---

## 📊 Dados

- **Fonte:** [Stack Overflow Annual Developer Survey 2024](https://survey.stackoverflow.co/2024/)
- **Volume inicial:** 65.437 respostas, 114 colunas
- **Após filtros de qualidade** (respondentes CLT full-time, com salário informado, outliers removidos por corte de percentil): **17.182 respostas, 8 colunas relevantes**

Detalhes completos da fonte e como reproduzir a coleta em [`dados/brutos/FONTE.md`](dados/brutos/FONTE.md).

---

## 🤖 Modelagem

Foram treinados e comparados três modelos de regressão:

| Modelo | MAE (USD) | RMSE (USD) |
|---|---|---|
| Regressão Linear | 28.981,59 | 42.549,79 |
| Random Forest | 30.125,79 | 45.031,14 |
| **Gradient Boosting** ✅ | **28.544,25** | **42.322,54** |

**Modelo escolhido:** Gradient Boosting, por apresentar o menor erro nas duas métricas avaliadas. A margem de ganho sobre a Regressão Linear foi pequena (~1,5%), o que sugere que a relação entre as variáveis e o salário é majoritariamente linear — uma leitura honesta dos dados, em vez de assumir que "modelo mais complexo é sempre melhor".

### 🔎 Insight: o peso da variável país

A análise de importância de variáveis revelou que `Country_United States of America` responde por **58% de todo o poder preditivo do modelo** — mais que todas as outras 68 variáveis combinadas.

Para validar essa observação, foi feito um experimento controlado: treinar o mesmo modelo **sem nenhuma informação de país**. Resultado: o erro (MAE) piora em **41,44%** (de USD 28.544 para USD 40.372), confirmando quantitativamente que a localização geográfica é o fator dominante na previsão salarial de TI — um reflexo real da disparidade salarial do mercado global.

---

## 🚀 API

A aplicação expõe dois endpoints principais:

### `GET /health`
Verifica se a API está no ar.

### `POST /predict`
Recebe os dados de um profissional e retorna a previsão de salário anual em USD.

**Exemplo de requisição:**
```json
{
  "Country": "Brazil",
  "YearsCodePro": 5,
  "DevType": "Developer, full-stack",
  "EdLevel": "Bachelor's degree",
  "RemoteWork": "Remote",
  "OrgSize": "100 to 499 employees"
}
```

**Exemplo de resposta:**
```json
{
  "salario_previsto_usd": 31182.56,
  "moeda": "USD"
}
```

Documentação interativa (Swagger) disponível em `/docs` quando a aplicação está em execução.

---

## ▶️ Como executar localmente

### Com Docker (recomendado)

```bash
docker build -t ia-previsao-salario .
docker run -p 8000:8000 ia-previsao-salario
```

Acesse: `http://localhost:8000/docs`

### Sem Docker

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

---

## ✅ Testes

O projeto conta com testes automatizados cobrindo os principais cenários da API (resposta de saúde, previsão válida, payload incompleto, valores de borda):

```bash
pytest testes/ -v
```

Os testes são executados automaticamente via **GitHub Actions** a cada `push` na branch `main`.

---

## 📁 Estrutura do projeto

ia-previsao-salario/
├── app/                  # código da API (FastAPI, esquemas, lógica do modelo)
├── dados/
│   ├── brutos/           # dados originais (não versionados — ver FONTE.md)
│   └── processados/      # dados limpos, prontos para modelagem
├── modelos/              # modelo treinado serializado (.pkl)
├── notebooks/            # exploração, limpeza e modelagem
├── testes/               # testes automatizados (pytest)
├── documentos/           # diário de desenvolvimento e documentação para recrutador
├── .github/workflows/    # pipeline de CI
├── Dockerfile
└── main.py

---

## 📝 Nota sobre deploy

A aplicação foi validada em ambiente containerizado (Docker) e está pronta para deploy em qualquer plataforma compatível. O deploy público não foi mantido ativo devido a mudanças recentes nas políticas de cadastro (exigência de cartão de crédito) das principais plataformas gratuitas disponíveis no momento do desenvolvimento.

---

## 👤 Autor

Fabricio Tonetta

