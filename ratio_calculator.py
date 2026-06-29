def calculate_gross_margin(income_statement, year_index=0):
    revenue = income_statement.loc["Total Revenue"].dropna().iloc[year_index]
    gross_profit = income_statement.loc["Gross Profit"].dropna().iloc[year_index]
    return (gross_profit / revenue) * 100

def calculate_operating_margin(income_statement, year_index=0):
    revenue = income_statement.loc["Total Revenue"].dropna().iloc[year_index]
    operating_income = income_statement.loc["Operating Income"].dropna().iloc[year_index]
    operating_margin = (operating_income / revenue) * 100
    return operating_margin

def calculate_net_margin(income_statement, year_index=0):
    revenue = income_statement.loc["Total Revenue"].dropna().iloc[year_index]
    net_income = income_statement.loc["Net Income Common Stockholders"].dropna().iloc[year_index]
    net_margin = (net_income / revenue) * 100
    return net_margin

def calculate_roa(income_statement, balance_sheet, year_index=0):
    net_income = income_statement.loc["Net Income Common Stockholders"].dropna().iloc[year_index]
    total_assets = balance_sheet.loc["Total Assets"].dropna().iloc[year_index]
    roa = (net_income / total_assets) * 100
    return roa

def calculate_roe(income_statement, balance_sheet, year_index=0):
    net_income = income_statement.loc["Net Income Common Stockholders"].dropna().iloc[year_index]
    stockholders_equity = balance_sheet.loc["Stockholders Equity"].dropna().iloc[year_index]
    roe = (net_income / stockholders_equity) * 100
    return roe

def calculate_current_ratio(balance_sheet, year_index=0):
    current_assets=balance_sheet.loc["Current Assets"].dropna().iloc[year_index]
    current_liabilities=balance_sheet.loc["Current Liabilities"].dropna().iloc[year_index]
    current_ratio=current_assets/current_liabilities
    return current_ratio

def calculate_quick_ratio(balance_sheet, year_index=0):
    current_assets = balance_sheet.loc["Current Assets"].dropna().iloc[year_index]
    current_liabilities = balance_sheet.loc["Current Liabilities"].dropna().iloc[year_index]

    if "Inventory" in balance_sheet.index:
        inventory = balance_sheet.loc["Inventory"].dropna().iloc[year_index]
    else:
        inventory = 0

    quick_ratio = (current_assets - inventory) / current_liabilities
    return quick_ratio

def calculate_cash_ratio(balance_sheet, year_index=0):
    cash=balance_sheet.loc["Cash And Cash Equivalents"].dropna().iloc[year_index]
    current_liabilities=balance_sheet.loc["Current Liabilities"].dropna().iloc[year_index]
    cash_ratio=cash/current_liabilities
    return cash_ratio

def calculate_debt_to_assets(balance_sheet, year_index=0):
    total_debt=balance_sheet.loc["Total Debt"].dropna().iloc[year_index]
    total_assets=balance_sheet.loc["Total Assets"].dropna().iloc[year_index]
    debt_to_assets=(total_debt/total_assets)*100
    return debt_to_assets

def calculate_debt_to_equity(balance_sheet, year_index=0):
    total_debt = balance_sheet.loc["Total Debt"].dropna().iloc[year_index]
    equity = balance_sheet.loc["Stockholders Equity"].dropna().iloc[year_index]
    debt_to_equity = (total_debt / equity) 
    return debt_to_equity

def calculate_equity_ratio(balance_sheet, year_index=0):
    equity = balance_sheet.loc["Stockholders Equity"].dropna().iloc[year_index]
    total_assets = balance_sheet.loc["Total Assets"].dropna().iloc[year_index]
    equity_ratio = (equity / total_assets) * 100
    return equity_ratio

def calculate_asset_turnover(income_statement, balance_sheet, year_index=0):
    revenue = income_statement.loc["Total Revenue"].dropna().iloc[year_index]
    total_assets = balance_sheet.loc["Total Assets"].dropna().iloc[year_index]
    asset_turnover = revenue / total_assets
    return asset_turnover

def calculate_interest_coverage(income_statement, year_index=0):
    ebit = income_statement.loc["EBIT"].dropna().iloc[year_index]
    interest_expense = abs(income_statement.loc["Interest Expense"].iloc[year_index])
    interest_coverage = ebit / interest_expense
    return interest_coverage