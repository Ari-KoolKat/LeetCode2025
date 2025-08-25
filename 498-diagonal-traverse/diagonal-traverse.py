class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        a=[]
        i,j=len(mat),len(mat[0])
        l=i+j-1
        for k in range(l):
            if k%2==0:
                t=min(k,i-1)
                while t>=0 and k-t<j:
                    a.append(mat[t][k-t])
                    t-=1
            else:
                t=min(k,j-1)
                while t>=0 and k-t<i:
                    a.append(mat[k-t][t])
                    t-=1
        return a