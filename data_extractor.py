import json
import requests
from datetime import date, timedelta


def defilama_api():
    lama_pool_id = '405d8dad-5c99-4c91-90d3-82813ade1ff1'
    req = requests.get('https://yields.llama.fi/pools')

    data = json.loads(req.text)
    filtered_data = []

    for i in range(len(data["data"])):
        if data["data"][i]["pool"] == lama_pool_id:
            filtered_data.append(data["data"][i])


    tvlUsd = filtered_data[0]["tvlUsd"]
    apy = filtered_data[0]["apy"]
    apyBase7d = filtered_data[0]["apyBase7d"]
    apyMean30d = filtered_data[0]["apyMean30d"]

    val = {
        "tvlUsd": tvlUsd,
        "apy": apy,
        "apyBase7d": apyBase7d,
        "apyMean30d": apyMean30d
    }
    # return dictionary
    return val


def aave_api():
    # liquidity v2
    pool_id = "0xb53c1a33016b2dc2ff3653530bff1848a515c8c5"
    yesterday = date.today() - timedelta(days=1)

    aave = requests.get(f"https://aave-api-v2.aave.com/data/liquidity/v2?poolId={pool_id}&date={yesterday}")

    data = [d for d in aave.json() if d.get('symbol') == 'DAI']

    extracted_data = {}

    
    for item in data:
        extracted_item = {
            'price': item['price']['priceInEth'],
            'totalLiquidity': item['totalLiquidity'],
            'totalBorrowsNormalized': item['totalBorrowsNormalized'],
            'utilizationRate': item['utilizationRate'],
            'variableBorrowRate': item['variableBorrowRate'],
            'stableBorrowRate': item['stableBorrowRate'],
            'reserveLiquidationThreshold': item['reserveLiquidationThreshold'],
            'reserveLiquidationBonus': item['reserveLiquidationBonus'],
            'baseLTVasCollateral': item['baseLTVasCollateral'],
            'usageAsCollateralEnabled': item['usageAsCollateralEnabled'],
            'reserveFactor': item['reserveFactor']
        }
        extracted_data.update(extracted_item)
    # return dictionary
    return extracted_data