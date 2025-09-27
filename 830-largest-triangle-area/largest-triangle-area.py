class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        m=0
        for i in range(len(points)):
            i1,i2=points[i]
            for j in range(i+1,len(points)):
                j1,j2=points[j]
                for k in range(j+1,len(points)):
                    k1,k2=points[k]
                    a=abs(i1*(j2-k2)+j1*(k2-i2)+k1*(i2-j2))
                    m=a if a>m else m
        return m/2.0