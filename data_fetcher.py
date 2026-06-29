import yfinance as yf

def get_company_info(company_name):
    company = yf.Ticker(company_name)
    info = company.info
    return info


def get_financial_statements(company_name):
    company = yf.Ticker(company_name)
    income_statement = company.financials
    balance_sheet = company.balance_sheet
    cash_flow = company.cashflow
    market_cap = company.info.get("marketCap")
    industry = company.info.get("industry")
    return income_statement, balance_sheet, cash_flow, market_cap, industry