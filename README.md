# 📊 Data Pipeline - Looqbox Challenge

## 🚀 Overview
Pipeline ETL desenvolvido em Python para extração, transformação e carga de dados no PostgreSQL.

## 🏗️ Arquitetura
- Extract → PostgreSQL
- Transform → Pandas
- Load → PostgreSQL
- Config via .env
- Logging estruturado

## 🛠️ Stack
- Python 3.11+
- PostgreSQL
- SQLAlchemy
- Pandas

## ▶️ Como rodar

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py