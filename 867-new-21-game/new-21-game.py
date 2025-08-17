class Solution(object):
    def new21Game(self, n, k, maxPts):
        """
        :type n: int
        :type k: int
        :type maxPts: int
        :rtype: float
        """
        if k == 0 or n >= k + maxPts:
            return 1.0
        
        dp = [0.0] * (n + 1)
        dp[0] = 1.0 
        
        Wsum = 1.0  
        result = 0.0
        
        for i in range(1, n + 1):
            dp[i] = Wsum / maxPts  
            
            if i < k:
                Wsum += dp[i]  
            else:
                result += dp[i]  
            
            if i >= maxPts:
                Wsum -= dp[i - maxPts]  
        
        return result