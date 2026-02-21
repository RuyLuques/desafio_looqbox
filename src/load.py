import logging
import pandas as pd
from sqlalchemy.engine import Engine
from src.config import settings

logger = logging.getLogger(__name__)


def load(df: pd.DataFrame, engine: Engine) -> None:
    try:
        logger.info(f"Carregando dados na tabela {settings.processed_table}")
        df.to_sql(
            settings.processed_table,
            engine,
            if_exists="replace",
            index=False,
        )
        logger.info("Carga realizada com sucesso")
    except Exception:
        logger.exception("Erro na etapa de carga")
        raise