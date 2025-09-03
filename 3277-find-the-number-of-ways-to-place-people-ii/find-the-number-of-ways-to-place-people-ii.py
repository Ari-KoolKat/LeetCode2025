class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda p:(p[0],-p[1]))
        c=0
        for i in range(len(points)):
            b=float('-inf')
            for j in range(i+1,len(points)):
                if points[i][1]>=points[j][1]:#seeing alice is at higher y coordinate
                    if points[j][1]>b:
                        c+=1
                        b=points[j][1]
        return c
