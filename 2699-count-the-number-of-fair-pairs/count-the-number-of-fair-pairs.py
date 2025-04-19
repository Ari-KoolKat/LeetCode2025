class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()
        return self._countLess(nums, upper) - self._countLess(nums, lower - 1)

    def _countLess(self, nums, sum_val):
        res = 0
        j = len(nums) - 1
        for i in range(len(nums)):
            while i < j and nums[i] + nums[j] > sum_val:
                j -= 1
            if i < j:
                res += j - i
        return res