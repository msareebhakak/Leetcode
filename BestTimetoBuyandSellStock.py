# Leetcode 121. Best Time to Buy and Sell Stock
from typing import List


# This is solved via sliding window. Left and Right Pointer.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)
            else:
                left = right
            right += 1

        return max_profit


if __name__ == '__main__':
    prices = [2, 1, 5, 3]
    sol = Solution()
    print(sol.maxProfit(prices))
