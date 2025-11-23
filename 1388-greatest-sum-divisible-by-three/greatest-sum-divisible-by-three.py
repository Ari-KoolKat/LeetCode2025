class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        if s % 3 == 0:
            return s
        
        r1 = []
        r2 = []
        
        for x in nums:
            if x % 3 == 1:
                r1.append(x)
            elif x % 3 == 2:
                r2.append(x)
        
        r1.sort()
        r2.sort()
        
        if s % 3 == 1:
            a = r1[0] if r1 else float('inf')
            b = sum(r2[:2]) if len(r2) >= 2 else float('inf')
            return s - min(a, b)
        else:
            a = r2[0] if r2 else float('inf')
            b = sum(r1[:2]) if len(r1) >= 2 else float('inf')
            return s - min(a, b)