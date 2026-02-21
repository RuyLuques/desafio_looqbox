import logging
from src.database import engine
from src.extract import extract
from src.transform import transform
from src.load import load

logger = logging.getLogger(__name__)


def run_pipeline() -> None:
    try:
        logger.info("🚀 Iniciando pipeline")

        df_raw = extract(engine)
        df_processed = transform(df_raw)
        load(df_processed, engine)

        logger.info("🏆 Pipeline finalizado com sucesso")

    except Exception:
        logger.critical("Falha crítica no pipeline")
        raise