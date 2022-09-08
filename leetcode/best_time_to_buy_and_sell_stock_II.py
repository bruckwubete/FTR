from typing import List


def max_profit(prices: List[int]) -> int:
    # go from back and add the ones that show some up side
    j = len(prices) - 1
    profit = 0
    while j >= 0:
        r = prices[j + 1] - prices[j]
        if r > 0:
            profit += r
    return profit
