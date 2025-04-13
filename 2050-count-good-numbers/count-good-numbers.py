class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10**9 + 7

        def power(x, y):
            res = 1
            x = x % mod
            while y > 0:
                if y % 2 == 1:
                    res = (res * x) % mod
                y = y // 2
                x = (x * x) % mod
            return res

        even_pos = (n + 1) // 2  
        odd_pos = n // 2         

        return (power(5, even_pos) * power(4, odd_pos)) % mod