class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        diff_a = [0] * (len(nums)+1)
        for l, r in queries:
            diff_a[l] -= 1
            diff_a[r+1] += 1
        current = 0
        for i in range(len(nums)):
            current += diff_a[i]
            if nums[i] + current > 0:
                return False
        return True