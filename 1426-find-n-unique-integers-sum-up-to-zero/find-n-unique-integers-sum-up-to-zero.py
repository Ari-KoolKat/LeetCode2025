class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]

        """
        l=[]
        for i in range(1, n//2+1):
            l.append(-i)
            l.append(i)
        if n%2==0:
            return l
        else :
            l.append(0)
        return l