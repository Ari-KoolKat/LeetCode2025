class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        weeks = n // 7          
        days = n % 7            
        total = 28 * weeks + (weeks * (weeks - 1) * 7) // 2

        start = weeks + 1
        total += (2 * start + (days - 1)) * days // 2

        return total