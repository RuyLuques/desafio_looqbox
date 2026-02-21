import logging
import pandas as pd
from sqlalchemy.engine import Engine
from src.config import settings

logger = logging.getLogger(__name__)


def extract(engine: Engine) -> pd.DataFrame:
    try:
        logger.info(f"Extraindo dados da tabela {settings.raw_table}")
        query = f"SELECT * FROM {settings.raw_table}"
        df = pd.read_sql(query, engine)
        logger.info(f"{len(df)} registros extraídos")
        return df
    except Exception:
        logger.exception("Erro na etapa de extração")
        raise