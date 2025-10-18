class Solution(object):
    def maxDistinctElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        f = float('-inf')
        r = 0
        nums.sort()
        for i in nums:
            l = i - k
            u = i + k
            if f < l:
                f = l
                r += 1
            elif f < u:
                f += 1
                r += 1
        return r