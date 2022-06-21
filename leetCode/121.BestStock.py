#UNRESOLVED
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = min(prices,)
        ind = prices.index(buy)
        print(buy)
        sell = max(prices[ind:])
        print(sell)
        if buy > sell: return 0
        return (sell - buy)

prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]
prices3 = [2,4,1]
print(Solution.maxProfit(Solution,prices1))
print(Solution.maxProfit(Solution,prices2))
print(Solution.maxProfit(Solution,prices3))
