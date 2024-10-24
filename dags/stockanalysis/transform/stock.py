from typing import Dict, List, Tuple

def transform_market_cap(market_cap) -> Tuple[float, str]:
    value = market_cap[:-1]
    value = float(value)
    unit = market_cap[-1]
    return value, unit