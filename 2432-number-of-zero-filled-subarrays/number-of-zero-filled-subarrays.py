class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        curr_zeroes = 0
        for n in nums:
            if n == 0:
                curr_zeroes += 1
                count += curr_zeroes
            else:
                curr_zeroes = 0
        return count