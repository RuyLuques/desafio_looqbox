import logging
import pandas as pd

logger = logging.getLogger(__name__)


def transform(df: pd.DataFrame) -> pd.DataFrame:
    try:
        logger.info("Iniciando transformação dos dados")

        df.columns = df.columns.str.lower().str.strip()

        sales_columns = [
            col for col in df.columns if col.startswith("sales_month_")
        ]

        df["total_units_sold"] = df[sales_columns].sum(axis=1)
        df["total_revenue"] = df["price"] * df["total_units_sold"]

        mean_rev = df["total_revenue"].mean()
        std_rev = df["total_revenue"].std()

        if std_rev != 0:
            df["revenue_zscore"] = (
                df["total_revenue"] - mean_rev
            ) / std_rev
        else:
            df["revenue_zscore"] = 0

        df["is_outlier"] = df["revenue_zscore"] > 2

        result = df[
            [
                "product_name",
                "category",
                "price",
                "total_units_sold",
                "total_revenue",
                "review_score",
                "is_outlier",
            ]
        ].sort_values("total_revenue", ascending=False)

        logger.info("Transformação concluída com sucesso")
        return result

    except Exception:
        logger.exception("Erro na etapa de transformação")
        raise