class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        count = 0
        for i in range(n):
            Ax, Ay = points[i]
            for j in range(n):
                Bx, By = points[j]
                if i == j:
                    continue
                if Ax <= Bx and By <= Ay:
                    empty = True
                    for k in range(n):
                        if k == i or k == j:
                            continue    
                        Px, Py = points[k]
                        if Ax <= Px <= Bx and By <= Py <= Ay:
                            empty = False
                            break
                    if empty:
                        count += 1
        return count
