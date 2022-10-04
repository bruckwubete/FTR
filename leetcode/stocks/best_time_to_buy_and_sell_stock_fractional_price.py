from typing import List


def max_profit(self, k: int, prices: List[int]) -> int:
    dp = {}
    profits = []

    def dfs(i, buying):
        if i >= len(prices):
            return 0
        if (i, buying) in dp:
            return dp[(i, buying)]

        if buying:
            buy = dfs(i + 1, False) - prices[i]
            cooldown = dfs(i + 1, True)
            if buy > cooldown:
                profits.append(buy)
            dp[(i, buying)] = max(buy, cooldown)
        else:
            sell = dfs(i + 1, True) + prices[i]
            cooldown = dfs(i + 1, True)
            dp[(i, buying)] = max(sell, cooldown)

        #print(dp[(i, buying)])
        return dp[(i, buying)]

    dfs(0, True)
    print(profits)
    return sum(sorted(profits, reverse=True)[:k])


