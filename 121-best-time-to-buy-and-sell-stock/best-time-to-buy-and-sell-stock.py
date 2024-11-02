class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        dp = [0] * n
        min_p = prices[0]

        for i in range(1, n):
            if prices[i] < min_p:
                min_p = prices[i]
            dp[i] = max(dp[i - 1], prices[i] - min_p)

        return dp[-1]
