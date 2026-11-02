# Best Time to Buy and Sell Stock — Easy (#121)
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

r"""
You are given an array prices where prices[i] is the price of a given stock on the
i^th day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.

Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
    6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must
    buy before you sell.

Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
  - 1 <= prices.length <= 10^5
  - 0 <= prices[i] <= 10^4

Tags: array, dynamic-programming"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price = prices[0]
        max_profit = 0
        for sell_price in prices:
            buy_price = min(buy_price, sell_price)
            profit = sell_price - buy_price
            max_profit = max(max_profit, profit)
        return max_profit


CASES = [
    (([7, 1, 5, 3, 6, 4],), 5),
    (([7, 6, 4, 3, 1],), 0),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().maxProfit, CASES)
