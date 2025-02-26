class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minSum=0
        maxSum=0
        prefixSum=0

        for i in range(0, len(nums)):
            prefixSum += nums[i]
            minSum=min(minSum, prefixSum)
            maxSum=max(maxSum, prefixSum)
        
        return maxSum-minSum