class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ts = sum(nums)
        ls = 0
        r = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                rs = ts - ls
                if abs(rs - ls) <= 1:
                    if rs == ls:
                        r += 2
                    else:
                        r += 1
            ls += nums[i]
        
        return r