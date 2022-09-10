from typing import List


def maxProfit(self, prices: List[int]) -> int:
    i = 1
    profit = 0
    current_price = prices[0]
    num_transactions = 0
    unrealized_profit = 0
    while i < len(prices):
        if num_transactions < 2:
            if prices[i] - current_price > 0:
                if unrealized_profit == 0:
                    num_transactions+=1
                unrealized_profit += prices[i] - current_price
            else:
                num_transactions+=1
                profit += unrealized_profit
                unrealized_profit=0
                current_price=prices[i]
        i+=1

    return profit
