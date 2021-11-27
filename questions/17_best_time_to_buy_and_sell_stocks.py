"""
Question - You are given an array prices where prices[i] is the price of a given stock on the ith day.
            You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
            Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

example -
        [7,1,5,3,6,4]

        answer - 5
"""

class Solution:
    def maxProfit(self, prices):
        length=len(prices)
        max_profit = 0
        pick = prices[0]
        for i in prices:
            if pick > i:
                pick = i
            if pick < i and max_profit < (i-pick):
                max_profit = i-pick
        return max_profit

solution = Solution()
inp = [7,6,4,3,2]
print(solution.maxProfit(inp))