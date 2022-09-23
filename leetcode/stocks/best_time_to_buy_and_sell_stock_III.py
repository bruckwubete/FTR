from typing import List
import sys


def maxProfit(self, prices: List[int]) -> int:
    fs = ss = 0
    fb = sb = ~sys.maxsize
    for i in prices:
        fb = max(fb, -1 * i)
        fs = max(fs, fb + i)
        sb = max(sb, fs - i)
        ss = max(ss, sb + i)
    return ss


def max_profit_2(self, prices: List[int]) -> int:
    dp = {}
    profits = []

    def dfs(i, buying):
        if i > len(prices):
            return 0
        if (i, buying) in dp:
            return dp[(i, buying)]

        if buying:
            buy = dfs(i + 1, False) - prices[i]
            cooldown = dfs(i + 1, True)
            dp[(i, buying)] = max(buy, cooldown)
        else:
            sell = dfs(i + 2, True) + prices[i]
            cooldown = dfs(i + 1, True)
            dp[(i, buying)] = max(sell, cooldown)
            profits.append(dp[(i, buying)])
        return dp[(i, buying)]

    dfs(0, True)
    return sum(profits.sort(reverse=True)[:2])
