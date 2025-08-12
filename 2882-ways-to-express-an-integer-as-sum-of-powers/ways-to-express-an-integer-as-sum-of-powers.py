class Solution(object):
    def numberOfWays(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        powers = []
        i = 1
        while True:
            val = i ** x
            if val > n:
                break
            powers.append(val)
            i += 1
        
        dp = [0] * (n + 1)
        dp[0] = 1  
        
        for val in powers:
            for s in range(n, val - 1, -1):
                dp[s] = (dp[s] + dp[s - val]) % MOD
        
        return dp[n]