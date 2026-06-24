--TOP 5 AUM
SELECT *
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

--Average NAV Per Month
SELECT
strftime('%Y-%m', nav_date),
AVG(nav)
FROM fact_nav
GROUP BY 1;

--Transactions by State
SELECT
state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

--Funds Expense Ratio < 1
SELECT
scheme_name,
expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1;

--Top Categories by Number of Funds
SELECT
category,
COUNT(*) AS fund_count
FROM dim_fund
GROUP BY category
ORDER BY fund_count DESC;

--Funds with Highest Sharpe Ratio
SELECT
amfi_code,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

--Highest 3-Year Return Funds
SELECT
amfi_code,
return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 10;

--AUM by Fund House
SELECT
fund_house,
SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC;

--Transaction Type Distribution
SELECT
transaction_type,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type
ORDER BY total_transactions DESC;

--Monthly SIP Trend
SELECT
month,
sip_inflow_crore,
yoy_growth_pct
FROM monthly_sip_inflows
ORDER BY month;