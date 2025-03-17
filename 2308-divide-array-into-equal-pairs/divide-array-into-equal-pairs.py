class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c=Counter(nums)
        for i in c:
            if c[i]&1==1:
                return False
        return True