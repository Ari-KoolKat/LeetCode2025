class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k>min(nums):
            return -1
        if k<min(nums):
            return len(set(nums))
        if k==min(nums):
            return len(set(nums))-1