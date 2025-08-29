class Solution(object):
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        c=0
        for i in range(1,n+1): #no of flowers start from 1
            if i%2==0:
                c+=(m+1)//2 
                #This is even i pair with every odd till m
            else:
                c+=m//2
                #This odd i will make pair with all even till m
        return c 