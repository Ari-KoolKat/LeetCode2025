class Solution(object):
    def rangeAddQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[List[int]]
        """
        mat = [[0 for _ in range(n)] for _ in range(n)]

        for r1, c1, r2, c2 in queries:
            mat[r1][c1] += 1
            if c2 + 1 < n:
                mat[r1][c2 + 1] -= 1
            if r2 + 1 < n:
                mat[r2 + 1][c1] -= 1
            if r2 + 1 < n and c2 + 1 < n:
                mat[r2 + 1][c2 + 1] += 1

        for r in range(n):
            for c in range(1, n):
                mat[r][c] += mat[r][c-1]

        for c in range(n):
            for r in range(1, n):
                mat[r][c] += mat[r-1][c]

        return mat