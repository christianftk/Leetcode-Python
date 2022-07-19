#UNRESOLVED
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for i, buy_price in enumerate(prices):
            sell_price = max(prices[i:])
            profit = max(profit, sell_price - buy_price)
        return profit

prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]
prices3 = [2,4,1]
print(Solution.maxProfit(Solution,prices1))
print(Solution.maxProfit(Solution,prices2))
print(Solution.maxProfit(Solution,prices3))
