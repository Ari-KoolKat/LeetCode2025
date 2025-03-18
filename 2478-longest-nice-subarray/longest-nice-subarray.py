class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mark = 0
        res = 1
        for i in range(1, len(nums)):
            j = i - 1
            while j >= mark:
                if nums[i] & nums[j]:
                    break
                j -= 1
            
            mark = j + 1
            res = max(res, i - mark + 1)
        
        return res