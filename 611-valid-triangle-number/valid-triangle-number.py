class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        c = 0
        for i in range(len(nums)-1, 1, -1):
            l = 0
            r = i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    c += r - l
                    r -= 1
                else:
                    l += 1
        return c