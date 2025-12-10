class Solution(object):
    def countPermutations(self, complexity):
        """
        :type complexity: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(complexity)
        
        if n <= 1:
            return 1
            
        root_val = complexity[0]
        
        for i in range(1, n):
            if complexity[i] <= root_val:
                return 0
                
        ans = 1
        for i in range(2, n):
            ans = (ans * i) % MOD
             
        return ans