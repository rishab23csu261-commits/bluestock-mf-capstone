import requests
import pandas as pd

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in schemes.items():
    try:
        url = f"https://api.mfapi.in/mf/{code}"

        response = requests.get(url)
        data = response.json()

        print(f"\n{name}")
        print(data["meta"]["scheme_name"])

        df = pd.DataFrame(data["data"])

        df.to_csv(
            f"data/raw/{name}.csv",
            index=False
        )

        print(f"Saved {name}.csv")

    except Exception as e:
        print(f"Error for {name}: {e}")