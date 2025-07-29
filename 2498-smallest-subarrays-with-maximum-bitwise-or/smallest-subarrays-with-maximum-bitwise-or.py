class Solution(object):
    def smallestSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        digit = {}
        res = [0]*n
        for i in range(n-1,-1,-1):
            num = nums[i]
            shift = 0
            while num: 
                d = num & 1
                if d:
                    digit[d*(2**shift)] = i
                shift += 1
                num >>= 1
            if not digit:
                res[i] = 1
            else:
                res[i] = max(digit.values()) - i + 1 
        return res