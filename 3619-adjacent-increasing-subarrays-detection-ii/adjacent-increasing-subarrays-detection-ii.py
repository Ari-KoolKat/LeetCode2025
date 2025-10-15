class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 1
        
        l = 0  # Last/previous sequence length
        c = 1  # Current sequence length
        m = 0  # Maximum k found
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                c += 1
            else:
                m = max(m, max(c//2, min(c, l)))
                l = c
                c = 1
        
        m = max(m, max(c//2, min(c, l)))
        return m