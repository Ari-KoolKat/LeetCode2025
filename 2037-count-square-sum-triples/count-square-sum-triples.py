class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                if(sqrt(i*i+j*j) in range(1,n+1)):
                    a+=1
        return a 