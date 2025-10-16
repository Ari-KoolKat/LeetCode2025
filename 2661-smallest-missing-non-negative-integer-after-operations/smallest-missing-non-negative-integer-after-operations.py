class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        counts = [0] * value
        for n in nums:
            counts[n % value] += 1
        small = min(counts)
        mod = counts.index(small)
        return mod + small * value