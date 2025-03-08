class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        n = len(blocks)
        w = blocks[:k].count('W')

        ans = w

        for i in range(k, n):
            if blocks[i] == 'W':
                w += 1  
            if blocks[i - k] == 'W':
                w -= 1  
            ans = min(ans, w) 

        return ans