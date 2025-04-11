class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        def is_symmetric(n):
            s = str(n)
            if len(s) % 2 != 0:
                return False
            mid = len(s) // 2
            left = sum(map(int, s[:mid]))
            right = sum(map(int, s[mid:]))
            return left == right

        count = 0
        for i in xrange(low, high + 1):
            if is_symmetric(i):
                count += 1
        return count