📊 Data Pipeline — Looqbox Challenge

Pipeline ETL desenvolvido em Python para extração, transformação e carga de dados no PostgreSQL, totalmente containerizado com Docker e integrado com GitHub Actions (CI).

🚀 Objetivo

Processar dados da tabela vendas_raw, aplicar transformações analíticas e gerar a tabela vendas_processadas com métricas agregadas e identificação de outliers.

🏗️ Arquitetura
PostgreSQL (vendas_raw)
        ↓
Extract (SQLAlchemy)
        ↓
Transform (Pandas)
        ↓
Load (PostgreSQL)
📂 Estrutura do Projeto
DESAFIO_SQL/
│
├── docker/
│   └── init.sql
│
├── src/
│   ├── config.py
│   ├── database.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── pipeline.py
│   └── logger.py
│
├── tests/
│   └── test_transform.py
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── main.py
└── README.md
🛠️ Stack

Python 3.11+

PostgreSQL 15

SQLAlchemy

Pandas

Docker

Pytest

GitHub Actions

🐳 Execução com Docker (recomendado)
🔹 Subir containers
docker compose up --build
🔹 Resetar ambiente
docker compose down -v

O banco é inicializado automaticamente via:

docker/init.sql
🔹 Conexão interna Docker
postgresql://postgres:postgres@db:5432/looqbox_challenge
💻 Execução sem Docker
1️⃣ Criar ambiente virtual
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
2️⃣ Criar banco manualmente
CREATE DATABASE looqbox_challenge;

Executar:

docker/init.sql
3️⃣ Configurar .env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/looqbox_challenge
4️⃣ Rodar pipeline
python main.py
🔄 Transformações Aplicadas

Para cada produto:

Soma das vendas dos 12 meses

Cálculo de total_units_sold

Cálculo de total_revenue

Identificação de outliers via desvio padrão

Preservação de review_score

📊 Tabela Final: vendas_processadas
Coluna	Descrição
product_name	Nome do produto
category	Categoria
price	Preço unitário
total_units_sold	Total vendido
total_revenue	Receita total
review_score	Nota média
is_outlier	Flag de anomalia
🧪 Testes

O projeto possui testes unitários focados na camada de transformação (transform.py), garantindo:

Cálculo correto de total_units_sold

Cálculo correto de total_revenue

Presença da coluna is_outlier

🔹 Executar testes
pytest
🔹 Exemplo de saída
collected 1 item

tests/test_transform.py .                                [100%]

1 passed in 0.75s

Os testes utilizam pytest e rodam de forma independente do banco de dados.

🤖 CI — GitHub Actions

Pipeline automatizado que:

Instala dependências

Executa testes

Valida build

Arquivo:

.github/workflows/ci.yml
📈 Exemplo de Saída
SELECT * FROM vendas_processadas;
product_name	total_units_sold	total_revenue
Notebook Pro 15	255	1147500
Wireless Mouse	...	...
🧠 Decisões Técnicas

Arquitetura modular seguindo separation of concerns

Configuração via .env

Pipeline idempotente

Logging estruturado

Banco inicializado automaticamente

Infra totalmente reproduzível via Docker

Healthcheck no container do banco

🏆 Diferenciais

✔ Estrutura pronta para produção
✔ Infra containerizada
✔ CI automatizado
✔ Código organizado por responsabilidade
✔ Testes unitários
✔ Pipeline idempotente

📌 Autor

Ana Ruy
Desafio Técnico — Looqbox