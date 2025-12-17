class Solution(object):
    def maximumProfit(self, prices, k):
        """
        :type prices: List[int]
        :type k: int
        :rtype: int
        """
        n = len(prices)
        prev = [0] * n
        curr = [0] * n

        for t in range(1, k+1):
            bestLong = -prices[0]
            bestShort = prices[0]
            curr[0] = 0

            for i in range(1, n):
                res = curr[i-1]
                res = max(res, prices[i] + bestLong)
                res = max(res, -prices[i] + bestShort)
                curr[i] = res

                bestLong = max(bestLong, prev[i-1] - prices[i])
                bestShort = max(bestShort, prev[i-1] + prices[i])

            prev, curr = curr, prev

        return prev[n-1]