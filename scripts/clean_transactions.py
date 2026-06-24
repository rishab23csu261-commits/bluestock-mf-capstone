import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

# Date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

valid_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

df = df[
    df["transaction_type"].isin(valid_types)
]

# Amount validation
df = df[df["amount_inr"] > 0]

# KYC validation
valid_kyc = [
    "Verified",
    "Pending"
]

df = df[
    df["kyc_status"].isin(valid_kyc)
]

df.to_csv(
    "data/processed/clean_transactions.csv",
    index=False
)

print(df.shape)