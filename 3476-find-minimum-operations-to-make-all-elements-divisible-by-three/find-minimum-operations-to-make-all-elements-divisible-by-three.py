class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        for i in range(len(nums)):
            r = nums[i] % 3
            if r != 0:
                c += min(r, 3 - r)
        return c