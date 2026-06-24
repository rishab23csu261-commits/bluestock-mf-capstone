import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

returns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in returns:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Expense ratio range
df = df[
    (df["expense_ratio_pct"] >= 0.1)
    &
    (df["expense_ratio_pct"] <= 2.5)
]

# Flag negative Sharpe
negative_sharpe = df[
    df["sharpe_ratio"] < 0
]

print(
    "Negative Sharpe:",
    len(negative_sharpe)
)

df.to_csv(
    "data/processed/clean_performance.csv",
    index=False
)