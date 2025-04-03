class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return 0
        
        max_prefix = [0] * n
        max_prefix[0] = nums[0]
        for i in range(1, n):
            max_prefix[i] = max(max_prefix[i-1], nums[i])
        
        max_diff = [0] * n
        max_diff[1] = max_prefix[0] - nums[1]
        for j in range(2, n):
            current_diff = max_prefix[j-1] - nums[j]
            max_diff[j] = max(max_diff[j-1], current_diff)
        
        max_triplet = 0
        for k in range(2, n):
            current_val = max_diff[k-1] * nums[k]
            if current_val > max_triplet:
                max_triplet = current_val
        
        return max_triplet if max_triplet > 0 else 0