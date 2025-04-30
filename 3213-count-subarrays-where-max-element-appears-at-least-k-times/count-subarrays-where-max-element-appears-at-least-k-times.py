class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_val = max(nums)
        count = 0
        left = 0
        ans = 0
        
        for right in range(len(nums)):
            if nums[right] == max_val:
                count += 1
            while count >= k:
                ans += len(nums) - right
                if nums[left] == max_val:
                    count -= 1
                left += 1
        return ans