class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        current_sum = 0
        result = 0
        
        for end in range(len(nums)):
            current_sum += nums[end]
            
            while current_sum * (end - start + 1) >= k:
                current_sum -= nums[start]
                start += 1
            
            result += (end - start + 1)
        
        return result