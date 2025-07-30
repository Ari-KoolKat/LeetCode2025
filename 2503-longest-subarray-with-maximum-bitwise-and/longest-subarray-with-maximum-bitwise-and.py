class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = 0
        max_val = 0

        # 1st loop to find the maximum value
        for num in nums:
            max_val = max(max_val, num)

        # 2nd loop to find the longest contiguous subarray of the maximum value
        count = 0
        for num in nums:
            if num == max_val:
                count += 1
                length = max(length, count)
            else:
                count = 0

        return length