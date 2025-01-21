class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        n = len(grid[0])
        if n==1:
            return 0
        for i in range(1,n):
            grid[1][i]+=grid[1][i-1]
        for i in range(n-2, -1, -1):
            grid[0][i]+=grid[0][i+1]
        
        m = float('inf')
        for i in range(n):
            if i == 0:
                m = min(m, grid[0][i+1])
            elif i == n-1:
                m = min(m, grid[1][i-1])
            else:
                m = min(m,max( grid[0][i+1], grid[1][i-1]))
        return m