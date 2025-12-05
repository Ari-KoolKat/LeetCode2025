class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        total = sum(nums)
        left = 0
        
        for i in range(len(nums) - 1):
            left += nums[i]
            right = total - left
            if (left - right) % 2 == 0:
                c += 1
                
        return c