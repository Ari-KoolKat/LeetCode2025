class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low, high = min(nums), max(nums)

        def canRob(cap):
            count, i = 0, len(nums)
            j = 0 
            while j < i:
                if nums[j] <= cap:
                    count += 1
                    if count >= k:  
                        return True
                    j += 1  
                j += 1  
            return count >= k

        while low < high:
            mid = (low + high) // 2
            if canRob(mid):
                high = mid  
            else:
                low = mid + 1 
        
        return low