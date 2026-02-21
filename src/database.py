from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from src.config import settings


def create_db_engine() -> Engine:
    engine = create_engine(
        settings.database_url,
        pool_pre_ping=True,
        pool_size=5,
        max_overflow=10,
    )
    return engine


engine = create_db_engine()