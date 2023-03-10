import json

# Parse JSONs
with open('lama_data_filtered.json') as f:
    data1 = json.load(f)

with open('liquidity_filtered.json') as f:
    data2 = json.load(f)

# Extract values
tvl_usd = data1[0]['tvlUsd']
apy = data1[0]['apy']
apy_pct_1d = data1[0]['apyPct1D']
apy_pct_7d = data1[0]['apyPct7D']
apy_pct_30d = data1[0]['apyPct30D']

total_liquidity = data2[0]['totalLiquidity']
total_borrows_normalized = data2[0]['totalBorrowsNormalized']
utilization_rate = data2[0]['utilizationRate']
variable_borrow_rate = data2[0]['variableBorrowRate']
stable_borrow_rate = data2[0]['stableBorrowRate']
reserve_liquidation_threshold = data2[0]['reserveLiquidationThreshold']
reserve_liquidation_bonus = data2[0]['reserveLiquidationBonus']
base_ltv_as_collateral = data2[0]['baseLTVasCollateral']
usage_as_collateral_enabled = data2[0]['usageAsCollateralEnabled']
reserve_factor = data2[0]['reserveFactor']

# Create new JSON
result = {
    "tvlUsd": tvl_usd,
    "apy": apy,
    "apyPct1D": apy_pct_1d,
    "apyPct7D": apy_pct_7d,
    "apyPct30D": apy_pct_30d,
    "totalLiquidity": total_liquidity,
    "totalBorrowsNormalized": total_borrows_normalized,
    "utilizationRate": utilization_rate,
    "variableBorrowRate": variable_borrow_rate,
    "stableBorrowRate": stable_borrow_rate,
    "reserveLiquidationThreshold": reserve_liquidation_threshold,
    "reserveLiquidationBonus": reserve_liquidation_bonus,
    "baseLTVasCollateral": base_ltv_as_collateral,
    "usageAsCollateralEnabled": usage_as_collateral_enabled,
    "reserveFactor": reserve_factor
}

# Convert result to JSON string
json_result = json.dumps(result, indent=4)

# write JSON string to file
with open('result.json', 'w') as f:
    f.write(json_result)
