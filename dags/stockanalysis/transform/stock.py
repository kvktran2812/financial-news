from typing import Dict, List, Tuple

def transform_market_cap(market_cap) -> Tuple[float, str]:
    if market_cap != "-":
        value = market_cap[:-1].replace(",", "")
        value = float(value)
        unit = market_cap[-1]
    else:
        value = 0
        unit = "N"
    return value, unit