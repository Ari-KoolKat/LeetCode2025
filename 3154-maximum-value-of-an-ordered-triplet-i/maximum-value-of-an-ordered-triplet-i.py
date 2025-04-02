class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_i = nums[0] 
        max_ij = float('-inf') 
        max_ijk = 0  
        
        for j in range(1, n - 1):
            max_ij = max(max_ij, max_i - nums[j])
            max_ijk = max(max_ijk, max_ij * nums[j + 1])
            max_i = max(max_i, nums[j])  
        
        return max_ijk