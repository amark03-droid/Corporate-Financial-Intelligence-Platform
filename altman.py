from industry_mapping import MANUFACTURING_INDUSTRIES

def calculate_working_capital(balance_sheet):
    current_assets = balance_sheet.loc["Current Assets"].dropna().iloc[0]
    current_liabilities = balance_sheet.loc["Current Liabilities"].dropna().iloc[0]
    working_capital = current_assets - current_liabilities
    return working_capital

def calculate_x1(balance_sheet):
    working_capital = calculate_working_capital(balance_sheet)
    total_assets = balance_sheet.loc["Total Assets"].dropna().iloc[0]
    x1 = working_capital / total_assets
    return x1

def calculate_x2(balance_sheet):
    retained_earnings = balance_sheet.loc["Retained Earnings"].dropna().iloc[0]
    total_assets = balance_sheet.loc["Total Assets"].dropna().iloc[0]
    x2=retained_earnings / total_assets
    return x2

def calculate_x3(income_statement, balance_sheet):
    ebit=income_statement.loc["EBIT"].dropna().iloc[0]
    total_assets=balance_sheet.loc["Total Assets"].dropna().iloc[0]
    x3=ebit/total_assets
    return x3

def calculate_x4(balance_sheet, market_cap):
    total_liabilities = balance_sheet.loc["Total Liabilities Net Minority Interest"].dropna().iloc[0]
    x4 = market_cap / total_liabilities
    return x4

def calculate_x4_book(balance_sheet):
    equity = balance_sheet.loc["Stockholders Equity"].dropna().iloc[0]
    total_liabilities = balance_sheet.loc["Total Liabilities Net Minority Interest"].dropna().iloc[0]
    return equity / total_liabilities

def calculate_x5(income_statement, balance_sheet):
    revenue = income_statement.loc["Total Revenue"].dropna().iloc[0]
    total_assets = balance_sheet.loc["Total Assets"].dropna().iloc[0]
    x5 = revenue / total_assets
    return x5

def calculate_original_altman_zscore(income_statement, balance_sheet, market_cap):
    x1 = calculate_x1(balance_sheet)
    x2 = calculate_x2(balance_sheet)
    x3 = calculate_x3(income_statement, balance_sheet)
    x4 = calculate_x4(balance_sheet, market_cap)
    x5 = calculate_x5(income_statement, balance_sheet)

    z_score = (
        (1.2 * x1)
        + (1.4 * x2)
        + (3.3 * x3)
        + (0.6 * x4)
        + (1.0 * x5)
    )

    return z_score

def calculate_non_manufacturing_altman_zscore(income_statement,balance_sheet):
    x1 = calculate_x1(balance_sheet)
    x2 = calculate_x2(balance_sheet)
    x3 = calculate_x3(income_statement, balance_sheet)
    x4 = calculate_x4_book(balance_sheet)

    z_score = (
        (6.56 * x1)
        + (3.26 * x2)
        + (6.72 * x3)
        + (1.05 * x4)
    )

    return z_score

def calculate_altman_score(income_statement,balance_sheet,market_cap,industry):
   
    if industry in MANUFACTURING_INDUSTRIES:
       return calculate_original_altman_zscore(
            income_statement,
            balance_sheet,
            market_cap
        )

    else:
        return calculate_non_manufacturing_altman_zscore(
            income_statement,
            balance_sheet,
        )