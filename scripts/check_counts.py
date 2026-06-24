from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
"sqlite:///data/db/bluestock_mf.db"
)

tables = [
"dim_fund",
"fact_nav",
"fact_transactions",
"fact_performance",
"fact_aum"
]

for t in tables:
    count = pd.read_sql(
        f"SELECT COUNT(*) c FROM {t}",
        engine
    )

    print(t)
    print(count)