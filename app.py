import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from data_fetcher import get_company_info, get_financial_statements
from altman import calculate_altman_score
from cfhi import calculate_cfhi_scores
from altman import (
    calculate_x1,
    calculate_x2,
    calculate_x3,
    calculate_x4,
    calculate_x5
)
from industry_mapping import MANUFACTURING_INDUSTRIES
from financial_metrics import (
    get_revenue,
    get_gross_profit,
    get_net_income,
    get_total_assets,
    get_equity,
    format_number
)

from ratio_calculator import (
    calculate_gross_margin,
    calculate_operating_margin,
    calculate_net_margin,
    calculate_roa,
    calculate_roe,
    calculate_current_ratio,
    calculate_quick_ratio,
    calculate_cash_ratio,
    calculate_debt_to_assets,
    calculate_debt_to_equity,
    calculate_equity_ratio,
    calculate_asset_turnover,
    calculate_interest_coverage
)

st.title("Corporate Financial Intelligence Platform")
st.markdown("""
An end-to-end financial analytics dashboard that transforms raw financial statements into
meaningful business insights using financial ratios, Altman Z-Score, the Corporate Financial Health Index (CFHI),
interactive visualizations, and executive financial summaries.
""")

company = st.text_input(
    "Enter Company Ticker",
    placeholder="e.g. AAPL, MSFT, BA, TCS.NS, INFY.NS")
st.caption("💡 Examples: AAPL (Apple) • MSFT (Microsoft) • BA (Boeing) • TCS.NS (TCS) • INFY.NS (Infosys)")

if st.button("Analyze"):

    info = get_company_info(company)
    if not info or info.get("longName") is None:
       st.error("Unable to fetch company information from Yahoo Finance.")
       st.info("Please try another ticker")
       st.stop()

    st.write("Company Name:", info.get("longName"))
    st.write("Sector:", info.get("sector"))
    st.write("Industry:", info.get("industry"))

    income_statement, balance_sheet, cash_flow, market_cap, industry = get_financial_statements(company)
    revenue = get_revenue(income_statement)
    gross_profit = get_gross_profit(income_statement)
    net_income = get_net_income(income_statement)
    total_assets = get_total_assets(balance_sheet)
    equity = get_equity(balance_sheet)

    st.subheader("Income Statement")
    st.dataframe(income_statement)
    st.subheader("Balance Sheet")
    st.dataframe(balance_sheet)
    st.subheader("Key Financial Metrics")
    col1, col2 = st.columns(2)
    with col1:
       st.metric("Revenue", format_number(revenue))
       st.metric("Gross Profit", format_number(gross_profit))
       st.metric("Net Income", format_number(net_income))
    with col2:
       st.metric("Total Assets", format_number(total_assets))
       st.metric("Stockholders Equity", format_number(equity))
#profitability ratios    
    gross_margin = calculate_gross_margin(income_statement)
    gross_margin = calculate_gross_margin(income_statement)
    operating_margin = calculate_operating_margin(income_statement)
    net_margin = calculate_net_margin(income_statement)
    roa=calculate_roa(income_statement, balance_sheet)
    roe=calculate_roe(income_statement, balance_sheet)
#Liquidity ratios
    current_ratio=calculate_current_ratio(balance_sheet)
    quick_ratio=calculate_quick_ratio(balance_sheet)
    cash_ratio=calculate_cash_ratio(balance_sheet)
#Solvency ratios
    debt_to_assets=calculate_debt_to_assets(balance_sheet)
    debt_to_equity=calculate_debt_to_equity(balance_sheet)
    equity_ratio = calculate_equity_ratio(balance_sheet)
    interest_coverage = calculate_interest_coverage(income_statement)
