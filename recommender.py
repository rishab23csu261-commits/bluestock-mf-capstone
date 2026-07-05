import pandas as pd

def run_recommender():
    try:
        report = pd.read_csv('var_cvar_report.csv')
    except FileNotFoundError:
        print("Error: var_cvar_report.csv not found.")
        return

    print("--- Fund Recommendation Engine ---")
    risk_appetite = input("Enter Risk Appetite (Low, Moderate, High): ").strip().title()

    # We might have categories like 'Very High' in the data, let's map loosely if needed, or exact match.
    # Check what categories exist
    available_risks = report['Risk Grade'].unique()

    # Filter based on risk
    matched_funds = report[report['Risk Grade'].str.contains(risk_appetite, case=False, na=False)]

    if matched_funds.empty:
        print(f"No funds found for risk appetite: {risk_appetite}")
        print(f"Available risk grades: {', '.join(available_risks)}")
        return

    # Sort by Highest Sharpe Ratio
    top_3 = matched_funds.sort_values(by='Sharpe Ratio', ascending=False).head(3)

    print("\nTop 3 Funds Recommended for you:\n")
    print(top_3[['Scheme', 'Risk Grade', 'Sharpe Ratio', 'VaR', 'CVaR']].to_string(index=False))

if __name__ == '__main__':
    run_recommender()
