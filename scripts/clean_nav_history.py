import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort by fund and date
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Forward fill NAV values
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Keep only positive NAV values
df = df[df["nav"] > 0]

print("Rows after cleaning:", len(df))

df.to_csv(
    "data/processed/clean_nav_history.csv",
    index=False
)

print("clean_nav_history.csv saved successfully")