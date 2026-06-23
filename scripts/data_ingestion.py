import pandas as pd
from pathlib import Path

data_path = Path("data/raw")

csv_files = list(data_path.glob("*.csv"))

for file in csv_files:
    print("\n" + "="*60)
    print(f"FILE: {file.name}")
    print("="*60)

    df = pd.read_csv(file)

    print("\nShape:")
    print(df.shape)

    print("\nDtypes:")
    print(df.dtypes)

    print("\nHead:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())