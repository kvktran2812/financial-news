from stockanalysis.stock.overview import *
from stockanalysis.transform.stock import *

metadata, data = get_all_stocks(early_stop=True)
print(metadata)

for i in range(5):
    value, unit = transform_market_cap(data[i][-1])
    print(data[i], value, unit)