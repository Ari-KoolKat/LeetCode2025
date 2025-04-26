class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        n = len(nums)
        last_minK = last_maxK = -1
        last_invalid = -1
        count = 0
        
        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                last_invalid = i
            
            if nums[i] == minK:
                last_minK = i
            
            if nums[i] == maxK:
                last_maxK = i
            
            if last_minK != -1 and last_maxK != -1:
                count += max(0, min(last_minK, last_maxK) - last_invalid)
        
        return count