# Data Dictionary

## 1. dim_fund

**Source:** 01_fund_master.csv

| Column Name        | Data Type | Description                                            |
| ------------------ | --------- | ------------------------------------------------------ |
| amfi_code          | TEXT      | Unique AMFI scheme code                                |
| fund_house         | TEXT      | Asset Management Company (AMC) name                    |
| scheme_name        | TEXT      | Official mutual fund scheme name                       |
| category           | TEXT      | Fund category (Equity, Debt, Hybrid, etc.)             |
| sub_category       | TEXT      | Fund sub-category (Large Cap, Small Cap, Liquid, etc.) |
| plan               | TEXT      | Direct or Regular plan                                 |
| launch_date        | DATE      | Scheme launch date                                     |
| benchmark          | TEXT      | Benchmark index used for comparison                    |
| expense_ratio_pct  | REAL      | Annual expense ratio percentage                        |
| exit_load_pct      | REAL      | Exit load percentage                                   |
| fund_manager       | TEXT      | Primary fund manager                                   |
| risk_category      | TEXT      | SEBI risk category                                     |
| sebi_category_code | TEXT      | Internal SEBI classification code                      |

---

## 2. fact_nav

**Source:** 02_nav_history.csv

| Column Name | Data Type | Description                      |
| ----------- | --------- | -------------------------------- |
| amfi_code   | TEXT      | Foreign key referencing dim_fund |
| date        | DATE      | NAV date                         |
| nav         | REAL      | Net Asset Value per unit         |

---

## 3. fact_transactions

**Source:** 08_investor_transactions.csv

| Column Name        | Data Type | Description                          |
| ------------------ | --------- | ------------------------------------ |
| investor_id        | TEXT      | Unique investor identifier           |
| transaction_date   | DATE      | Date of transaction                  |
| amfi_code          | TEXT      | Mutual fund scheme code              |
| transaction_type   | TEXT      | SIP, Lumpsum, or Redemption          |
| amount_inr         | INTEGER   | Transaction amount in INR            |
| state              | TEXT      | Investor state                       |
| city               | TEXT      | Investor city                        |
| city_tier          | TEXT      | T30 or B30 classification            |
| age_group          | TEXT      | Investor age bracket                 |
| gender             | TEXT      | Investor gender                      |
| annual_income_lakh | REAL      | Annual income in lakh rupees         |
| payment_mode       | TEXT      | UPI, Net Banking, Mandate, or Cheque |
| kyc_status         | TEXT      | Verified or Pending                  |

---

## 4. fact_performance

**Source:** 07_scheme_performance.csv

| Column Name        | Data Type | Description                   |
| ------------------ | --------- | ----------------------------- |
| amfi_code          | TEXT      | Mutual fund scheme code       |
| return_1yr_pct     | REAL      | 1-year return percentage      |
| return_3yr_pct     | REAL      | 3-year CAGR return percentage |
| return_5yr_pct     | REAL      | 5-year CAGR return percentage |
| benchmark_3yr_pct  | REAL      | Benchmark 3-year CAGR         |
| alpha              | REAL      | Excess return over benchmark  |
| beta               | REAL      | Market sensitivity measure    |
| sharpe_ratio       | REAL      | Risk-adjusted return metric   |
| sortino_ratio      | REAL      | Downside-risk-adjusted return |
| std_dev_ann_pct    | REAL      | Annualized standard deviation |
| max_drawdown_pct   | REAL      | Maximum portfolio decline     |
| morningstar_rating | INTEGER   | Rating from 1 to 5 stars      |

---

## 5. fact_aum

**Source:** 03_aum_by_fund_house.csv

| Column Name      | Data Type | Description                       |
| ---------------- | --------- | --------------------------------- |
| fund_house       | TEXT      | Asset Management Company name     |
| aum_crore        | REAL      | Assets Under Management (₹ Crore) |
| market_share_pct | REAL      | Percentage market share           |
| rank             | INTEGER   | Rank based on AUM                 |

---

## Business Definitions

### NAV (Net Asset Value)

Represents the per-unit value of a mutual fund scheme calculated daily.

### AUM (Assets Under Management)

Total market value of assets managed by a mutual fund company.

### SIP (Systematic Investment Plan)

A recurring investment made periodically into a mutual fund scheme.

### Expense Ratio

Annual fee charged by the mutual fund house for managing investments.

### Sharpe Ratio

Measures risk-adjusted returns. Higher values indicate better performance relative to risk.

### Alpha

Excess return earned by a fund compared to its benchmark.

### Beta

Measure of volatility compared to the market benchmark.

### KYC Status

Investor verification status as per regulatory requirements.