#Efficiency ratios
    asset_turnover=calculate_asset_turnover(income_statement, balance_sheet)
    
    scores = calculate_cfhi_scores(
    gross_margin,
    operating_margin,
    net_margin,
    roa,
    roe,
    current_ratio,
    quick_ratio,
    cash_ratio,
    debt_to_assets,
    debt_to_equity,
    equity_ratio,
    interest_coverage,
    asset_turnover
)
    
    st.subheader("Financial Ratios")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Gross Margin: {gross_margin:.2f}%")
        st.write(f"Operating Margin: {operating_margin:.2f}%")
        st.write(f"Net Profit Margin: {net_margin:.2f}%")
        st.write(f"ROA: {roa:.2f}%")
        st.write(f"ROE: {roe:.2f}%")
        st.write(f"Equity Ratio: {equity_ratio:.2f}%")
        st.write(f"Interest Coverage: {interest_coverage:.2f}")
    with col2:
        st.write(f"Current Ratio: {current_ratio:.2f}")
        st.write(f"Quick Ratio: {quick_ratio:.2f}")
        st.write(f"Cash Ratio: {cash_ratio:.2f}")
        st.write(f"Debt to Assets: {debt_to_assets:.2f}%")
        st.write(f"Debt to Equity: {debt_to_equity:.2f}%")
        st.write(f"Asset Turnover: {asset_turnover:.2f}")
    
    altman_score = calculate_altman_score(
    income_statement,
    balance_sheet,
    market_cap,
    industry
)
    st.subheader("Altman Z-Score")
    st.metric("Altman Z-Score", f"{altman_score:.2f}")

    if industry in MANUFACTURING_INDUSTRIES:
       st.write("Model Used: Original Altman Z-Score (Manufacturing)")
    else:
       st.write("Model Used: Altman Z2 Score (Non-Manufacturing)")

    if altman_score > 2.6:
       st.success("🟢 Safe Zone")

    elif altman_score >= 1.1:
       st.warning("🟡 Grey Zone")

    else:
       st.error("🔴 Distress Zone")
    

    st.subheader("Corporate Financial Health Index (CFHI)")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("CFHI Score",f"{scores['CFHI Score']:.2f}/100")

    if scores["CFHI Score"] >= 80:
       st.success("🟢 Excellent Financial Health")
    elif scores["CFHI Score"] >= 60:
       st.warning("🟡 Good Financial Health")
    elif scores["CFHI Score"] >= 40:
       st.warning("🟠 Average Financial Health")
    else:
       st.error("🔴 Poor Financial Health")

    st.progress(scores["CFHI Score"] / 100)

    st.markdown("---")
    st.subheader("Category Scores")
    
    st.write(f"Profitability : {scores['Profitability Score']:.2f}/10")
    st.write(f"Liquidity : {scores['Liquidity Score']:.2f}/10")
    st.write(f"Solvency : {scores['Solvency Score']:.2f}/10")
    st.write(f"Efficiency : {scores['Efficiency Score']:.2f}/10")

    fig = go.Figure()#creating a blank fig
    categories = ["Profitability","Liquidity","Solvency","Efficiency"]
    values = [
    scores["Profitability Score"],
    scores["Liquidity Score"],
    scores["Solvency Score"],
    scores["Efficiency Score"] ]
#for radar chart 2 things i.e categories & values
#here trace is like adding multiple layer like upon adding multiple 
#traces u can add like 2 radars plus also scatter chart
#toself connecting those point last to first
#fill is like filling inside the connected doutline
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill="toself",
        fillcolor="rgba(0,123,255,0.35)",
        line=dict(color="royalblue", width=3),
        marker=dict(size=8),
        name="CFHI"))
    fig.update_layout(
        title=dict(text="Corporate Financial Health Radar",x=0.26),
        polar=dict(radialaxis=dict(
                        visible=True,
                        range=[0, 10],
                        tickvals=[2, 4, 6, 8, 10],
                        tickfont=dict(size=12),
                        gridcolor="lightgray",
                        linecolor="black"),
                    angularaxis=dict(tickfont=dict(size=14))),
        showlegend=True,
        height=320,
        width=320,
        margin=dict(l=15, r=15, t=50, b=55))
    
    st.plotly_chart(fig, use_container_width=True)

#starting the trends part
    st.subheader("Financial Trends")
    revenue = income_statement.loc["Total Revenue"].dropna()#all years no iloc
    years = revenue.index.year.astype(str)#chnging type bcs these labels nt int
    revenue_df = pd.DataFrame({
        "Year": years,
        "Revenue": revenue.values})
    revenue_df = revenue_df.sort_values("Year").reset_index(drop=True)#droping the index
    #st.write(revenue_df)
    revenue_fig = go.Figure()
    revenue_fig.add_trace(
        go.Scatter(
            x=revenue_df["Year"],
            y=revenue_df["Revenue"],
            mode="lines+markers",
            name="Revenue"))#for line chart also used scatter so to see the dots
    revenue_fig.update_layout(
        title=dict(
            text="Revenue Trend",
            x=0.4),
        xaxis_title="Year",
        yaxis_title="Revenue",
        showlegend=False,
        height=400)
    st.plotly_chart(revenue_fig, use_container_width=True)
