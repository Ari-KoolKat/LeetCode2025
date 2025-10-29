class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        while 2**i - 1 < n:
            i += 1
        return 2**i - 1