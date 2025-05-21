class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row_length=len(matrix)
        col_length=len(matrix[0])

        zero_row_length=set()
        zero_col_length=set()

        for i in range(row_length):
            for j in range(col_length):
                if matrix[i][j]==0:
                    zero_row_length.add(i)
                    zero_col_length.add(j)
        
        for i in zero_row_length:
            for j in range(col_length):
                matrix[i][j]=0

        for j in zero_col_length:
            for i in range(row_length):
                matrix[i][j]=0
        return matrix