#trend for net income
    net_income = income_statement.loc["Net Income Common Stockholders"].dropna()
    net_income_years = net_income.index.year.astype(str)
    net_income_df = pd.DataFrame({
        "Year": net_income_years,
        "Net Income": net_income.values})
    net_income_df = net_income_df.sort_values("Year").reset_index(drop=True)
    #st.write(net_income_df)
    net_income_fig = go.Figure()
    net_income_fig.add_trace(
        go.Scatter(
            x=net_income_df["Year"],
            y=net_income_df["Net Income"],
            mode="lines+markers",
            name="Net Income"))
    net_income_fig.update_layout(
        title=dict(
            text="Net Income Trend",
            x=0.4),
        xaxis_title="Year",
        yaxis_title="Net Income",
        showlegend=False,
        height=400)
    st.plotly_chart(net_income_fig, use_container_width=True)

    st.subheader("CFHI Trend")
    cfhi_scores = []
    years = []
    for year_index in range(4):
        gross_margin = calculate_gross_margin(income_statement, year_index)
        operating_margin = calculate_operating_margin(income_statement, year_index)
        net_margin = calculate_net_margin(income_statement, year_index)
        roa = calculate_roa(income_statement, balance_sheet, year_index)
        roe = calculate_roe(income_statement, balance_sheet, year_index)
    # Liquidity Ratios
        current_ratio = calculate_current_ratio(balance_sheet, year_index)
        quick_ratio = calculate_quick_ratio(balance_sheet, year_index)
        cash_ratio = calculate_cash_ratio(balance_sheet, year_index)
    # Solvency Ratios
        debt_to_assets = calculate_debt_to_assets(balance_sheet, year_index)
        debt_to_equity = calculate_debt_to_equity(balance_sheet, year_index)
        equity_ratio = calculate_equity_ratio(balance_sheet, year_index)
        interest_coverage = calculate_interest_coverage(income_statement, year_index)
    # Efficiency Ratio
        asset_turnover = calculate_asset_turnover(income_statement,balance_sheet,year_index)
        scores = calculate_cfhi_scores(
            gross_margin,
            operating_margin,
            net_margin,
            roa,
            roe,
            current_ratio,
            quick_ratio,
            cash_ratio,
            debt_to_assets,
            debt_to_equity,
            equity_ratio,
            interest_coverage,
            asset_turnover)
       
        cfhi_scores.append(scores["CFHI Score"])
        years.append(income_statement.columns[year_index].year)
    cfhi_df = pd.DataFrame({
        "Year": years,
        "CFHI": cfhi_scores})
    cfhi_df = cfhi_df.sort_values("Year").reset_index(drop=True)
    cfhi_fig = go.Figure()

    cfhi_fig.add_trace(
        go.Scatter(
            x=cfhi_df["Year"],
            y=cfhi_df["CFHI"],
            mode="lines+markers",
            name="CFHI"))

    cfhi_fig.update_layout(
        title=dict(
            text="CFHI Trend",
            x=0.4),
        xaxis_title="Year",
        yaxis_title="CFHI Score",
        showlegend=False,
        height=400)

    st.plotly_chart(cfhi_fig, use_container_width=True)
    st.subheader("Executive Financial Summary")

    summary = ""
# Overall Financial Health
    if scores["CFHI Score"] >= 80:
        summary += "The company demonstrates excellent overall financial health. "
    elif scores["CFHI Score"] >= 60:
        summary += "The company demonstrates good financial health with a stable financial position. "
    elif scores["CFHI Score"] >= 40:
        summary += "The company shows moderate financial health with some areas requiring improvement. "
    else:
        summary += "The company exhibits weak financial health and may face financial challenges. "

# Profitability
    if scores["Profitability Score"] >= 8:
        summary += "Profitability is a major strength of the company. "
    elif scores["Profitability Score"] >= 6:
        summary += "Profitability is satisfactory. "
    else:
        summary += "Profitability remains weak and requires improvement. "

# Liquidity
    if scores["Liquidity Score"] >= 8:
        summary += "Liquidity is strong, indicating good short-term financial stability. "
    elif scores["Liquidity Score"] >= 6:
        summary += "Liquidity is adequate. "
    else:
        summary += "Liquidity is weak, which may affect the company's ability to meet short-term obligations. "

# Solvency
    if scores["Solvency Score"] >= 8:
        summary += "The company's debt position is well managed and financial leverage remains under control. "
    elif scores["Solvency Score"] >= 6:
        summary += "The company's solvency position is satisfactory. "
    else:
        summary += "High leverage may expose the company to long-term financial risk. "

# Efficiency
    if scores["Efficiency Score"] >= 8:
        summary += "The company utilizes its assets efficiently to generate revenue. "
    elif scores["Efficiency Score"] >= 6:
        summary += "Asset utilization is satisfactory. "
    else:
        summary += "Operational efficiency can be improved to generate better returns from assets. "

# Altman Z-Score
    if altman_score >= 3:
        summary += "The Altman Z-Score indicates a low probability of financial distress."
    elif altman_score >= 1.8:
        summary += "The Altman Z-Score places the company in the grey zone, suggesting moderate financial risk."
    else:
        summary += "The Altman Z-Score indicates a high probability of financial distress."

    st.info(summary)




 


    
 
