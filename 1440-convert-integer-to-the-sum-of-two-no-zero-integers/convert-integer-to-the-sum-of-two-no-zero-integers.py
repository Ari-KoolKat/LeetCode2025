class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(n): #check all number till the n
            j=n-i #other number will be the remaining in n
            if '0' in set(str(i)) or '0' in set(str(j)): #if has 0
                continue
            else: #when both don't have a 0
                return [i,j] #we return both digits
        