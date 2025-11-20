class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[1], -x[0]))
        r = []
        
        for i in intervals:
            common = 0
            if len(r) >= 1 and i[0] <= r[-1] <= i[1]:
                common += 1
            if len(r) >= 2 and i[0] <= r[-2] <= i[1]:
                common += 1
            
            if common == 0:
                r.append(i[1] - 1)
                r.append(i[1])
            elif common == 1:
                r.append(i[1])
        
        return len(r)