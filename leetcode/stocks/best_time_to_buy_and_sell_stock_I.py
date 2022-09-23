from typing import List


def max_profit(prices: List[int]) -> int:
    min_price = prices[0]
    profit_max = 0
    for i in prices:
        min_price = min(min_price, i)
        profit_max = max(profit_max, i - min_price)
    return profit_max