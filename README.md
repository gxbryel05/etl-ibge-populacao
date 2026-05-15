# Pipeline ETL — Municípios Brasileiros (IBGE)

Pipeline de dados desenvolvido em Python que extrai informações de todos os municípios brasileiros via API pública do IBGE, realiza transformações e limpeza com Pandas e carrega em PostgreSQL. O projeto evoluiu para incluir orquestração completa com Apache Airflow.

---

## Sobre

Projeto construído para aplicar na prática os fundamentos de Engenharia de Dados, simulando um pipeline ETL real com dados públicos brasileiros.

O pipeline processa 5.570 municípios, normalizando estruturas JSON aninhadas, padronizando texto, removendo inconsistências e persistindo os dados de forma estruturada para análise posterior.

---

## Arquitetura

### Fase 1 — Pipeline local
```
[API IBGE] → [extract.py] → [transform.py] → [load.py] → [PostgreSQL]
```

### Fase 2 — Orquestração com Airflow
```
[Airflow Scheduler] → DAG: etl_ibge_municipios
        ↓
   extrair → transformar → carregar
      ↓           ↓            ↓
  API IBGE      Pandas      PostgreSQL
```

---

## Stacks utilizada

| Tecnologia      | Uso                                      |
|-----------------|------------------------------------------|
| Python 3.11     | Linguagem principal                      |
| Pandas          | Transformação e limpeza dos dados        |
| Requests        | Consumo da API REST do IBGE              |
| SQLAlchemy      | Conexão e carga no banco de dados        |
| PostgreSQL 15   | Armazenamento dos dados                  |
| Apache Airflow  | Orquestração e agendamento do pipeline   |
| Docker Compose  | Infraestrutura local                     |
| Git & GitHub    | Versionamento do projeto                 |

---

## Estrutura do projeto

```
etl-ibge-populacao/
├── src/                        # Pipeline original
│   ├── extract.py              # Extração via API do IBGE
│   ├── transform.py            # Limpeza e transformação com Pandas
│   ├── load.py                 # Carga no PostgreSQL via SQLAlchemy
│   └── pipeline.py             # Orquestrador manual do fluxo ETL
├── airflow/                    # Orquestração com Airflow
│   ├── dags/
│   │   ├── etl_ibge.py         # Definição da DAG
│   │   └── etl/                # Módulos ETL usados pelo Airflow
│   └── docker-compose.yaml     # Infraestrutura do Airflow
├── sql/
│   ├── create_tables.sql       # Criação da tabela no banco
│   └── queries_analise.sql     # Queries de validação e análise
├── .env.example                # Modelo de variáveis de ambiente
├── .gitignore
└── README.md
```

---

## Executando:

### Fase 1 — Pipeline local

```bash
# Clone o repositório
git clone https://github.com/gxbryel05/etl-ibge-populacao.git
cd etl-ibge-populacao

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o .env com suas credenciais

# Suba o PostgreSQL com Docker
docker run --name etl-postgres \
  -e POSTGRES_USER=seu_user \
  -e POSTGRES_PASSWORD=sua_senha \
  -e POSTGRES_DB=etl_db \
  -p 5432:5432 -d postgres:15

# Execute o pipeline
cd src && python pipeline.py
```

### Fase 2 — Orquestração com Airflow

```bash
# Entre na pasta do Airflow
cd airflow

# Suba os serviços
docker compose up -d

# Acesse a interface
# http://localhost:8080 (usuário: airflow / senha: airflow)

# Ative a DAG etl_ibge_municipios e clique em ▶
```

---

## Resultados e análises

| Região        | Total |
|---------------|-------|
| Nordeste      | 1.794 |
| Sudeste       | 1.668 |
| Sul           | 1.191 |
| Centro-Oeste  | 467   |
| Norte         | 450   |

---

## Próximos passos

- [ ] Migrar o armazenamento para Google BigQuery (GCP)
- [ ] Adicionar camada de testes automatizados com Pytest
- [ ] Criar dashboard interativo com Streamlit

---

## Contatos

**Gabryel Rosa Bomfim**
[LinkedIn](https://linkedin.com/in/gabryel-rosa) • [GitHub](https://github.com/gxbryel05)