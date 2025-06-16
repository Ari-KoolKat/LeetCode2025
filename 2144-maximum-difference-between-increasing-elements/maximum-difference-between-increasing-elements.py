class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        mn = 0
        mx = 1
        res = -1
        ind = 2
        while mx < len(nums):
            if nums[mx] < nums[mn] :
                mn = mx
            elif nums[mx] > nums[mn]:
                res = max(res, nums[mx] - nums[mn])
            mx += 1

        return res