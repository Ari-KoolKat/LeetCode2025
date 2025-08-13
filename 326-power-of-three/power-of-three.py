class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x=1
        while x<=n:
            if x==n:
                return True
            x*=3
        return False