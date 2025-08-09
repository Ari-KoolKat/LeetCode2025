class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0 or n < 0 :
            return False

        if n==1:
            return True
        
        return self.helper(n)

    def helper(self, n):
        if n == 2:
            return True

        if n % 2 == 1:
            return False

        return self.helper(n // 2)
