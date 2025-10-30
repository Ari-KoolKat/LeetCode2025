class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        last = 0
        ops = 0

        for i in target :
            if i > last:
                ops += i-last
            last = i
        return ops
