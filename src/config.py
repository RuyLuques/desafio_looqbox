import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    database_url: str = os.getenv("DATABASE_URL", "")
    raw_table: str = os.getenv("RAW_TABLE", "vendas_raw")
    processed_table: str = os.getenv("PROCESSED_TABLE", "vendas_processadas")

    def validate(self):
        if not self.database_url:
            raise ValueError("DATABASE_URL não definida no .env")


settings = Settings()
settings.validate()