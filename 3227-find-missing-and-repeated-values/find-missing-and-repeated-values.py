class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n, seen = len(grid), set()
        repeated = next(num for row in grid for num in row if num in seen or seen.add(num))
        missing = (n * n * (n * n + 1) // 2) - sum(sum(row) for row in grid) + repeated
        return [repeated, missing]