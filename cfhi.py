def score_ratio(value, benchmarks):
    for minimum_value, score in benchmarks:
        if value >= minimum_value:
            return score
    return 2

def score_reverse_ratio(value, benchmarks):
    for maximum_value, score in benchmarks:
        if value <= maximum_value:
            return score
    return 2

GROSS_MARGIN_BENCHMARKS = [
    (50, 10),
    (40, 9),
    (30, 8),
    (20, 6),
    (10, 4),
    (0, 2)
]
OPERATING_MARGIN_BENCHMARKS = [
    (25, 10),
    (20, 9),
    (15, 8),
    (10, 6),
    (5, 4),
    (0, 2)
]
NET_MARGIN_BENCHMARKS = [
    (20, 10),
    (15, 9),
    (10, 8),
    (5, 6),
    (2, 4),
    (0, 2)
]
ROA_BENCHMARKS = [
    (15, 10),
    (10, 9),
    (7, 8),
    (5, 6),
    (2, 4),
    (0, 2)
]
ROE_BENCHMARKS = [
    (25, 10),
    (20, 9),
    (15, 8),
    (10, 6),
    (5, 4),
    (0, 2)
]
CURRENT_RATIO_BENCHMARKS = [
    (2.0, 10),
    (1.75, 9),
    (1.5, 8),
    (1.25, 7),
    (1.0, 6),
    (0.8, 4),
    (0, 2)
]
QUICK_RATIO_BENCHMARKS = [
    (1.5, 10),
    (1.2, 9),
    (1.0, 8),
    (0.8, 6),
    (0.5, 4),
    (0, 2)
]
CASH_RATIO_BENCHMARKS = [
    (1.0, 10),
    (0.8, 9),
    (0.6, 8),
    (0.4, 6),
    (0.2, 4),
    (0, 2)
]
EQUITY_RATIO_BENCHMARKS = [
    (70, 10),
    (60, 9),
    (50, 8),
    (40, 6),
    (30, 4),
    (0, 2)
]
INTEREST_COVERAGE_BENCHMARKS = [
    (15, 10),
    (10, 9),
    (6, 8),
    (3, 6),
    (1.5, 4),
    (0, 2)
]
ASSET_TURNOVER_BENCHMARKS = [
    (2.0, 10),
    (1.5, 9),
    (1.0, 8),
    (0.75, 6),
    (0.5, 4),
    (0, 2)
]
DEBT_TO_ASSETS_BENCHMARKS = [
    (20, 10),
    (30, 9),
    (40, 8),
    (50, 6),
    (60, 4),
    (100, 2)
]
DEBT_TO_EQUITY_BENCHMARKS = [
    (0.25, 10),
    (0.50, 9),
    (1.00, 8),
    (2.00, 6),
    (3.00, 4),
    (100, 2)
]
def calculate_cfhi_scores(
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
):

    scores = {}

    scores["Gross Margin"] = score_ratio(gross_margin,GROSS_MARGIN_BENCHMARKS)
    scores["Operating Margin"] = score_ratio(operating_margin,OPERATING_MARGIN_BENCHMARKS)
    scores["Net Margin"] = score_ratio(net_margin,NET_MARGIN_BENCHMARKS)
    scores["ROA"] = score_ratio(roa,ROA_BENCHMARKS)
    scores["ROE"] = score_ratio(roe,ROE_BENCHMARKS)
    scores["Current Ratio"] = score_ratio(current_ratio,CURRENT_RATIO_BENCHMARKS)
    scores["Quick Ratio"] = score_ratio(quick_ratio,QUICK_RATIO_BENCHMARKS)
    scores["Cash Ratio"] = score_ratio(cash_ratio,CASH_RATIO_BENCHMARKS)
    scores["Debt to Assets"] = score_reverse_ratio(debt_to_assets,DEBT_TO_ASSETS_BENCHMARKS)
    scores["Debt to Equity"] = score_reverse_ratio(debt_to_equity,DEBT_TO_EQUITY_BENCHMARKS)
    scores["Equity Ratio"] = score_ratio(equity_ratio,EQUITY_RATIO_BENCHMARKS)
    scores["Interest Coverage"] = score_ratio(interest_coverage,INTEREST_COVERAGE_BENCHMARKS)
    scores["Asset Turnover"] = score_ratio(asset_turnover,ASSET_TURNOVER_BENCHMARKS)

    profitability = (
        scores["Gross Margin"]
        + scores["Operating Margin"]
        + scores["Net Margin"]
        + scores["ROA"]
        + scores["ROE"]
    ) / 5

    liquidity = (
        scores["Current Ratio"]
        + scores["Quick Ratio"]
        + scores["Cash Ratio"]
    ) / 3

    solvency = (
        scores["Debt to Assets"]
        + scores["Debt to Equity"]
        + scores["Equity Ratio"]
        + scores["Interest Coverage"]
    ) / 4

    efficiency = scores["Asset Turnover"]

    cfhi_score = (
        (profitability * 0.35)
        + (liquidity * 0.25)
        + (solvency * 0.25)
        + (efficiency * 0.15)
    )
    cfhi_score = cfhi_score * 10

    scores["Profitability Score"] = profitability
    scores["Liquidity Score"] = liquidity
    scores["Solvency Score"] = solvency
    scores["Efficiency Score"] = efficiency
    scores["CFHI Score"] = cfhi_score
    
    return scores
