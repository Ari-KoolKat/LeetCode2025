class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ops = 0
        stack = []
        for x in nums:
            while stack and stack[-1] > x:
                stack.pop()
            
            if x > 0:
                if not stack or stack[-1] < x:
                    stack.append(x)
                    ops += 1
                
        return ops