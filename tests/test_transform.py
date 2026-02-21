import pandas as pd
from src.transform import transform


def test_transform_basic():
    data = {
        "product_name": ["Produto A"],
        "category": ["Teste"],
        "price": [100],
        "sales_month_1": [10],
        "sales_month_2": [5],
        "review_score": [4.5],
    }

    df = pd.DataFrame(data)

    result = transform(df)

    assert result["total_units_sold"].iloc[0] == 15
    assert result["total_revenue"].iloc[0] == 1500
    assert "is_outlier" in result.columns