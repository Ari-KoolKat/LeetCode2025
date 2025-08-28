class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        diag_list = [[] for _ in range(2*n-1)]
        for i in range(n):
            for j in range(n):
                diag_list[i-j+n-1].append(grid[i][j])
        for i in range(n-1):
            diag_list[i].sort()
        for i in range(n-1,2*n-1):
            diag_list[i].sort(reverse =True)
        # print(diag_list)
        for i in range(2*n-1):
            for j in range(len(diag_list[i])):
                row = max(0,i-n+1)+j
                col = max(0,n-1-i)+j
                grid[row][col] = diag_list[i][j]
        return grid