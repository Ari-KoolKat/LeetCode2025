class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        arr = [num for row in grid for num in row]
        arr.sort()
        
        remainder = arr[0] % x
        if any(num % x != remainder for num in arr):
            return -1
        
        median = arr[len(arr) // 2]
        return sum(abs(num - median) // x for num in arr)