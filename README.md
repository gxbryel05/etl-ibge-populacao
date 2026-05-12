# 🔄 Pipeline ETL — Municípios Brasileiros (IBGE)

Pipeline de dados desenvolvido em Python que extrai informações
de todos os municípios brasileiros diretamente da API pública do
IBGE, realiza transformações e limpeza dos dados com Pandas e
carrega o resultado em um banco de dados PostgreSQL.

---

## 📌 Sobre o projeto

Este projeto foi desenvolvido com o objetivo de aplicar na prática
os fundamentos de Engenharia de Dados, simulando um pipeline ETL
real com dados públicos brasileiros.

O pipeline processa 5.570 municípios, normalizando estruturas JSON
aninhadas, padronizando texto, removendo inconsistências e
persistindo os dados de forma estruturada para análise posterior.

---

## 🏗️ Arquitetura
[API IBGE] → [extract.py] → [transform.py] → [load.py] → [PostgreSQL]
↓                 ↓                 ↓
JSON bruto        DataFrame         Tabela
5.571 registros   limpo e           municipios
padronizado       5.570 registros

---

## 🛠️ Stack utilizada

| Tecnologia      | Uso                                      |
|-----------------|------------------------------------------|
| Python 3.11     | Linguagem principal                      |
| Pandas          | Transformação e limpeza dos dados        |
| Requests        | Consumo da API REST do IBGE              |
| SQLAlchemy      | Conexão e carga no banco de dados        |
| PostgreSQL 15   | Armazenamento dos dados                  |
| Docker          | Ambiente isolado para o PostgreSQL       |
| Git & GitHub    | Versionamento do projeto                 |

---

## 📁 Estrutura do projeto
etl-ibge-populacao/
├── src/
│   ├── extract.py           # Extração via API do IBGE
│   ├── transform.py         # Limpeza e transformação com Pandas
│   ├── load.py              # Carga no PostgreSQL via SQLAlchemy
│   └── pipeline.py          # Orquestrador do fluxo ETL
├── sql/
│   ├── create_tables.sql    # Criação da tabela no banco
│   └── queries_analise.sql  # Queries de validação e análise
├── .env.example             # Modelo de variáveis de ambiente
├── .gitignore
└── requirements.txt

---

## ⚙️ Como executar

### Pré-requisitos
- Python 3.11+
- Docker

### 1. Clone o repositório
```bash
git clone https://github.com/gxbryel05/etl-ibge-populacao.git
cd etl-ibge-populacao
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente
```bash
cp .env.example .env
# Edite o .env com suas credenciais
```

### 5. Suba o PostgreSQL com Docker
```bash
docker run --name etl-postgres \
  -e POSTGRES_USER=seu_user \
  -e POSTGRES_PASSWORD=sua_senha \
  -e POSTGRES_DB=etl_db \
  -p 5432:5432 -d postgres:15
```

### 6. Execute o pipeline
```bash
cd src
python pipeline.py
```

---

## 📊 Resultados e análises

Após a execução, os dados ficam disponíveis para consulta no
PostgreSQL. Algumas análises possíveis:

**Municípios por região:**
| Região        | Total |
|---------------|-------|
| Nordeste      | 1.794 |
| Sudeste       | 1.668 |
| Sul           | 1.191 |
| Centro-Oeste  | 467   |
| Norte         | 450   |

---

## 💡 Aprendizados e próximos passos

Este projeto cobre os fundamentos de um pipeline ETL real.
Como evolução natural, pretendo:

- [ ] Orquestrar o pipeline com Apache Airflow
- [ ] Migrar o armazenamento para Google BigQuery (GCP)
- [ ] Adicionar camada de testes automatizados com Pytest
- [ ] Criar dashboard interativo com Streamlit

---

## 👨‍💻 Autor

**Gabryel Rosa Bomfim**
[LinkedIn](https://linkedin.com/in/gabryel-rosa) •
[GitHub](https://github.com/gxbryel05)