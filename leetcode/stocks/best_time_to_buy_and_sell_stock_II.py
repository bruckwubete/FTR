from typing import List


def maxProfit(self, prices: List[int]) -> int:
    j = len(prices) - 2
    profit = 0
    while j != -1:
        r = prices[j + 1] - prices[j]
        if r > 0:
            profit += r
        j-=1
    return profit
