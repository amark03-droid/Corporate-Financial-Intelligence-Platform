def get_revenue(income_statement):
    return income_statement.loc["Total Revenue"].dropna().iloc[0]


def get_gross_profit(income_statement):
    return income_statement.loc["Gross Profit"].dropna().iloc[0]


def get_net_income(income_statement):
    return income_statement.loc["Net Income Common Stockholders"].dropna().iloc[0]


def get_total_assets(balance_sheet):
    return balance_sheet.loc["Total Assets"].dropna().iloc[0]


def get_equity(balance_sheet):
    return balance_sheet.loc["Stockholders Equity"].dropna().iloc[0]

def format_number(number):
    if number >= 1_000_000_000_000:
        return f"{number / 1_000_000_000_000:.2f}T"
    elif number >= 1_000_000_000:
        return f"{number / 1_000_000_000:.2f}B"
    elif number >= 1_000_000:
        return f"{number / 1_000_000:.2f}M"
    else:
        return f"{number:,.0f}"