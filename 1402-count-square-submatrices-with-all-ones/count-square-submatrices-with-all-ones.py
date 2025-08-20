class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        t=0
        r=len(matrix)
        c=len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==1:
                    if i>0 and j>0:
                        matrix[i][j]=1+min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])
                    t+=matrix[i][j]
        return t