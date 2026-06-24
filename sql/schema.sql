CREATE TABLE dim_fund(
amfi_code TEXT PRIMARY KEY,
fund_house TEXT,
scheme_name TEXT,
category TEXT,
sub_category TEXT,
expense_ratio_pct REAL,
risk_category TEXT
);

CREATE TABLE dim_date(
date_id INTEGER PRIMARY KEY,
date DATE,
year INTEGER,
month INTEGER,
quarter INTEGER
);

CREATE TABLE fact_nav(
id INTEGER PRIMARY KEY AUTOINCREMENT,
amfi_code TEXT,
nav_date DATE,
nav REAL,
FOREIGN KEY(amfi_code)
REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_transactions(
tx_id INTEGER PRIMARY KEY AUTOINCREMENT,
investor_id TEXT,
amfi_code TEXT,
transaction_date DATE,
amount_inr REAL,
transaction_type TEXT
);

CREATE TABLE fact_performance(
id INTEGER PRIMARY KEY AUTOINCREMENT,
amfi_code TEXT,
return_1yr_pct REAL,
return_3yr_pct REAL,
return_5yr_pct REAL,
sharpe_ratio REAL
);

CREATE TABLE fact_aum(
id INTEGER PRIMARY KEY AUTOINCREMENT,
fund_house TEXT,
date DATE,
aum_crore REAL
);